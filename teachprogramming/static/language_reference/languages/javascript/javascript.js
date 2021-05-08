/*
Javascript      // VER: title

https://developer.mozilla.org/en-US/docs/Web/JavaScript   // VER: help

node my_file.js  // VER: run
<script>CODE</script>  in html and opened in web browser // VER: run
*/

fs = require('fs');

/*
console = {
    log: print,
    error: print
};
*/

//------------------------------------------------------------------------------

function hello_world() {
  console.log("Hello World");     // VER: hello_world
}

function read_line_from_console() {
  // in browser?  prompt("Please enter your name", "Harry Potter");
}

function comment() {
  // // This is a comment    // VER: comment
  /* So is this */        // VER: comment
}

function define_variables() {
  let count = 0;              // VER: define_variables
  let username = "Betty";     // VER: define_variables
  let distance = 3.14;        // VER: define_variables
  let email_errors = true;    // VER: define_variables    
}

function define_constants() {
  const GRAVITY = 9.81  // VER: define_constants
}

function arithmetic() {
  let xpos = 0;
  let item_price = 0;
  let quant = 0;
  let count = 0; 

  xpos = xpos + 1;                 // VER: arithmetic
  distance = 3 / 4;                // VER: arithmetic
  total_cost = item_price * quant; // VER: arithmetic
  remainder = 14 % 11;             // VER: arithmetic
  count += 1;                      // VER: arithmetic
}

function if_statement() {
  let username = 'bob';
  let count = 3;

  if (count >= 5 && username == "Jim") {  // VER: if_statement
      console.log("Yes");                 // VER: if_statement
  }                                       // VER: if_statement
  else if (username == "admin" || username == "Bob") {         // VER: if_statement
      console.log("Admin");               // VER: if_statement
  }                                       // VER: if_statement
  else {                                  // VER: if_statement
      console.log("No");                  // VER: if_statement
  }                                       // VER: if_statement
}

function if_statement_more() {
    
}

function for_loop() {
  const data = [5,6,7];                                              // VER: for_loop
  for (let i=0 ; i < data.length ; i++) {                                     // VER: for_loop
    console.log(data[i]);                                               // VER: for_loop
  }                                                                           // VER: for_loop
}

function while_loop() {
  let count = 0;                          // VER: while_loop
  while (count < 10) {                    // VER: while_loop
    console.log("Count is " + count);   // VER: while_loop
    count = count + 2;                  // VER: while_loop
  }
}

function until_loop() {
}

function for_each_loop() {
  const ff = ["a", "b", "c"];    // VER: for_each_loop
  for (let f of ff) {                              // VER: for_each_loop
    console.log(f);                              // VER: for_each_loop
  }                                                   // VER: for_each_loop
}

function file_write() {
  // javascript cannot write to local files because of the security model
  // write to persistant local page storeage
  let localStorage = {"out.txt": ""};
  let line_to_write = "Append to end of file";             // VER: file_write
  localStorage["out.txt"] += line_to_write + "\n";         // VER: file_write
}

function file_read() {
  // File Select
  // javascript cannot access local files unless selected by the user
  let document = {
    getElementById: function(elementId) {
      return {
        addEventListener: function(event, func) {},
      };
    },
  };
  //<input type="file" id="fileInput">                        // VER: file_read_alternate_select
  //<script type="text/javascript">                           // VER: file_read_alternate_select
    let fileInput = document.getElementById('fileInput');   // VER: file_read_alternate_select
    fileInput.addEventListener('change', function(e) {      // VER: file_read_alternate_select
      let reader = new FileReader();                      // VER: file_read_alternate_select
      reader.onload = function(e) {                       // VER: file_read_alternate_select
        console.log(reader.result);                     // VER: file_read_alternate_select
      }                                                   // VER: file_read_alternate_select
      reader.readAsText(fileInput.files[0]);              // VER: file_read_alternate_select
    });                                                     // VER: file_read_alternate_select
  //</script>                                                 // VER: file_read_alternate_select

  // Ajax
  // Can read files within an AJAX callback, this also works for files on webserver
  function readTextFile(file, callback) {                 // VER: file_read_alternate
    let request = new XMLHttpRequest();                 // VER: file_read_alternate
    request.open("GET", file, false);                   // VER: file_read_alternate
    request.onreadystatechange = function() {           // VER: file_read_alternate
      if ( // VER: file_read_alternate
        request.readyState === 4 && // VER: file_read_alternate
        (request.status === 200 || request.status == 0) // VER: file_read_alternate
      ) {  // VER: file_read_alternate
        callback(request.responseText);             // VER: file_read_alternate
      }                                               // VER: file_read_alternate
    }                                                   // VER: file_read_alternate
    request.send(null);                                 // VER: file_read_alternate
  };                                                      // VER: file_read_alternate
  
  // read from persistent local page storage
  let localStorage = {"in.txt": read("in.txt", "text")};
  let line_count = 0;                                     // VER: file_read
  lines = localStorage["in.txt"].split("\n");             // VER: file_read
  for (let line_num in lines) {                           // VER: file_read
    let line = lines[line_num];                         // VER: file_read
    console.log("Line " + line_count + ": " + line);    // VER: file_read
    line_count += 1;                                    // VER: file_read
  }                                                       // VER: file_read
}

