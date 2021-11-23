using System;

//namespace HelloWorld
//{
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
        dynamic stuff = JsonConvert.DeserializeObject("{ 'Name': 'Jon Smith', 'Address': { 'City': 'New York', 'State': 'NY' }, 'Age': 42 }");

        string name = stuff.Name;
        string address = stuff.Address.City;
    }
}
//}