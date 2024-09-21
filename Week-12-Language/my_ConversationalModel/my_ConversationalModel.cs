using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class my_ConversationalModel {
    private Dictionary<string, string> responses = new Dictionary<string, string> {
        { "hello", "Hi there!" },
        { "how are you", "I'm doing well, thank you!" },
        { "what is your name", "I'm a conversational model. My name is Survi" },
        { "tell me a joke", "Why don't scientists trust atoms? Because they make up everything!" },
        { "my name is", "Nice to meet you!" },
        { "happy", "I'm glad to hear that!" },
        { "sad", "I'm sorry to hear that. I hope things get better soon." },
        { "goodbye", "Goodbye! Have a great day!" },
        { "help", "I can assist you with various tasks. Feel free to ask me anything!" },
        { "thanks", "You're welcome!" },    
        { "who developed you", "I am Survi conversational model. I am developed by Majumder industries."}
    };

    private Dictionary<string, List<string>> synonyms = new Dictionary<string, List<string>> {
        { "hello", new List<string> { "hi", "hey", "greetings" } },
        { "how are you", new List<string> { "how's it going", "how do you do", "what's up" } },
        { "what is your name", new List<string> { "who are you", "your name" } },
        { "calculator", new List<string> { "calc", "math", "compute" } },
        { "developed", new List<string> { "created", "built", "made" } },
        { "thanks", new List<string> { "thank you", "appreciate it", "grateful" } },
        { "goodbye", new List<string> { "bye", "farewell", "see you later" } },
        { "help", new List<string> { "assist", "support", "guide" } },
        { "who developed you", new List<string> { "who created you", "who built you", "who made you" } }
    };

    private Dictionary<string, string> context = new Dictionary<string, string>();
    private Calculator cal = new Calculator();

    public string GetResponse(string input) {
        input = Normalize(input);
        string response = PatternMatching(input);
        if (response == null && input.Contains("calculator")) {
            response = "Calculator mode activated. Do you want to continue? (Y/N)";
            context["mode"] = "calculator";
        } else if (context.ContainsKey("mode") && context["mode"] == "calculator") {
            response = HandleCalculator(input);
        }
        return response ?? "I don't understand that.";
    }

    private string Normalize(string input) {
        input = input.ToLower();
        input = Regex.Replace(input, @"[^\w\s]", "");
        return input;
    }

    private string PatternMatching(string input) {
        foreach (var pattern in responses.Keys) {
            if (Regex.IsMatch(input, $@"\b{pattern}\b")) {
                return responses[pattern];
            }
        }

        foreach (var synonym in synonyms) {
            foreach (var word in synonym.Value) {
                if (Regex.IsMatch(input, $@"\b{word}\b")) {
                    return responses[synonym.Key];
                }
            }
        }
#pragma warning disable CS8603
        return null;
#pragma warning restore CS8603
    }

    private string NamedEntityRecognition(string input) {
        // Simple NER implementation
        if (Regex.IsMatch(input, @"\bmy name is (\w+)\b")) {
            var match = Regex.Match(input, @"\bmy name is (\w+)\b");
            var name = match.Groups[1].Value;
            context["name"] = name;
            return $"Nice to meet you, {name}!";
        }
#pragma warning disable CS8603
        return null;
#pragma warning restore CS8603
    }

    private string SentimentAnalysis(string input) {
        // Simple sentiment analysis
        if (Regex.IsMatch(input, @"\b(happy|great|good)\b")) {
            return "I'm glad to hear that!";
        }
        else if (Regex.IsMatch(input, @"\b(sad|bad|terrible)\b")) {
            return "I'm sorry to hear that. I hope things get better soon.";
        }
#pragma warning disable CS8603
        return null;
#pragma warning restore CS8603
    }

    private string DynamicResponseGeneration(string input) {
        // Use context to generate dynamic responses
        if (context.ContainsKey("name")) {
            return $"How can I assist you today, {context["name"]}?";
        }
#pragma warning disable CS8603
        return null;
#pragma warning restore CS8603
    }


    // Fetching the Calculator.cs file and its methods for operations
    private string HandleCalculator(string input) {
        if (input == "n") {
            context.Remove("mode");
            return "Exiting calculator mode.";
        } else if (input == "y") {
            return "Enter two numbers followed by the operation (+, -, *, /, root, square, cube):";
        } else {
            var parts = input.Split(' ');
            if (parts.Length == 3) {
                double num1 = double.Parse(parts[0]);
                double num2 = double.Parse(parts[1]);
                string operation = parts[2];
                
                double result = operation switch {
                    "+" => cal.Add(num1, num2),
                    "-" => cal.Subtract(num1, num2),
                    "*" => cal.Multiply(num1, num2),
                    "/" => cal.Divide(num1, num2),
                    "root" => cal.SquareRoot(num1),
                    "square" => cal.Power(num1, num2),
                    "%" => cal.Modulo(num1, num2),
                    _ => throw new InvalidOperationException("Invalid operation")
                };
                return $"The result is: {result}. Continue? (Y/N)";
            }
            return "Invalid input. Please enter two numbers followed by the operation.";
        }
    }
}
