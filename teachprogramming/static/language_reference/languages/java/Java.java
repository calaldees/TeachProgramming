/*
Java 15  // VER: title
https://www.oracle.com/uk/java/technologies/javase-downloads.html  // VER: download
Java SE (Standard Edition) JDK (Java Development Kit)                       // VER: download
http://java.sun.com/docs/books/tutorial/                                    // VER: help
https://howtodoinjava.com/                                                  // VER: help
https://docs.oracle.com/javase/                                             // VER: help

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
import java.util.HashMap;    // VER: define_map
import static java.util.Map.entry;   // VER: dict_comprehension

import java.util.Set;    // VER: define_set
import java.util.HashSet;    // VER: define_set


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

  void define_map() {
    Map<String,Integer> data = new HashMap<>(Map.ofEntries(                                  // VER: define_map
      entry("a", 1),                                                            // VER: define_map
      entry("b", 2)                                                            // VER: define_map
    ));                                                                          // VER: define_map
    System.out.println(data.get("b"));  // prints 2   // VER: define_map
    data.put("c", 3);  // VER: define_map
    data.remove("a");  // VER: define_map
    for (var key_value_pair : data.entrySet()){  // VER: define_map
      System.out.println("Key: %s, Value: %s".formatted(key_value_pair.getKey(), key_value_pair.getValue()));  // VER: define_map
    }  // VER: define_map
    if (data.containsKey("d")) {}  // VER: define_map
  }

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
    List<Integer> data1 = new ArrayList<>(Arrays.asList(new Integer[]{1,2,3,4,5,6}));          // VER: list_comprehension
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


  void define_2d_arrays() {
    Integer width = 3;   // VER: define_2d_arrays
    Integer height = 3;   // VER: define_2d_arrays
    Integer value = 1;  // VER: define_2d_arrays
                          // VER: define_2d_arrays
    Integer[][] grid1 = new Integer[width][height];   // VER: define_2d_arrays
    for (var row: grid1) {Arrays.fill(row, value);}   // VER: define_2d_arrays
    grid1[2][1] = 5;                                  // VER: define_2d_arrays
    System.out.println(grid1[0][0]);                 // VER: define_2d_arrays
                                                      // VER: define_2d_arrays
    record Point(Integer x, Integer y) {}                 // VER: define_2d_arrays
    record Dimension(Integer width, Integer height) {                 // VER: define_2d_arrays
      Integer size() {return width() * height();}                 // VER: define_2d_arrays
      Integer coord_to_index(Point p) {return coord_to_index(p.x(), p.y());}                // VER: define_2d_arrays
      Integer coord_to_index(Integer x, Integer y) {return (y * width()) + (x % width());}  // VER: define_2d_arrays
      Point index_to_coord(Integer i) {return new Point(i % width(), i / width());}         // VER: define_2d_arrays
    }                 // VER: define_2d_arrays
                                                           // VER: define_2d_arrays
    Dimension d = new Dimension(width, height);                 // VER: define_2d_arrays
    Integer[] grid2 = new Integer[d.size()];                 // VER: define_2d_arrays
    Arrays.fill(grid2, value);                 // VER: define_2d_arrays
    grid2[d.coord_to_index(2, 1)] = 5;                 // VER: define_2d_arrays
    System.out.println(grid2[d.coord_to_index(0,0)]);                 // VER: define_2d_arrays
                                                           // VER: define_2d_arrays
    Map<Point,Integer> grid3 = new HashMap<>();                 // VER: define_2d_arrays
    for (Integer y=0 ; y<height ; y++) {                 // VER: define_2d_arrays
      for (Integer x=0 ; x<width ; x++) {                 // VER: define_2d_arrays
        grid3.put(new Point(x,y), value);                 // VER: define_2d_arrays
      }                 // VER: define_2d_arrays
    }                 // VER: define_2d_arrays
    grid3.put(new Point(2,1), 5);                 // VER: define_2d_arrays
    System.out.println(grid3.get(new Point(0,0)));                 // VER: define_2d_arrays
  }

  void define_set() {
    Set<Integer> aa = Set.of(new Integer[]{1,2,3});  // VER: define_set
    Set<Integer> bb = Set.of(new Integer[]{2,3,4});  // VER: define_set
    Set<Integer> cc = Set.of(new Integer[]{1,2});  // VER: define_set
    Set<Integer> xx = null;   // VER: define_set
                              // VER: define_set
    xx = new HashSet<>(aa);   // VER: define_set
    xx.addAll(bb);            // VER: define_set
    System.out.println(xx);   // VER: define_set
                              // VER: define_set
    xx = new HashSet<>(aa);   // VER: define_set
    xx.retainAll(bb);         // VER: define_set
    System.out.println(xx);   // VER: define_set
                              // VER: define_set
    xx = new HashSet<>(aa);   // VER: define_set
    xx.removeAll(cc);         // VER: define_set
    System.out.println(xx);   // VER: define_set
                              // VER: define_set
    System.out.println(aa.containsAll(cc));    // VER: define_set
    xx.add(5);  // VER: define_set
  }

  void function_with_param_function() {
    interface MyFunction {  // VER: function_with_param_function
      Integer my_func(Integer a, Integer b); // VER: function_with_param_function
    }  // VER: function_with_param_function
    MyFunction my_func_1 = (Integer a, Integer b) -> a + b;  // VER: function_with_param_function
    MyFunction my_func_2 = new MyFunction() {  // VER: function_with_param_function
      public Integer my_func(Integer a, Integer b) {  // VER: function_with_param_function
        return a * b;  // VER: function_with_param_function
      } // VER: function_with_param_function
    };  // VER: function_with_param_function
    var mm = new Object(){  // VER: function_with_param_function
      void print_my_func(MyFunction ff) {  // VER: function_with_param_function
        System.out.println(ff.my_func(2,3));  // VER: function_with_param_function
      }  // VER: function_with_param_function
    };  // VER: function_with_param_function
    mm.print_my_func(my_func_1);  // VER: function_with_param_function
    mm.print_my_func(my_func_2);  // VER: function_with_param_function
  }


/*


    class Array2D<T> {
      public final T[] data;
      public final Dimension d;
      Array2D(Dimension dimension, T[] data) {
        this.d = dimension;
        this.data = data;
      }
      Array2D(Dimension dimension, T value) {
        this(dimension, (T[])new Object[width * height]);  //this.data = new T[width * height];
        Arrays.fill(this.data, value);
      }


      T get(Point p) {
        return this.data[this.coord_to_index(p)];
      }
    }
*/


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
    define_map();
    define_set();
    function_with_param_function();
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