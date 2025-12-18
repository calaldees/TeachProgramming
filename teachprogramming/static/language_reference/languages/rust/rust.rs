use std::collections::HashMap;  // VER: define_map
use std::collections::HashSet;  // VER: define_set


//fn main() {               // VER: hello_world
fn hello_world() {
  println!("Hello World");  // VER: hello_world
}                           // VER: hello_world

fn comment() {
  ////This is a comment  // VER: comment
  /* So is this */       // VER: comment
}

const THRESHOLD: i32 = 10;  // VER: define_constants
fn define_constants() {
  let gravity = 9.81;       // VER: define_constants
  let count = 0;            // VER: define_constants
  let username = "Betty";   // VER: define_constants
  let email_errors = true;  // VER: define_constants
  let multiline = r###"a b"###;  // VER: define_constants
}

fn arithmetic() {
  let item_price = 0;
  let quant = 0;

  let mut xpos = 0;                    // VER: arithmetic
  xpos = xpos + 1;                     // VER: arithmetic
  let distance = 3 / 4;                // VER: arithmetic
  let total_cost = item_price * quant; // VER: arithmetic
  let remainder = 14 % 11;             // VER: arithmetic
  let mut count = 0;                   // VER: define_variables
  count += 1;                          // VER: arithmetic

  println!("{}",xpos);
  println!("{}",distance);
  println!("{}",total_cost);
  println!("{}",remainder);
  println!("{}",count);
}


fn struct_example() {
  //struct Matrix(f32, f32, f32, f32);
}

fn if_statement() {
  let username = "bob";
  let count = 3;

  if count >= 5 && username == "Jim" {// VER: if_statement
    println!("Yes");                  // VER: if_statement
  }                                   // VER: if_statement
  else if username == "admin" || username == "Bob" {  // VER: if_statement
    println!("Admin");                // VER: if_statement
  }                                   // VER: if_statement
  else {                              // VER: if_statement
    println!("No");                   // VER: if_statement
  }                                   // VER: if_statement
}

fn for_loop() {
  let data = [5,6,7];        // VER: for_loop
  for i in 0..data.len() {   // VER: for_loop
    println!("{}", data[i]); // VER: for_loop
  }                          // VER: for_loop
}

fn while_loop() {
  let mut count = 0;  // VER: while_loop
  while count < 10 {  // VER: while_loop
    println!("Count is {}", count);  // VER: while_loop
    count = count + 2;  // VER: while_loop
  }  // VER: while_loop
}

fn for_each_loop() {
  let ff = ["a","b","c"]; // VER: for_each_loop
  for f in ff {           // VER: for_each_loop
    println!("{}", f);    // VER: for_each_loop
  }                       // VER: for_each_loop
}


fn sayHello() {         // VER: function
  println!("Hello");    // VER: function
  println!("Goodbye");  // VER: function
}                       // VER: function
fn function() {
  sayHello();           // VER: function
}

fn biggest(a: i32, b: i32) -> i32 {  // VER: function_with_return_value
  if a > b {   // VER: function_with_return_value
    return a;  // VER: function_with_return_value
  } // VER: function_with_return_value
  else { // VER: function_with_return_value
    return b; // VER: function_with_return_value
  } // VER: function_with_return_value
}    // VER: function_with_return_value
fn function_with_return_value() -> () {
  println!("{}", biggest(1,2));  // VER: function_with_return_value
}


fn define_fixed_array() {
  let mut aa: [&str; 3] = [""; 3];   // VER: define_fixed_array
  aa[1] = "test";                    // VER: define_fixed_array
  println!("{:?}", aa);              // VER: define_fixed_array
  println!("{}", aa[1]);             // VER: define_fixed_array
                                     // VER: define_fixed_array
  // vec!
  let bb = ["a", "b", "c"];            // VER: define_fixed_array
  println!("bb size is {}", bb.len()); // VER: define_fixed_array
  for i in bb.iter() {                 // VER: define_fixed_array
    println!("{}", i);                 // VER: define_fixed_array
  }                                    // VER: define_fixed_array
  if bb.iter().find(|&&x| x == "a").is_some() {  // VER: define_fixed_array
    println!("a exists in array")    // VER: define_fixed_array
  }  // VER: define_fixed_array
}


