fn main() {
  hello_world();
  comment();
  define_constants();
  arithmetic();
  if_statement();
  define_fixed_array();
  define_list();
}

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
  //multiline = """a b"""    // TODO
}

fn arithmetic() {
  let item_price = 0;
  let quant = 0;

  let mut xpos = 0;  // VER: arithmetic
  xpos = xpos + 1;                  // VER: arithmetic
  let distance = 3 / 4;                 // VER: arithmetic
  let total_cost = item_price * quant;  // VER: arithmetic
  let remainder = 14 % 11;              // VER: arithmetic
  let mut count = 0;                 // VER: define_variables
  count += 1;                       // VER: arithmetic

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
  //if bb.find("a") {                  // VER: define_fixed_array
  //  println!("a exists in array")    // VER: define_fixed_array
  //}                                  // VER: define_fixed_array
}


fn define_list() {
  let mut cc = vec!["a", "b", "c"]; // VER: define_list
  println!("{:?}", cc);         // VER: define_list
  println!("{}", cc[0]);        // VER: define_list
  let last = cc.pop();          // VER: define_list
  cc.push("d");                 // VER: define_list
  let first = cc.remove(0);     // VER: define_list
  cc.insert(0, "z");            // VER: define_list
  //cc.remove("b")              // VER: define_list
  for i in cc.iter() {          // VER: define_list
    println!("{}", i); // 'z' 'd' // VER: define_list
  }                             // VER: define_list
  //if "z" in cc:               // VER: define_list
  //  print("z exists in list") // VER: define_list
}