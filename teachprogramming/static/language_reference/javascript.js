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
    var forename = 'bob';
    var surname = 'jones';
    fullname = forename + " " + surname;    // VER: string_concatination
    console.log(fullname);
}

function convert_string_to_interger_and_back() {
    var sum = 5 + parseInt('5');    // VER: conert_string_to_interger_and_back
    console.log(String(sum))        // VER: conert_string_to_interger_and_back
}

function convert_double_to_string_and_back() {
    var f = parseFloat("3.1415");   // VER: convert_double_to_string_and_back
    console.log(String(f));         // VER: convert_double_to_string_and_back
}

function _function() {
    function sayHello() {           // VER: function
        console.log("Hello");       // VER: function
        console.log("Goodbye");     // VER: function
    }                               // VER: function
    sayHello();                     // VER: function
}

function function_with_return_value() {
    function biggest(a, b) {    // VER: function_with_return_value
        if (a > b) {            // VER: function_with_return_value
            return a;           // VER: function_with_return_value
        }                       // VER: function_with_return_value
        else {                  // VER: function_with_return_value
            return b;           // VER: function_with_return_value
        }                       // VER: function_with_return_value
    }                           // VER: function_with_return_value
    console.log(biggest(1, 2)); // VER: function_with_return_value
}

function function_with_params_by_reference() {
    
}

function function_with_params_by_value() {
    
}

function define_fixed_array() {
    var names = Array(3);       // VER: define_fixed_array
    names[0] = "Bob";           // VER: define_fixed_array
    names[1] = "Foo";           // VER: define_fixed_array
    names[2] = "Rah";           // VER: define_fixed_array
    for (var i in names) {      // VER: define_fixed_array
        var name = names[i];    // VER: define_fixed_array
        console.log(name);      // VER: define_fixed_array
    }                           // VER: define_fixed_array
    console.log("array size is " + names.length) // VER: define_fixed_array
}

function define_2d_arrays() {
    //var grid = Array(10,10)  // VER: define_2d_arrays
    //grid(5,5) = 1               // VER: define_2d_arrays
}

function linked_list() {
    var list = [];                              // VER: linked_list
    list.push("Bill")                           // VER: linked_list
    list.push("Ben")                            // VER: linked_list
    list.push("Bob")                            // VER: linked_list
    list.pop("Ben")                             // VER: linked_list
    list.pop()                                  // VER: linked_list
    list.unshift("Kim")                         // VER: linked_list
    for (var i in list) {                       // VER: linked_list
        var name = list[i];                     // VER: linked_list
        console.log(name);                      // VER: linked_list
    }                                           // VER: linked_list
    console.log("list size is " + list.length)  // VER: linked_list
}

function define_map() {
    var dict = {};
    dict["Joe"] = 77;
    dict["Jane"] = 51;
    for (var key in dict) {
        var value = dict[key];
        console.log("Key: " + key + " Value: " + value);
    }    
}

function error_handling() {
    try {                                   // VER: error_handling
        // thing that may error             // VER: error_handling
    } catch(e) {                            // VER: error_handling
        // what to do if things go wrong    // VER: error_handling
    }                                       // VER: error_handling
}

function split_strings() {
    var csv_line_test = "Jane,09/09/1989,Female,Blue"   // VER: split_strings
    var line_split = csv_line_test.split(",");          // VER: split_strings
    console.log(line_split[1]);
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

var functions = read("_function_order.txt", "text").split("\n");

for (var i in functions) {
    var function_name = functions[i];
    console.log("-"+function_name+"-");
    try {
        this[function_name]();
    } catch(e) {
        console.log(e);
    }
}