fn define_list() {
  let mut cc = vec!["a", "b", "c"]; // VER: define_list
  println!("{:?}", cc);         // VER: define_list
  println!("{}", cc[0]);        // VER: define_list
  let last = cc.pop();          // VER: define_list
  cc.push("d");                 // VER: define_list
  let first = cc.remove(0);     // VER: define_list
  cc.insert(0, "z");            // VER: define_list
  cc.retain(|&i| i != "b"); //slow! // VER: define_list
  for i in cc.iter() {          // VER: define_list
    println!("{}", i); // 'z' 'd' // VER: define_list
  }                             // VER: define_list
  if cc.into_iter().find(|&x| x == "z").is_some() { // VER: define_list
    println!("z exists in list");  // VER: define_list
  }                                // VER: define_list
}


fn define_map() {
  let mut data = HashMap::from([ // VER: define_map
    ("a", 1),                // VER: define_map
    ("b", 2),                // VER: define_map
  ]);                        // VER: define_map
  println!("{:?}", data.get("b")); // prints 2  // VER: define_map
  data.insert("c", 3);      // VER: define_map
  data.remove("a");         // VER: define_map
  for (k, v) in data.iter() {                   // VER: define_map
    println!("Key: {k}, Value: {v}", k=k, v=v); // VER: define_map
  }                                             // VER: define_map
  if data.contains_key("d") {  // VER: define_map
    println!("contains d");    // VER: define_map
  }                            // VER: define_map
}


fn string_concatenation() {
  let forename = "bob";
  let surname = "jones";
  let fullname = String::from(forename) + " " + surname; // VER: string_concatenation
  let fullname2 = format!("{} {}",forename, surname);  // VER: string_concatenation
  let fullname3 = "{forename} {surname}"               // VER: string_concatenation
    .replace("{forename}", forename)                   // VER: string_concatenation
    .replace("{surname}", surname);                    // VER: string_concatenation
  println!("{}", fullname);
}

fn split_strings() {
  let csv_line_test = "Jane,09/09/1989,Female,Blue";  // VER: split_strings
  let line_split = csv_line_test.split(',').collect::<Vec<_>>(); // VER: split_strings
  println!("{}", line_split[1]);                      // VER: split_strings
  let csv_line_test2 = line_split.join(" : ");        // VER: split_strings
  println!("{}", csv_line_test2);                     // VER: split_strings
}

fn dict_comprehension() {
  let data3 = HashMap::from([ //  VER: dict_comprehension
    ("a", 1),                 //  VER: dict_comprehension
    ("b", 2),                 //  VER: dict_comprehension
    ("c", 3),                 //  VER: dict_comprehension
  ]);                         //  VER: dict_comprehension
  let data4 = data3.iter()    //  VER: dict_comprehension
    .filter(|(&k,&v)| v>=2)   //  VER: dict_comprehension
    .map(|(&k,&v)| (v+10,k))  //  VER: dict_comprehension
    .collect::<HashMap<_,_>>();  //  VER: dict_comprehension
  println!("{:?}", data4);
}

fn define_set() {
  let mut aa: HashSet<_> = vec![1,2,3].into_iter().collect(); // VER: define_set
  let bb: HashSet<_> = vec![2,3,4].into_iter().collect();     // VER: define_set
  let cc: HashSet<_> = vec![1,2].into_iter().collect();       // VER: define_set
  println!("{:?}", aa.union(&bb).collect::<Vec<_>>());        // VER: define_set
  println!("{:?}", aa.intersection(&bb).collect::<Vec<_>>()); // VER: define_set
  println!("{:?}", aa.difference(&bb).collect::<Vec<_>>());   // VER: define_set
  println!("{:?}", cc.is_subset(&aa));                        // VER: define_set
  aa.insert(5);                                               // VER: define_set
}


fn main() {
  hello_world();
  comment();
  define_constants();
  arithmetic();
  if_statement();
  for_loop();
  while_loop();
  for_each_loop();
  function();
  function_with_return_value();
  define_fixed_array();
  define_list();
  define_map();
  string_concatenation();
  split_strings();
  dict_comprehension();
  define_set();
}