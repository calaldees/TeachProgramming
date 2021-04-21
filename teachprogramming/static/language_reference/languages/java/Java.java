/*
Java  // VER: title
https://www.oracle.com/uk/java/technologies/javase-downloads.html  // VER: download
Java SE (Standard Edition) JDK (Java Development Kit)                       // VER: download
http://java.sun.com/docs/books/tutorial/                                    // VER: help

javac HelloWorld.java && java HelloWorld                        # VER: run
// NOTE: filename and `public FILENAME {` must match name+case  # VER:run
*/

import java.util.Scanner; //Add at top of file                                  // VER: read_line_from_console

import java.io.BufferedReader; //Add at top of file                             // VER: file_read
import java.io.FileReader;                                                      // VER: file_read

import java.io.BufferedWriter; //Add at top of file                             // VER: file_write
import java.io.FileWriter;                                                      // VER: file_write
 
  


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

  void if_statement() {
    String username = "bob";
    Integer count = 3;

    if (count >= 5 && username.equals("Jim")) {                                 // VER: if_statement
      System.out.println("Yes");                                                // VER: if_statement
    }                                                                           // VER: if_statement
    else if (username == "admin") {                                             // VER: if_statement
      System.out.println("Admin");                                              // VER: if_statement
    }                                                                           // VER: if_statement
    else {                                                                      // VER: if_statement
      System.out.println("No");                                                 // VER: if_statement
    }
  }

  void for_loop() {
    String username = "Jim";
    for (Integer i=0 ; i < username.length() ; i++) {                           // VER: for_loop
      System.out.println(username.charAt(i));                                   // VER: for_loop
    }                                                                           // VER: for_loop
  }

  void while_loop() {
    Integer count = 0;  // VER: while_loop
    while (count < 10) {  // VER: while_loop
      System.out.println("Count is " + count);  // VER: while_loop
      count = count + 2;  // VER: while_loop
    }  // VER: while_loop
  }

  void for_each_loop() {
    String[] names = {"Bob","Ben","Bill","Borris","Bin"}; // VER: for_each_loop
    for (String name: names) {  // VER: for_each_loop
      System.out.println(name);  // VER: for_each_loop
    }  // VER: for_each_loop
  }


// TODO: java8? https://howtodoinjava.com/java8/java-8-write-to-file-example/
  void file_write() {
    String line_to_write = "Append to end of file"; // VER: file_write
    try { // VER: file_write
      BufferedWriter file = new BufferedWriter(new FileWriter("out.txt", true));  // VER: file_write
      file.write(line_to_write); // VER: file_write
      file.close(); // VER: file_write
    } // VER: file_write
    catch (Exception e){ // VER: file_write
      System.err.println("Error: " + e.getMessage()); // VER: file_write
    } // VER: file_write
  }


  void file_read() {
    try {                                                                       // VER: file_read
      int line_count = 0;                                                       // VER: file_read
      String line;                                                              // VER: file_read
      BufferedReader input =  new BufferedReader(new FileReader("in.txt"));     // VER: file_read
      while (( line = input.readLine()) != null) {                              // VER: file_read
        System.out.println("Line " + line_count + ": " + line);                 // VER: file_read
        line_count += 1;                                                        // VER: file_read
      }                                                                         // VER: file_read
      input.close();                                                            // VER: file_read
    }                                                                           // VER: file_read
    catch (Exception e) {                                                       // VER: file_read
      System.err.println("Error: " + e.getMessage());                           // VER: file_read
    }                                                                           // VER: file_read
  }


  void function() {
    sayHello();
  }
  void sayHello() {  // VER: function
    System.out.println("Hello");  // VER: function
    System.out.println("Goodbye");  // VER: function
  }  // VER: function

  void function_with_return_value() {
    System.out.println(biggest(1,2));
  }
  Integer biggest(Integer a, Integer b) {  // VER: function_with_return_value
    if (a > b) {   // VER: function_with_return_value
      return a;  // VER: function_with_return_value
    } // VER: function_with_return_value
    else { // VER: function_with_return_value
      return b; // VER: function_with_return_value
    } // VER: function_with_return_value
  }


  void define_fixed_array() {
    String[] names = new String[3];  // VER: define_fixed_array
    names[0] = "Bob"; // VER: define_fixed_array
    names[1] = "Foo";  // VER: define_fixed_array
    names[2] = "Rah";  // VER: define_fixed_array
    for (String name : names) {  // VER: define_fixed_array
      System.out.println(name);  // VER: define_fixed_array
    }  // VER: define_fixed_array
    System.out.println("array size is "+names.length);  // VER: define_fixed_array
   }  // VER: define_fixed_array

  //----------------------------------------------------------------------------

  public static void main(String[] args) {new Java();}
  public Java() {
    hello_world();
    //read_line_from_console();
    define_variables();
    define_constants();
    arithmetic();
    if_statement();
    for_loop();
    while_loop();
    for_each_loop();
    file_read();
    function();
    function_with_return_value();
  }

}