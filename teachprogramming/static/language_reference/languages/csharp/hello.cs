// sudo apt-get install mono-mcs -y
// bash shortcut
// function csharp { mcs "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe"; }

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine ("Hello Mono World");
    }
}
