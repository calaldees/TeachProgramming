using System;

public class Task
{
    public static void Main(string[] args) { new Task(); }
    Task() {
        // https://docs.microsoft.com/en-us/dotnet/api/system.console?view=net-5.0#common-operations
        Console.WriteLine(Console.BufferWidth);
        Console.WriteLine(Console.BufferHeight);
        Console.Clear();
        Console.WriteLine(Console.CursorLeft);
        Console.WriteLine(Console.CursorTop);
        Console.Clear();
        Console.SetCursorPosition(10, 10);
        
        Console.ForegroundColor = ConsoleColor.Red;
        Console.Write("Yee");
        Console.SetCursorPosition(10, 10);
        Console.ForegroundColor = ConsoleColor.Green;
        Console.Write("P");
        Console.BackgroundColor = ConsoleColor.Red;
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.SetCursorPosition(0, 0);
        Console.Write(Console.WindowHeight);
        
    }
}