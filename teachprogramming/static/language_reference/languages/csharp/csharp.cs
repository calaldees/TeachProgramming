/*
C#                                                                              // VER: title

Visual Studio Comunity                                                          // VER: download
https://visualstudio.microsoft.com/downloads/                                   // VER: download

https://docs.microsoft.com/en-us/dotnet/csharp/                                 // VER: help
https://www.tutorialspoint.com/csharp/index.htm                                 // VER: help

# TODO: install mono                                                            // VER: run
function csharp {     # linux bash function                                     // VER: run
  mcs "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe";                  // VER: run
}                                                                               // VER: run


*/

using System;                                                                   // VER: hello_world
using System.IO;                                                                // VER: file_write
using System.Collections.Generic;                                               // VER: define_map
using System.Linq;                                                              // VER: list_comprehension
//using System.Text.Json;  // TODO see json_data

public class Star { // VER: class
    public int x; // VER: class
    public int y; // VER: class
    public int speed; // VER: class
} // VER: class

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
    string multiline = $@"a b";                                                 // VER: define_variables
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
    int[] data = new int[]{5,6,7};                                              // VER: for_loop
    for (int i=0 ; i < data.Length ; i++) {                                     // VER: for_loop
      Console.WriteLine(data[i]);                                               // VER: for_loop
    }                                                                           // VER: for_loop
  }

  void while_loop() {
    int count = 0;  // VER: while_loop
    while (count < 10) {  // VER: while_loop
      Console.WriteLine("Count is " + count);  // VER: while_loop
      count = count + 2;  // VER: while_loop
    }  // VER: while_loop
  }

  void until_loop() { // VER: until_loop
    string word = "gibber"; // VER: until_loop
    do { // VER: until_loop
      word = word + word; // VER: until_loop
    } while (word.Length < 10); // VER: until_loop
    Console.WriteLine(word); // VER: until_loop
  } // VER: until_loop

  void for_each_loop() {
    string[] ff = new string[]{"a","b","c"}; // VER: for_each_loop
    foreach (string f in ff) {  // VER: for_each_loop
      Console.WriteLine(f);  // VER: for_each_loop
    }  // VER: for_each_loop
  }


  void until_loop() {
    int count = 0;                             // VER: until_loop
    do {                                       // VER: until_loop
      Console.WriteLine("Count is " + count);  // VER: until_loop
      count = count + 2;                       // VER: until_loop
    } while(count < 10);                       // VER: until_loop
  }


  void file_write() {
    string line_to_write = "Append to end of file"; // VER: file_write
    try { // VER: file_write
      using (StreamWriter file = new StreamWriter("out.txt")) {  // VER: file_write
        file.WriteLine(line_to_write);   // VER: file_write
      } // VER: file_write
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

  void error_handling() {                        // VER: error_handling
    try {                                        // VER: error_handling
      // thing that may error                    // VER: error_handling
    }                                            // VER: error_handling
    catch{                                       // VER: error_handling
      // what to do if things go wrong           // VER: error_handling
    }                                            // VER: error_handling
  }                                              // VER: error_handling

  void string_concatenation() {
    string forename = "bob";
    string surname = "jones";
    string fullname = $"{forename} {surname}";                                         // VER: string_concatenation
    string fullname2 = forename + " " + surname;                                       // VER: string_concatenation
    // // TODO: other formatting                                                // VER: string_concatenation
    Console.WriteLine(fullname);

  }
  void split_strings() {
    string csv_line_test = "Jane,09/09/1989,Female,Blue";                       // VER: split_strings
    string[] line_split = csv_line_test.Split(",");                             // VER: split_strings
    Console.WriteLine(line_split[1]);
    string csv_line_test2 = String.Join(" : ", line_split);                            // VER: split_strings
  }
  void string_compare() {
    // // TODO: string_compare  // VER: string_compare
  }
  void convert_string_to_integer_and_back() {
    // // TODO: // VER: convert_string_to_integer_and_back
  }


  void sayHello() {        // VER: function
      Console.WriteLine("Hello");      // VER: function
      Console.WriteLine("Goodbye");    // VER: function
  }    // VER: function
  void function() {
    sayHello();    // VER: function
  }


  int biggest(int a, int b) {      // VER: function_with_return_value
        if (a > b) {           // VER: function_with_return_value
            return a;        // VER: function_with_return_value
        }  // VER: function_with_return_value
        else {               // VER: function_with_return_value
            return b;        // VER: function_with_return_value
        }  // VER: function_with_return_value
  } // VER: function_with_return_value
  void function_with_return_value() {
    Console.WriteLine(biggest(1, 2));    // VER: function_with_return_value
  }

  void define_fixed_array() {
    var aa = new string[3];  // VER: define_fixed_array
    aa[1] = "test";  // VER: define_fixed_array
    Console.WriteLine(String.Join(",",aa));  // VER: define_fixed_array
    Console.WriteLine(aa[1]);  // VER: define_fixed_array
         // VER: define_fixed_array
    var bb = new string[]{"a", "b", "c"};  // VER: define_fixed_array
    Console.WriteLine("bb size is "+bb.Length);  // VER: define_fixed_array
    foreach (var i in bb) {  // VER: define_fixed_array
      Console.WriteLine(i);  // VER: define_fixed_array
    }  // VER: define_fixed_array
    if (Array.IndexOf(bb, "a") >= 0) {  // VER: define_fixed_array
      Console.WriteLine("a exists in array");  // VER: define_fixed_array
    }  // VER: define_fixed_array

    // TODO:
    // indexOf and join
  }

  void define_map() {
    var data = new Dictionary<string, int>(){   // VER: define_map
      {"a", 1},  // VER: define_map
      {"b", 2},  // VER: define_map
    };  // VER: define_map
    Console.WriteLine(data["b"]);  // prints 2   // VER: define_map
    data.Add("c", 3);  // VER: define_map
    data.Remove("a");  // VER: define_map
    foreach (var kv in data) {  // VER: define_map
      Console.WriteLine($"Key: {kv.Key}, Value: {kv.Value}");  // VER: define_map
    }  // VER: define_map
    if (data.ContainsKey("d")) {}  // VER: define_map

    // https://www.tutorialsteacher.com/csharp/csharp-dictionary

  }

  void sleep() {
    System.Threading.Thread.Sleep(1000);
  }

  void random_number() {
      Random random = new Random();   // VER: random_number
      int new_num = random.Next(0, 100);  // VER: random_number
      double new_fraction = random.NextDouble();     // VER: random_number

  }

  void _class() {
    Star s = new Star();    // VER: class
    s.x = 100;              // VER: class
    Console.WriteLine(s.x); // VER: class
  }

  void define_list() {
    var cc = new List<string>(new string[]{"a", "b", "c"});   // VER: define_list
    Console.WriteLine(cc[0]);   // VER: define_list
    string last = cc[cc.Count-1]; cc.RemoveAt(cc.Count-1);   // VER: define_list
    cc.Add("d");   // VER: define_list
    string first = cc[0]; cc.RemoveAt(0);   // VER: define_list
    cc.Insert(0, "z");   // VER: define_list
    cc.Remove("b");   // VER: define_list
    foreach (var i in cc) {   // VER: define_list
      Console.WriteLine(i);  // z d // VER: define_list
    }   // VER: define_list
    if (cc.Contains("z")) {                  // VER: define_list
      Console.WriteLine("z exists in list");  // VER: define_list
    } // VER: define_list
    // TODO: concat lists
  }

  void define_set() {
    var aa = new HashSet<int>(){1,2,3};  // VER: define_set
    var bb = new HashSet<int>(){2,3,4};  // VER: define_set
    var cc = new HashSet<int>(){1,2};  // VER: define_set
    HashSet<int> xx;  // VER: define_set
                        // VER: define_set
    xx = new HashSet<int>(aa);  // VER: define_set
    xx.UnionWith(bb);  // VER: define_set
    Console.WriteLine(String.Join(",",xx));  // VER: define_set
                            // VER: define_set
    xx = new HashSet<int>(aa);   // VER: define_set
    xx.IntersectWith(bb);         // VER: define_set
    Console.WriteLine(String.Join(",",xx));   // VER: define_set
                                   // VER: define_set
    xx = new HashSet<int>(aa);   // VER: define_set
    xx.ExceptWith(cc);         // VER: define_set
    Console.WriteLine(String.Join(",",xx));   // VER: define_set
                                   // VER: define_set
    Console.WriteLine(cc.IsSubsetOf(aa));   // VER: define_set
    xx.Add(5);   // VER: define_set
  }

  public delegate int MyFunction(int a, int b);    // VER: function_with_param_function
  void function_with_param_function() {
    MyFunction my_func_1 = (a, b) => a + b;    // VER: function_with_param_function
    MyFunction my_func_2 = delegate(int a, int b) {    // VER: function_with_param_function
      return a * b;    // VER: function_with_param_function
    };    // VER: function_with_param_function
    Action<MyFunction> print_my_func = (ff) => {  // VER: function_with_param_function
        Console.WriteLine(ff(2,3));  // VER: function_with_param_function
    };  // VER: function_with_param_function
    print_my_func(my_func_1);  // VER: function_with_param_function
    print_my_func(my_func_2);  // VER: function_with_param_function
  }


  // Mono did not support records or readonly structs
  //public record DailyTemperature(double HighTemp, double LowTemp) {}
  public struct Point {
    public int x;
    public int y;
  }
  public struct Dimension {    // VER: define_2d_arrays_with_1d_array_with_lookup_function
    public Dimension(int width, int height) {// VER: define_2d_arrays_with_1d_array_with_lookup_function
      this.width = width; this.height=height;// VER: define_2d_arrays_with_1d_array_with_lookup_function
    } // VER: define_2d_arrays_with_1d_array_with_lookup_function
    public int width {get;}    // VER: define_2d_arrays_with_1d_array_with_lookup_function
    public int height {get;}    // VER: define_2d_arrays_with_1d_array_with_lookup_function
    public int size {get {return width * height;}}    // VER: define_2d_arrays_with_1d_array_with_lookup_function
    public int coord_to_index(int x, int y) {// VER: define_2d_arrays_with_1d_array_with_lookup_function
      return (y * width) + (x % width);// VER: define_2d_arrays_with_1d_array_with_lookup_function
    }    // VER: define_2d_arrays_with_1d_array_with_lookup_function
    // ??? index_to_coord(Integer i) {return new Point(i % width(), i / width());}
  }    // VER: define_2d_arrays_with_1d_array_with_lookup_function
  void define_2d_arrays() {
    int width = 3;
    int height = 3;
    int value = 1;

    var grid1 = new int[width,height];             // VER: define_2d_arrays_with_nested_arrays
    for (int y=0; y < grid1.GetLength(1) ; y++) {     // VER: define_2d_arrays_with_nested_arrays
      for (int x=0; x < grid1.GetLength(0) ; x++) {   // VER: define_2d_arrays_with_nested_arrays
        grid1[x, y] = value;                        // VER: define_2d_arrays_with_nested_arrays
      }                                               // VER: define_2d_arrays_with_nested_arrays
    }                                                 // VER: define_2d_arrays_with_nested_arrays
    grid1[2,1] = 5;                                  // VER: define_2d_arrays_with_nested_arrays
    Console.WriteLine(grid1[0,0]);                   // VER: define_2d_arrays_with_nested_arrays
            // VER: define_2d_arrays_with_nested_arrays

    Dimension d = new Dimension(width, height);         // VER: define_2d_arrays_with_1d_array_with_lookup_function
    var grid2 = new int[d.size];                      // VER: define_2d_arrays_with_1d_array_with_lookup_function
    Array.Fill(grid2, value);                           // VER: define_2d_arrays_with_1d_array_with_lookup_function
    grid2[d.coord_to_index(2, 1)] = 5;                  // VER: define_2d_arrays_with_1d_array_with_lookup_function
    Console.WriteLine(grid2[d.coord_to_index(0,0)]);    // VER: define_2d_arrays_with_1d_array_with_lookup_function

    var grid3 = new Dictionary<Tuple<int, int>, int>(); // VER: define_2d_arrays_with_dictionary
    for (int y=0 ; y<height ; y++) {                // VER: define_2d_arrays_with_dictionary
      for (int x=0 ; x<width ; x++) {               // VER: define_2d_arrays_with_dictionary
        grid3.Add(new Tuple<int,int>(x,y), value);               // VER: define_2d_arrays_with_dictionary
      }    // VER: define_2d_arrays_with_dictionary
    }    // VER: define_2d_arrays_with_dictionary
    grid3[new Tuple<int,int>(2,1)] = 5;    // VER: define_2d_arrays_with_dictionary
    Console.WriteLine(grid3[new Tuple<int,int>(0,0)]);    // VER: define_2d_arrays_with_dictionary

  }

  void list_comprehension() {
    var data1 = new List<int>(new int[]{1,2,3,4,5,6});                           // VER: list_comprehension
    var data2 = data1                                                         // VER: list_comprehension
      .Where(                                                                // VER: list_comprehension
        (i) => i >= 3                                                     // VER: list_comprehension
      ).Select(                                                                  // VER: list_comprehension
        (i) => i * 2                                                      // VER: list_comprehension
      );                                                                      // VER: list_comprehension
      Console.WriteLine(String.Join(",",data2));
  }

  void dict_comprehension() {
    var data3 = new Dictionary<string, int>(){   // VER: dict_comprehension
      {"a", 1},  // VER: dict_comprehension
      {"b", 2},  // VER: dict_comprehension
      {"c", 3},  // VER: dict_comprehension
    };  // VER: dict_comprehension
    var data4 = data3  // VER: dict_comprehension
      .Where((kv) => kv.Value >= 2)  // VER: dict_comprehension
      .ToDictionary(  // VER: dict_comprehension
        (kv) => kv.Value + 10,  // VER: dict_comprehension
        (kv) => kv.Key  // VER: dict_comprehension
      )  // VER: dict_comprehension
    ;  // VER: dict_comprehension
    Console.WriteLine(String.Join(",",data4));
  }


  void json_data() {
    // using System.Text.Json;                                                  // VER: json_data
    // https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=net-5.0
    // https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-how-to?pivots=dotnet-5-0
    // https://stackoverflow.com/a/58495751/3356840
    // https://marcroussy.com/2020/08/17/deserialization-with-system-text-json/
    // TODO: WARNING!! this string inline needs investigating
    var stringifiedJson = @"{                           // VER: json_data
      ""Topic"":""Json Serialization Part 1"",          // VER: json_data
      ""Part"":1,                                       // VER: json_data
      ""Author"":""Marc"",                              // VER: json_data
      ""Co-Author"":""Helen"",                          // VER: json_data
      ""Keywords"":[""json"",""netcore"",""parsing""]   // VER: json_data
    }";                                                 // VER: json_data
    /*
    var blogPost = JsonDocument.Parse(stringifiedJson);  // VER: json_data
    var topic = blogPost.RootElement.GetProperty("Topic").GetString();  // VER: json_data
    Console.WriteLine(topic);  // VER: json_data
    */

    // Can deserialise into data object type      // VER: json_data
    // var personObject = JsonSerializer.Deserialize<Person>(jsonPerson);    // VER: json_data
  }

  static void sort() {
    // sort reverse with custom comparator
    // TODO:
    // https://stackoverflow.com/questions/15494463/how-can-i-do-an-inline-sort
    // (a, b) => String.Compare(a.Name, b.Name)
    // Consider "Key" to be inline with python?
    string[] data = {"b", "d", "c", "a"};       // VER: sort
    Array.Sort(data);                           // VER: sort
    Console.WriteLine(String.Join(",", data));  // VER: sort
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
      string_concatenation();
      split_strings();
      string_compare();
      function();
      function_with_return_value();
      sleep();
      define_fixed_array();
      define_list();
      define_map();
      define_set();
      function_with_param_function();
      define_2d_arrays();
      list_comprehension();
      dict_comprehension();
      json_data();
      sort();
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





https://www.tutorialsteacher.com/csharp/csharp-delegates

public delegate void MyDelegate(string msg); // declare a delegate

// set target method
MyDelegate del = new MyDelegate(MethodA);
// or
MyDelegate del = MethodA;
// or set lambda expression
MyDelegate del = (string msg) =>  Console.WriteLine(msg);

// target method
static void MethodA(string message)
{
    Console.WriteLine(message);
}


*/