function string_concatenation() {
  let forename = 'bob';
  let surname = 'jones';
  let fullname = forename + " " + surname;                // VER: string_concatenation
  let fullname2 = `${forname} ${surname}`;                 // VER: string_concatenation
  console.log(fullname);
}

function convert_string_to_interger_and_back() {
  let sum = 5 + parseInt('5');    // VER: conert_string_to_interger_and_back
  console.log(String(sum))        // VER: conert_string_to_interger_and_back
}

function convert_double_to_string_and_back() {
  let f = parseFloat("3.1415");   // VER: convert_double_to_string_and_back
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
  const aa = Array(3);   // VER: define_fixed_array
  aa[1] = "test";   // VER: define_fixed_array
  console.log(aa);   // VER: define_fixed_array
  console.log(aa[1]);   // VER: define_fixed_array
       // VER: define_fixed_array
  const bb = ["a", "b", "c"];       // VER: define_fixed_array
  console.log(`bb size is ${bb.length}`); // VER: define_fixed_array
  for (let i of bb) {      // VER: define_fixed_array
    console.log(i);      // VER: define_fixed_array
  }                           // VER: define_fixed_array
}

function define_list() {
  const cc = ["a", "b", "c"];  // VER: define_list
  console.log(cc[0]);  // VER: define_list
  const last = cc.pop();  // VER: define_list
  cc.push("d");  // VER: define_list
  const first = cc.shift();  // VER: define_list
  cc.unshift("z");  // VER: define_list
  function remove_by_value(array, v) { // VER: define_list
    const i = array.indexOf(v); if (i > -1) {array.splice(i, 1);}  // VER: define_list
  }  // VER: define_list
  remove_by_value(cc, "b"); // VER: define_list
  for (let i of cc) {  // VER: define_list
    console.log(i); // z d   // VER: define_list
  }  // VER: define_list
  if ("z" in cc) {  // VER: define_list
    console.log("z exists in list");  // VER: define_list
  }  // VER: define_list
}


function define_map() {
  let data = { // VER: define_map
    "a": 1,                                                            // VER: define_map
    "b": 2,                                                            // VER: define_map
  };  // VER: define_map
  console.log(data["b"]);  // prints 2   // VER: define_map
  data["c"] = 3;  // VER: define_map
  delete data["a"];  // VER: define_map
  for (let [k, v] of Object.entries(data)) {  // VER: define_map
    console.log(`Key: ${k}, Value: ${v}`);  //  VER: define_map
  }  //  VER: define_map
  if ("d" in data) {} // VER: define_map
}

function error_handling() {
  try {                                   // VER: error_handling
    // thing that may error             // VER: error_handling
  } catch(e) {                            // VER: error_handling
    // what to do if things go wrong    // VER: error_handling
  }                                       // VER: error_handling
}

function split_strings() {
  let csv_line_test = "Jane,09/09/1989,Female,Blue"   // VER: split_strings
  let line_split = csv_line_test.split(",");          // VER: split_strings
  console.log(line_split[1]);
  let csv_line_test2 = line_split.join(" : ");         // VER: split_strings
}

