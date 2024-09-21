using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class my_ConversationalModel {
    private Dictionary<string, string> responses = new Dictionary<string, string> {
        { "hello", "Hi there!" },
        { "how are you", "I'm doing well, thank you!" },
        { "what is your name", "I'm a conversational model." },
        { "tell me a joke", "Why don't scientists trust atoms? Because they make up everything!" }
    };

    private Dictionary<string, List<string>> synonyms = new Dictionary<string, List<string>> {
        { "hello", new List<string> { "hi", "hey", "greetings" } },
        { "how are you", new List<string> { "how's it going", "how do you do", "what's up" } },
        { "what is your name", new List<string> { "who are you", "your name" } }
    };

    private Dictionary<string, string> context = new Dictionary<string, string>();

    public string GetResponse(string input) {
        input = Normalize(input);
        string response = PatternMatching(input);
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
}
