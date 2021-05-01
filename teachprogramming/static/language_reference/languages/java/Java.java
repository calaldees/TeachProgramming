/*
Java  // VER: title
https://www.oracle.com/uk/java/technologies/javase-downloads.html  // VER: download
Java SE (Standard Edition) JDK (Java Development Kit)                       // VER: download
http://java.sun.com/docs/books/tutorial/                                    // VER: help
https://howtodoinjava.com/                                                  // VER: help
https://docs.oracle.com/en/java/javase/15/docs/api/overview-tree.html  // VER: help

javac HelloWorld.java && java HelloWorld                        # VER: run
// NOTE: filename and `public FILENAME {` must match name+case  # VER:run
*/

import java.util.Scanner; //Add at top of file                                  // VER: read_line_from_console

import java.io.BufferedReader; //Add at top of file                             // VER: file_read
import java.io.FileReader;                                                      // VER: file_read

import java.io.BufferedWriter; //Add at top of file                             // VER: file_write
import java.io.FileWriter;                                                      // VER: file_write
 
import java.util.List;    // VER: list_comprehension
import java.util.Arrays;  // VER: list_comprehension
import java.util.ArrayList;    // VER: list_comprehension

import java.util.stream.Collectors;   // VER: list_comprehension dict_comprehension
import java.util.Map;    // VER: dict_comprehension
import static java.util.Map.entry;   // VER: dict_comprehension

// TODO: this VER multiversion stuff is broken  ... I need some good tests and rewrite make_ver.py
// What a mess ...
/* poo double/ VER: list_comprehension dict_comprehension */  // WOW! this produces the output text  `poo  // dict_comprehension`


