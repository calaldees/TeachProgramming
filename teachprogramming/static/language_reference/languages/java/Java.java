/*
Java                                                                        // VER: title
java.sun.com                                                                // VER: download
Java SE (Standard Edition) JDK (Java Development Kit)                       // VER: download
http://java.sun.com/docs/books/tutorial/                                    // VER: help
*/

import java.util.Scanner; //Add at top of file                                  // VER: read_line_from_console

import java.io.BufferedReader; //Add at top of file                             // VER: read_file
import java.io.FileReader;                                                      // VER: read_file


public class Java {

    Scanner console = new Scanner(System.in);                                   // VER: read_line_from_console
    
    void hello_world() {
        //public class HelloWorld {                                             // VER: hello_world
            //public static void main(String[] args) {                          // VER: hello_world
                System.out.println("Hello World");                              // VER: hello_world
            //}                                                                 // VER: hello_world
        //}                                                                     // VER: hello_world
    }
    
    void read_line_from_console() {
        String username = console.nextLine();                                   // VER: read_line_from_console
    }

    void read_file() {
        try {                                                                   // VER: read_file
            int line_count = 0;                                                 // VER: read_file
            String line;                                                        // VER: read_file
            BufferedReader input =  new BufferedReader(new FileReader("in.txt"));// VER: read_file
            while (( line = input.readLine()) != null) {                        // VER: read_file
                System.out.println("Line " + line_count + ": " + line);         // VER: read_file
                line_count += 1;                                                // VER: read_file
            }                                                                   // VER: read_file
            input.close();                                                      // VER: read_file
        }                                                                       // VER: read_file
        catch (Exception e) {                                                   // VER: read_file
            System.err.println("Error: " + e.getMessage());                     // VER: read_file
        }                                                                       // VER: read_file
    }
    
    //--------------------------------------------------------------------------
    
    public static void main(String[] args) {
        Java j = new Java();
        j.hello_world();
        j.read_file();
    }
}