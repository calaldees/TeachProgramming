using System;

using System.Text.Json;

namespace Dotnet6Test {
    class Program  // Must match what is in `main.csproj`
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World 2!");
            /*
            dynamic stuff = JsonConvert.DeserializeObject("{ 'Name': 'Jon Smith', 'Address': { 'City': 'New York', 'State': 'NY' }, 'Age': 42 }");

            string name = stuff.Name;
            string address = stuff.Address.City;
            */

            var stringifiedJson = @"{ ""Topic"":""Json Serialization Part 1"",""Part"":1,""Author"":""Marc"",""Co-Author"":""Helen"",""Keywords"":[""json"",""netcore"",""parsing""]}";
            var blogPost = JsonDocument.Parse(stringifiedJson);
            var topic = blogPost.RootElement.GetProperty("Topic").GetString();
            Console.WriteLine(topic);

        }
    }
}