function random_number() {
  let new_num = Math.round(Math.random() * 100);
  let new_fraction = Math.random()
}

function _switch() {
    
}

function _data_container() {
  let star = {    // VER: data_container
    x: 0,       // VER: data_container
    y: 0,       // VER: data_container
    speed: 0    // VER: data_container
  }               // VER: data_container
}

function read_csv_into_array_of_classs() {
  let file_data = read("test.csv", "text");
  
  let students = []                               // VER: read_csv
  let filename = "test.csv"                       // VER: read_csv
                                                  // VER: read_csv
  // let file_data = "AJAX or localStorage"       // VER: read_csv
  lines = file_data.split("\n");                  // VER: read_csv
  for (let line_num in lines) {                   // VER: read_csv
    let line = lines[line_num];                 // VER: read_csv
    let line_split = line.split(",");           // VER: read_csv
    let new_student = {                         // VER: read_csv
      'forname': line_split[0],               // VER: read_csv
      'surname': line_split[1],               // VER: read_csv
      'date'   : line_split[2] //parse needed // VER: read_csv
    };                                          // VER: read_csv
    students.push(new_student);                 // VER: read_csv
  }                                               // VER: read_csv
  console.log("Loaded %s students" % students.length);  // VER: read_csv
}

function _sleep() {
  // setTimeout is a browser thing and is not available
  function setTimeout(f, timeout) {f();}
  function after_sleep() {                        // VER: sleep
    console.log("slept for a second");          // VER: sleep
  }                                               // VER: sleep
  let timeout = setTimeout(after_sleep, 1000);    // VER: sleep
}

function random_number() {
  const new_num = Math.floor(Math.random() * 100);    // VER: random_number
  const new_fraction = random.random();      // VER: random_number
}


//------------------------------------------------------------------------------
// Unsorted

function list_comprehension() {
  const data1 = [1,2,3,4,5,6];                                                // VER: list_comprehension
  const data2 = data1                                                         // VER: list_comprehension
    .filter(                                                                // VER: list_comprehension
      (i) => i >= 3                                                     // VER: list_comprehension
      // function(i) {return i >= 3;}
    ).map(                                                                  // VER: list_comprehension
      (i) => i * 2                                                      // VER: list_comprehension
      // function(i) {return i * 2;}
    );                                                                      // VER: list_comprehension
}

function dict_comprehension() {
  const data3 = {                                                             // VER: dict_comprehension
    'a': 1,                                                                 // VER: dict_comprehension
    'b': 2,                                                                 // VER: dict_comprehension
    'c': 3,                                                                 // VER: dict_comprehension
  }                                                                           // VER: dict_comprehension
  const data4 = Object.fromEntries(Object.entries(data3)                      // VER: dict_comprehension
    .filter(                                                                // VER: dict_comprehension
      ([k, v]) => v >= 2                                                  // VER: dict_comprehension
      // function([k, v]) {return v >= 2;}
    )                                                                       // VER: dict_comprehension
    .map(                                                                   // VER: dict_comprehension
      ([k, v]) => [v + 10, k]                                             // VER: dict_comprehension
      // function([k, v]) {return [v + 10, k];}
    )                                                                       // VER: dict_comprehension
  );                                                                          // VER: dict_comprehension
}


function define_set() {
  //// javascript has Sets, but no set operations builtin.              // VER: define_set
  //// Copy them from                                                   // VER: define_set
  //// search https://developer.mozilla.org/ for basic set operations   // VER: define_set
  SetOperations = {
    isSuperset: (set, subset) => {
      for (let elem of subset) {if (!set.has(elem)) {return false}} 
      return true
    },
    union: (setA, setB) => {
      let _union = new Set(setA);
      for (let elem of setB) {_union.add(elem)}
      return _union;
    },
    intersection: (setA, setB) => {
      let _intersection = new Set(); 
      for (let elem of setB) {if (setA.has(elem)) {_intersection.add(elem)}} 
      return _intersection
    },
    symmetricDifference: (setA, setB) => {
      let _difference = new Set(setA); 
      for (let elem of setB) {
        if (_difference.has(elem)) {_difference.delete(elem)}
        else                       {_difference.add(elem)}
      }
      return _difference;
    },
    difference(setA, setB) {
      let _difference = new Set(setA);
      for (let elem of setB) {_difference.delete(elem)}
      return _difference;
    },
  }

  const aa = new Set([1, 2, 3]);                     // VER: define_set
  const bb = new Set([2, 3, 4]);                     // VER: define_set
  const cc = new Set([1, 2]);                        // VER: define_set
  console.log(SetOperations.union(aa, bb));          // VER: define_set
  console.log(SetOperations.intersection(aa, bb));   // VER: define_set
  console.log(SetOperations.difference(aa, cc));     // VER: define_set
  console.log(SetOperations.isSuperset(aa, cc));     // VER: define_set
  aa.add(5);                                         // VER: define_set
}


