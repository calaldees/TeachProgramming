/*
C#                                                                              // VER: title

Visual Studio Comunity                                                          // VER: download
https://visualstudio.microsoft.com/downloads/                                   // VER: download

https://docs.microsoft.com/en-us/dotnet/csharp/                                 // VER: help
https://www.tutorialspoint.com/csharp/index.htm                                 // VER: help

# TODO: install mono                                                            // VER: run
function csharp { mcs "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe"; } // VER: run
# linux bash function                                                           // VER: run

*/

using System;                                                                   // VER: hello_world
using System.IO;                                                                // VER: file_write

public class CSharp {

  void hello_world() {
  // public class HelloWorld {                                                  // VER: hello_world
  //   public static void Main(string[] args) {new HelloWorld();}               // VER: hello_world
  //   HelloWorld() {                                                           // VER: hello_world
          Console.WriteLine("Hello World");                                     // VER: hello_world
  //   }                                                                        // VER: hello_world
  // }                                                                          // VER: hello_world
  }

  void read_line_from_console() {
    string username = Console.ReadLine();                                       // VER: read_line_from_console
  }

  void comment() {
      // // This is a comment                                                   // VER: comment
      // /* this is a multiline comment */                                      // VER: comment
  }

  void define_variables() {
    int count = 0;                                                              // VER: define_variables
    string username = "Betty";                                                  // VER: define_variables
    double distance = 3.14;                                                     // VER: define_variables
    bool email_errors = true;                                                   // VER: define_variables
  }

  void define_constants() {
    const double GRAVITY = 9.81;                                                // VER: define_constants
  }

  void arithmetic() {
    int xpos = 0;
    double distance = 0;
    int total_cost = 0;
    int remainder = 0;
    int item_price = 0;
    int quant = 0;
    int count = 0;

    xpos = xpos + 1;                  // VER: arithmetic
    distance = 3 / 4;                 // VER: arithmetic
    total_cost = item_price * quant;  // VER: arithmetic
    remainder = 14 % 11;              // VER: arithmetic
    count += 1;                       // VER: arithmetic

    Console.WriteLine(xpos);
    Console.WriteLine(distance);
    Console.WriteLine(total_cost);
    Console.WriteLine(remainder);
    Console.WriteLine(count);
  }

  void if_statement() {
    string username = "bob";
    int count = 3;

    if (count >= 5 && username == "Jim") {                                      // VER: if_statement
      Console.WriteLine("Yes");                                                 // VER: if_statement
    }                                                                           // VER: if_statement
    else if (username == "admin" || username == "Bob") {                        // VER: if_statement
      Console.WriteLine("Admin");                                               // VER: if_statement
    }                                                                           // VER: if_statement
    else {                                                                      // VER: if_statement
      Console.WriteLine("No");                                                  // VER: if_statement
    }                                                                           // VER: if_statement
  }

  void for_loop() {
    string username = "Jim";                                                    // VER: for_loop
    for (int i=0 ; i < username.Length ; i++) {                                 // VER: for_loop
      Console.WriteLine(username[i]);                                           // VER: for_loop
    }                                                                           // VER: for_loop
  }

  void while_loop() {
    int count = 0;  // VER: while_loop
    while (count < 10) {  // VER: while_loop
      Console.WriteLine("Count is " + count);  // VER: while_loop
      count = count + 2;  // VER: while_loop
    }  // VER: while_loop
  }

  void for_each_loop() {
    string[] names = new string[]{"Bob","Ben","Bill","Boris","Bin"}; // VER: for_each_loop
    foreach (string name in names) {  // VER: for_each_loop
      Console.WriteLine(name);  // VER: for_each_loop
    }  // VER: for_each_loop
  }


  void file_write() {
    string line_to_write = "Append to end of file"; // VER: file_write
    try { // VER: file_write
      using (StreamWriter file = new StreamWriter("out.txt")) {  // VER: file_write
        file.WriteLine(line_to_write);   // VER: file_write
      }
      //file.Close();
    } // VER: file_write
    catch (Exception e){ // VER: file_write
      Console.Error.WriteLine($"Error: {e.Message}"); // VER: file_write
    } // VER: file_write
  }

  void file_read() {
    int line_count = 0;                                                         // VER: file_read
    string line;                                                                // VER: file_read

    // // With context manager - for object that support `IDisposable`
    try {                                                                       // VER: file_read
      // StreamReader input = new StreamReader("in.txt");                         // VER: file_read_old
      using (StreamReader input = new StreamReader("in.txt")) {                 // VER: file_read
        while (( line = input.ReadLine()) != null) {                            // VER: file_read
          Console.WriteLine($"Line {line_count}: {line}");                      // VER: file_read
          line_count += 1;                                                      // VER: file_read
        }                                                                      // VER: file_read
      }                                                                         // VER: file_read
      //input.Close();                                                            // VER: file_read_old
    }                                                                           // VER: file_read
    catch (Exception e) {                                                       // VER: file_read
      Console.Error.WriteLine($"Error: {e.Message}");                           // VER: file_read
    }                                                                           // VER: file_read


  }


  public static void Main(string[] args) {new CSharp();}
  CSharp() {
      hello_world();
      //read_line_from_console();
      comment();
      define_variables();
      define_constants();
      arithmetic();
      if_statement();
      for_loop();
      while_loop();
      for_each_loop();
      file_write();
      file_read();
  }
}


/*
List<int> termsList = new List<int>();
for (int runs = 0; runs < 400; runs++)
{
    termsList.Add(value);
}

// You can convert it back to an array if you would like to
int[] terms = termsList.ToArray();
*/