// //----------------------------- // VER: read_line_from_console file_read file_write list_comprehension dict_comprehension

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
    // // This is a comment                                                     // VER: comment
    ///* this is a multiline comment */                                         // VER: comment
  }

  void define_variables() {
    Integer count = 0;                                                          // VER: define_variables
    String username = "Betty";                                                  // VER: define_variables
    Double distance = 3.14;                                                     // VER: define_variables
    Boolean email_errors = true;                                                // VER: define_variables
    String multiline = """
    a 
    b
    """;  // TODO: multiline   // VER: define_variables
    System.out.println(count);
    System.out.println(username);
    System.out.println(distance);
    System.out.println(email_errors);
    System.out.println(multiline);
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
/*
//Get the file reference
Path path = Paths.get("c:/output.txt");
 
//Use try-with-resource to get auto-closeable writer instance
try (BufferedWriter writer = Files.newBufferedWriter(path)) 
{
    writer.write("Hello World !!");
}
*/
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
    Integer line_count = 0;                                                     // VER: file_read
    String line;                                                                // VER: file_read
    try {                                                                       // VER: file_read
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

  void sayHello() {  // VER: function
    System.out.println("Hello");  // VER: function
    System.out.println("Goodbye");  // VER: function
  }  // VER: function

  void function() {
    sayHello();      // VER: function
  }

  Integer biggest(Integer a, Integer b) {  // VER: function_with_return_value
    if (a > b) {   // VER: function_with_return_value
      return a;  // VER: function_with_return_value
    } // VER: function_with_return_value
    else { // VER: function_with_return_value
      return b; // VER: function_with_return_value
    } // VER: function_with_return_value
  }    // VER: function_with_return_value
  void function_with_return_value() {
    System.out.println(biggest(1,2));  // VER: function_with_return_value
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


  void string_concatenation() {
    String forename = "bob";
    String surname = "jones";
    String fullname = forename + " " + surname;                        // VER: string_concatenation
    String fullname2 = "%s %s".formatted(forename, surname);              // VER: string_concatenation
    String fullname3 = "{forename} {surname}".replace("{forename}", forename).replace("{surname}", surname);              // VER: string_concatenation
    System.out.println(fullname);
  }

  void split_strings() {
    final String csv_line_test = "Jane,09/09/1989,Female,Blue";  // VER: split_strings
    String[] line_split =  csv_line_test.split(",");  // VER: split_strings
    System.out.println(line_split[1]);
    String csv_line_test2 = String.join(" : ", line_split);         // VER: split_strings
    System.out.println(csv_line_test2);
  }

  void list_comprehension() {
    // int[] i = new int[]{1,2,3,4}; Arrays.stream(i).collect(toList());
    List<Integer> data1 = new ArrayList<>(Arrays.asList(1,2,3,4,5,6));          // VER: list_comprehension
    List<Integer> data2 = data1.stream(                                         // VER: list_comprehension
    ).filter(                                                                   // VER: list_comprehension
      (i) -> i >= 3                                                             // VER: list_comprehension
    ).map(                                                                      // VER: list_comprehension
      (i) -> i * 2                                                              // VER: list_comprehension
    ).collect(Collectors.toList());                                             // VER: list_comprehension

    System.out.println(data2);
  }

  void dict_comprehension() {
    Map<String,Integer> data3 = Map.ofEntries(                                  //  VER: dict_comprehension
      entry("a", 1),                                                            //  VER: dict_comprehension
      entry("b", 2),                                                            //  VER: dict_comprehension
      entry("c", 3)                                                             //  VER: dict_comprehension
    );                                                                          //  VER: dict_comprehension
    Map<Integer, String> data4 = data3.entrySet().stream(                       //  VER: dict_comprehension
    ).filter(                                                                   //  VER: dict_comprehension
      (e) -> e.getValue() >= 2                                                  //  VER: dict_comprehension
    ).map(                                                                      //  VER: dict_comprehension
      (e) -> entry(e.getValue() + 10, e.getKey())                               //  VER: dict_comprehension
    ).collect(Collectors.toMap((e)->e.getKey(), (e)->e.getValue()));            //  VER: dict_comprehension

    System.out.println(data4);
  }

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
    file_write();
    file_read();
    function();
    function_with_return_value();
    list_comprehension();
    dict_comprehension();
  }

}

/*

https://howtodoinjava.com/java-8-tutorial/

TODO: streams and lambda

https://howtodoinjava.com/java8/java-streams-by-examples/

Optional<Integer> possible = Optional.of(5); 
possible.ifPresent(System.out::println);


Optional<Company> companyOptional = Optional.empty();
companyOptional.filter(department -> "Finance".equals(department.getName())
                    .ifPresent(() -> System.out.println("Finance is present"));

// default methods in interfaces
public interface Moveable {
    default void move(){
        System.out.println("I am moving");
    }
}


import java.util.ArrayList;
import java.util.List;
 
public class Animal implements Moveable{
    public static void main(String[] args){
        List<Animal> list = new ArrayList();
        list.add(new Animal());
        list.add(new Animal());
        list.add(new Animal());
         
        //Iterator code reduced to one line
        list.forEach((Moveable p) -> p.move());
    }
}


List<Integer> integers = Arrays.asList(1,12,433,5);
Optional<Integer> max = integers.stream().reduce( Math::max );
max.ifPresent( System.out::println ); 
max.ifPresent(value -> System.out.println(value)); 


List<String> strings = Arrays
        .asList("how", "to", "do", "in", "java", "dot", "com");
 
List<String> sorted = strings
        .stream()
        .sorted((s1, s2) -> s1.compareTo(s2))
        .collect(Collectors.toList());
 
System.out.println(sorted);
 
List<String> sortedAlt = strings
        .stream()
        .sorted(String::compareTo)
        .collect(Collectors.toList());
 
System.out.println(sortedAlt);




List<Integer> integers = IntStream
                .range(1, 100)
                .boxed()
                .collect(Collectors.toCollection( ArrayList::new ));
 
Optional<Integer> max = integers.stream().reduce(Math::max); 
 
max.ifPresent(System.out::println); 





new Thread(new Runnable() {
    @Override
    public void run() {
        System.out.println("howtodoinjava");
    }
}).start();

If we use the lambda expression for this task then code will be :
new Thread(
    () ->   { 
              System.out.println("My Runnable"); 
            }
    ).start();



memberNames.stream().filter((s) -> s.startsWith("A"))
                    .map(String::toUpperCase)
                    .forEach(System.out::println);  



https://howtodoinjava.com/java8/stream-map-vs-flatmap/
flatmap is python chain


List<Integer> randomNumbers = Stream.generate(() -> (new Random()).nextInt(100))
                                    .limit(10)
                                    .collect(Collectors.toList());



 .takeWhile(s -> !s.equals("d"))



immutable map
        Map<String, String> names = Map.ofEntries(
                Map.entry("1", "Lokesh"),
                Map.entry("2", "Amit"),
                Map.entry("3", "Brian"));

var j = 10;

    String transformedName = name.transform(String::strip)
                                .transform(StringUtils::toCamelCase);


if (obj instanceof String s) {
    // can use s here
} else {
    // can't use s here
}



public record EmployeeRecord(Long id, 
        String firstName, 
        String lastName, 
        String email, 
        int age) {
     
}
public class RecordExample {
    public static void main(String[] args) 
    {
        EmployeeRecord e1 = new EmployeeRecord
                (1l, "Lokesh", "Gupta", "howtodoinjava@gmail.com", 38);
         
        System.out.println(e1.id());
        System.out.println(e1.email());
         
        System.out.println(e1);
    }
}


String dbSchema =   """
            CREATE TABLE 'TEST'.'EMPLOYEE'
            (
              'ID' INT NOT NULL DEFAULT 0 ,
              'FIRST_NAME' VARCHAR(100) NOT NULL ,
              'LAST_NAME' VARCHAR(100) NULL ,
              'STAT_CD' TINYINT NOT NULL DEFAULT 0
            );
                    """;


*/