// bash shortcut
// function cs { mcs "$1" && mono "${1%.*}.exe" && rm "${1%.*}.exe"; }

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine ("Hello Mono World");
    }
}
