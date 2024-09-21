using System;

class Program {
    static void Main(string[] args) {
        if (args.Length > 0) {
            var model = new my_ConversationalModel();
            string input = string.Join(" ", args);
            string res = model.GetResponse(input);
            Console.WriteLine(res);
        }
    }
}