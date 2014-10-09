/*
Javascript      // VER: title
*/

console = {log: print};

//------------------------------------------------------------------------------

function hello_world() {
    console.log("Hello World");     // VER: hello_world
}

function read_line_from_console() {
    
}

function comment() {
    // This is a comment    // VER: comment
    /* So is this */        // VER: comment
}

function define_variables() {
    var count = 0;              // VER: define_variables
    var username = "Betty";     // VER: define_variables
    var distance = 3.14;        // VER: define_variables
    var email_errors = true;    // VER: define_variables    
}

function define_constats() {
    var GRAVITY = 9.81  // VER: define_constants
}

function arithmetic() {
    var xpos = 0;
    var item_price = 0;
    var quat = 0;
    var count = 0; 

    xpos = xpos + 1;                 // VER: arithmetic
    distance = 3 / 4;                // VER: arithmetic
    total_cost = item_price * quant; // VER: arithmetic
    remainder = 14 % 11;             // VER: arithmetic
    count += 1;                      // VER: arithmetic
}

function if_statement() {
    var username = 'bob';
    var count = 3;

    if (count >= 5 && username == "Jim") {  // VER: if_statement
        console.log("Yes");                 // VER: if_statement
    }                                       // VER: if_statement
    else if (username == "admin") {         // VER: if_statement
        console.log("Admin");               // VER: if_statement
    }                                       // VER: if_statement
    else {                                  // VER: if_statement
        console.log("No");                  // VER: if_statement
    }
}

function if_statement_more() {
    
}

function for_loop() {
    var username = 'bob';                           // VER: for_loop
    for (var i = 0 ; i < username.length ; i++) {   // VER: for_loop
        console.log(username[i]);                   // VER: for_loop
    }                                               // VER: for_loop
}

function while_loop() {
    var count = 0;                          // VER: while_loop
    while (count < 10) {                    // VER: while_loop
        console.log("Count is " + count);   // VER: while_loop
        count = count + 2;                  // VER: while_loop
    }
}

function until_loop() {
}

function for_each_loop() {
    names = ["Bob", "Ben", "Bill", "Borris", "Bin"];    // VER: for_each_loop
    for (var i in names) {                              // VER: for_each_loop
        var name = names[i];                            // VER: for_each_loop
        console.log(name);                              // VER: for_each_loop
    }                                                   // VER: for_each_loop
}

function file_write() {
    
}

function file_read() {
    
}

function string_concatination() {
    
}

function convert_string_to_interger_and_back() {
    
}

function convert_double_to_string_and_back() {
    
}

function _function() {
    
}

function function_with_return_value() {
    
}

function function_with_params_by_reference() {
    
}

function function_with_params_by_value() {
    
}

function define_fixed_array() {
    
}

function define_2d_arrays() {
    
}

function linked_list() {
    
}

function define_map() {
    
}

function error_handling() {
    
}

function split_strings() {
    
}

function random_number() {
    
}

function _switch() {
    
}

function _class() {
    
}

function read_csv_into_array_of_classs() {
    
}

function _sleep() {
    
}

//------------------------------------------------------------------------------

var functions = ["hello_world", "test"];

for (var i in functions) {
    var function_name = functions[i];
    console.log("-"+function_name+"-");
    try {
        this[function_name]();
    } catch(e) {
        console.log(e);
    }
}