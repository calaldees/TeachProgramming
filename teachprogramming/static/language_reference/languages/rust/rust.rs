fn main() {
    hello_world();
    comment();
    define_constants();
    arithmetic();
}

//fn main() {                   // VER: hello_world
fn hello_world() {
    println!("Hello World");    // VER: hello_world
}                               // VER: hello_world


fn comment() {
    ////This is a comment  // VER: comment
}

fn define_constants() {
    let gravity = 9.81;  // VER: define_constants
    let count = 0;            // VER: define_constants
    let username = "Betty";   // VER: define_constants
    let email_errors = true;      // VER: define_constants
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

/*
fn if_statement() {
  let username = 'bob'
  let count = 3

  if count >= 5 and username == "Jim":  // VER: if_statement
    print("Yes")                      // VER: if_statement
  elif username == "admin" or username == "Bob":  // VER: if_statement
    print("Admin")                    // VER: if_statement
  else:                                 // VER: if_statement
    print("No")                       // VER: if_statement
}
*/