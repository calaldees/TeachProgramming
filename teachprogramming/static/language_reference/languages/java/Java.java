/*
Java  // VER: title
https://www.oracle.com/uk/java/technologies/javase-downloads.html  // VER: download
Java SE (Standard Edition) JDK (Java Development Kit)                       // VER: download
http://java.sun.com/docs/books/tutorial/                                    // VER: help

javac HelloWorld.java && java HelloWorld                        # VER: run
// NOTE: filename and `public FILENAME {` must match name+case  # VER:run
*/

import java.util.Scanner; //Add at top of file                                  // VER: read_line_from_console

import java.io.BufferedReader; //Add at top of file                             // VER: read_file
import java.io.FileReader;                                                      // VER: read_file


public class Java {

  Scanner console = new Scanner(System.in);                                     // VER: read_line_from_console
    
  void hello_world() {
    // // Must be in file named `HelloWorld.java`                               // VER: hello_world
    //public class HelloWorld {                                                 // VER: hello_world
      //public static void main(String[] args) {new HelloWorld()}               // VER: hello_world
      //public HelloWorld() {                                                   // VER: hello_world
          System.out.println("Hello World");                                    // VER: hello_world
      //}                                                                       // VER: hello_world
    //}                                                                         // VER: hello_world
  }
    
  void read_line_from_console() {
    String username = console.nextLine();                                       // VER: read_line_from_console
  }

  void comment() {
    //This is a comment                                                         // VER: comment
    ///* this is a multiline comment */                                         // VER: comment
  }

  void define_variables() {
    Integer count = 0;                                                          // VER: define_variables
    String username = "Betty";                                                  // VER: define_variables
    Double distance = 3.14;                                                     // VER: define_variables
    Boolean email_errors = true;                                                // VER: define_variables
  }

  void define_constants() {
    final double GRAVITY = 9.81;                                                // VER: define_constants
  }

  void arithmetic() {
    Integer xpos = 0;
    Double distance = 0d;
    Integer total_cost = 0;
    Integer remainder = 0;
    Integer item_price = 0;
    Integer quant = 0;
    Integer count = 0;

    xpos = xpos + 1;                                                            // VER: arithmetic
    distance = 3d / 4d;                                                         // VER: arithmetic
    total_cost = item_price * quant;                                            // VER: arithmetic
    remainder = 14 % 11;                                                        // VER: arithmetic
    count += 1;                                                                 // VER: arithmetic

    System.out.println(xpos);
    System.out.println(distance);
    System.out.println(total_cost);
    System.out.println(remainder);
    System.out.println(count);
  }


  void read_file() {
    try {                                                                       // VER: read_file
      int line_count = 0;                                                       // VER: read_file
      String line;                                                              // VER: read_file
      BufferedReader input =  new BufferedReader(new FileReader("in.txt"));     // VER: read_file
      while (( line = input.readLine()) != null) {                              // VER: read_file
        System.out.println("Line " + line_count + ": " + line);                 // VER: read_file
        line_count += 1;                                                        // VER: read_file
      }                                                                         // VER: read_file
      input.close();                                                            // VER: read_file
    }                                                                           // VER: read_file
    catch (Exception e) {                                                       // VER: read_file
      System.err.println("Error: " + e.getMessage());                           // VER: read_file
    }                                                                           // VER: read_file
  }

  //----------------------------------------------------------------------------

  public static void main(String[] args) {new Java();}
  public Java() {
    hello_world();
    read_file();
  }

}