function function_with_param_function() {
  function my_func_1(a, b) {  // VER: function_with_param_function
    return a + b;  // VER: function_with_param_function
  }  // VER: function_with_param_function
  const my_func_2 = (a, b) => a * b; // VER: function_with_param_function
  function print_my_func(ff) {  // VER: function_with_param_function
    console.log(ff(2,3));  // VER: function_with_param_function
  }  // VER: function_with_param_function
  print_my_func(my_func_1); // VER: function_with_param_function
  print_my_func(my_func_2); // VER: function_with_param_function
}

function define_2d_arrays() {
  const width = 3;
  const height = 3;
  const value = 1;

  grid1 = [...Array(height)].map(   // VER: define_2d_arrays_with_nested_arrays
    () => [...Array(width)].map(() => value));   // VER: define_2d_arrays_with_nested_arrays
  grid1[2][1] = 5;    // VER: define_2d_arrays_with_nested_arrays
  console.log(grid1[0][0]);   // VER: define_2d_arrays


    /*
  class Dimension {
    constructor(width, height) {
      this.width = width;
      this.height = height;
    }
    get size() {return self.width * self.height;}
    coord_to_index(x, y) {
      return (y * self.width) + (x % self.width)
    def index_to_cord(self, i):
      return (i % self.width, i//self.width)
    */

  const grid2 = [...Array(width * height)].map(() => value);   // VER: define_2d_arrays_with_1d_array_with_lookup_function
  function coord_to_index(x, y) {return (y * width) + (x % width)}   // VER: define_2d_arrays_with_1d_array_with_lookup_function
  grid2[coord_to_index(2, 1)] = 5;   // VER: define_2d_arrays_with_1d_array_with_lookup_function
  console.log(grid2[coord_to_index(0, 0)]);   // VER: define_2d_arrays_with_1d_array_with_lookup_function
  function index_to_cord(i) {return (i % width, Math.floor(i/width))}   // VER: define_2d_arrays_with_1d_array_with_lookup_function

  const grid3 = {};       // VER: define_2d_arrays_with_dictionary
  for (let y=0 ; y<height ; y++) {  // VER: define_2d_arrays_with_dictionary
    for (let x=0 ; x<width ; x++) {  // VER: define_2d_arrays_with_dictionary
      grid3[`${x},${y}`] = value;     // VER: define_2d_arrays_with_dictionary
    }                        // VER: define_2d_arrays_with_dictionary
  }                            // VER: define_2d_arrays_with_dictionary
  grid3["2,1"] = 5;   // VER: define_2d_arrays_with_dictionary
  console.log(grid3["0,0"]);   // VER: define_2d_arrays_with_dictionary
}

//------------------------------------------------------------------------------

function main() {
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
  //file_read()
  //function()
  function_with_return_value();
  list_comprehension();
  dict_comprehension();
  define_fixed_array();
  define_list();
  define_map();
  define_set();
  function_with_param_function();
  define_2d_arrays();

}
main();

/*
let functions = [];
fs.readFile("_function_order.txt", "utf8", function (err, data) {
    if (err) {
        console.error(err);
    }
    if (data) {
        functions = data.split("\n");
    }
});


for (let i in functions) {
    let function_name = functions[i];
    console.log("-"+function_name+"-");
    try {
        this[function_name]();
    } catch(e) {
        console.error(function_name);
        console.error(e);
    }
}
*/