<?php
# PHP 5                                        # VER: title
# windows.php.net/download/                    # VER: download
# www.apachefriends.org/en/xampp.html          # VER: download
# XAMPP Lite (if you want a mini web server)   # VER: download

function hello_world() {
#<?php                    # VER: hello_world
  echo "Hello World\n";   # VER: hello_world
#? >                       # VER: hello_world
}

function read_line_from_console() {
    #$username = fgets(STDIN);      # VER: read_line_from_console
}

function comment() {
    #This is a comment          # VER: comment
    /* so is this */            # VER: comment
}

function define_variables() {
    $count = 0;             # VER: define_variables
    $username = "Betty";    # VER: define_variables
    $distance = 3.14;       # VER: define_variables
    $email_errors = True;   # VER: define_variables
}

function define_constats() {
    define("GRAVITY", 9.81);   # VER: define_constants
}

function arithmetic() {
    $xpos = $xpos + 1;                      # VER: arithmetic
    $distance = 3 / 4;                      # VER: arithmetic
    $total_cost = $item_price * $quant;     # VER: arithmetic
    $remainder = 14 % 11;                   # VER: arithmetic
    $count += 1;                            # VER: arithmetic
}

function if_statement() {
    $username = 'bob';
    $count = 3;
    
    if ($count>=5 && $username == "Jim") {  # VER: if_statement
        echo "Yes\n";                       # VER: if_statement
    }                                       # VER: if_statement
    elseif ($username == "admin") {         # VER: if_statement
        echo "Admin\n";                     # VER: if_statement
    }                                       # VER: if_statement
    else {                                  # VER: if_statement
        echo "No\n";                        # VER: if_statement
    }                                       # VER: if_statement
}

function if_statement_more() {
    
}

function for_loop() {
    $username = 'bob';
    for ($count = 0 ; $count < strlen($username) ; $count++) {  # VER: for_loop
      echo "$username[$count]\n";                               # VER: for_loop
    }                                                           # VER: for_loop
}

function while_loop() {
    $count = 0;                         # VER: while_loop
    while ($count < 10) {               # VER: while_loop
        echo "Count is ".$count."\n";   # VER: while_loop
        $count = $count + 2;            # VER: while_loop
    }                                   # VER: while_loop
}

function until_loop() {
    $word = "gibber";               # VER: until_loop
    do {                            # VER: until_loop
        $word = $word . $word;      # VER: until_loop
    }                               # VER: until_loop
    while (strlen($word) < 10);     # VER: until_loop
    echo $word."\n";                # VER: until_loop
}

function for_each_loop() {
    $names = array ("Bob","Ben","Bill","Borris","Bin"); # VER: for_each_loop
    foreach ($names as $name) {                         # VER: for_each_loop
        echo $name."\n";                                # VER: for_each_loop
    }                                                   # VER: for_each_loop
}

function file_write() {
    $line_to_write = "Append to end of file";   # VER: file_write
    $file = fopen("out.txt", "a");              # VER: file_write
    fwrite($file, $line_to_write. "\n");        # VER: file_write
    fclose($file);                              # VER: file_write
}

function file_read() {
    $line_count = 0;                        # VER: file_read
    $file = fopen("in.txt", "r");           # VER: file_read
    while($line=fgets($file)) {             # VER: file_read
      echo "Line ".$line_count.": ".$line;  # VER: file_read
      $line_count += 1;                     # VER: file_read
    }                                       # VER: file_read
    fclose($file);                          # VER: file_read
}

function string_concatination() {
    $forename = 'bob';
    $surname = 'jones';
    $fullname = $forename." ".$surname;     # VER: string_concatination
    echo $fullname."\n";
}

function convert_string_to_interger_and_back() {
    $sum = 5 + intval("5");
    echo (string)sum;
}

function convert_double_to_string_and_back() {
    
}

function _function() {
    function sayHello() {   # VER: function
      echo "Hello\n";       # VER: function
      echo "Goodbye\n";     # VER: function
    }                       # VER: function
    sayHello();
}

function function_with_return_value() {
    function biggest ($a, $b) {     # VER: function_with_return_value
        if ($a > $b) {              # VER: function_with_return_value
            return $a;              # VER: function_with_return_value
        }                           # VER: function_with_return_value
        else {                      # VER: function_with_return_value
            return $b;              # VER: function_with_return_value
        }                           # VER: function_with_return_value
    }                               # VER: function_with_return_value
    echo biggest(1, 2);
    echo "\n";
}

function function_with_params_by_reference() {
    
}

function function_with_params_by_value() {
    
}

function define_fixed_array() {
    $names = array();                           # VER: define_fixed_array
    $names[0] = "Bob";                          # VER: define_fixed_array
    $names[1] = "Foo";                          # VER: define_fixed_array
    $names[2] = "Rah";                          # VER: define_fixed_array
    foreach ($names as $name) {                 # VER: define_fixed_array
        echo $name."\n";                        # VER: define_fixed_array
    }                                           # VER: define_fixed_array
    echo "array size is ".count($names)."\n";   # VER: define_fixed_array
}

function define_2d_arrays() {
    $grid = array(array());                             # VER: define_2d_arrays
    for ($x=0;$x<10;$x++) { #Fill the grid with 0's     # VER: define_2d_arrays
        for ($y=0;$y<10;$y++) {                         # VER: define_2d_arrays
            $grid[$x][$y] = 0;                          # VER: define_2d_arrays
        }                                               # VER: define_2d_arrays
    }                                                   # VER: define_2d_arrays
    $grid[5][5] = 1;                                    # VER: define_2d_arrays
}

function linked_list() {
    $list = array();                                        # VER: linked_list
    $list[] = "Bill"; #Add to end of array                  # VER: linked_list
    $list[] = "Ben";                                        # VER: linked_list
    $list[] = "Bob";                                        # VER: linked_list
    unset($list[1]); #No language feature to search for     # VER: linked_list
    array_pop($list); #Remove last item                     # VER: linked_list
    array_unshift($list, "Kim"); #Add first                 # VER: linked_list
    foreach ($list as $name) {                              # VER: linked_list
      echo $name."\n";                                      # VER: linked_list
    }                                                       # VER: linked_list
    echo "list size is ".count($list)."\n";                 # VER: linked_list
}

function define_map() {
    $dict = array();                                    # VER: define_map
    $dict['Joe'] = 77;                                  # VER: define_map
    $dict['Jane'] = 51;                                 # VER: define_map
    foreach($dict as $key){ //$key => $value            # VER: define_map
        echo "Key: ".$key." Value: ".$dict[$key]."\n";  # VER: define_map
    }                                                   # VER: define_map
}

function error_handling() {
    
}

function split_strings() {
    $csv_line_test = "Jane,09/09/1989,Female,Blue"; # VER: split_strings
    $line_split = explode(",", $csv_line_test);     # VER: split_strings
}

function random_number() {
    $new_num = rand(0, 100);    # VER: random_number
    $new_fraction = rand();     # VER: random_number
}

function _switch() {
    switch (condition) {
        case "value1" :
           break;
        case "value2" :
            break;
        default :
            break;    
    }
}

function _class() {
    class Star {
        public $x;
        public $y;
        public $speed;
    }
    $s = new Star();
    $s->x = 100;
}

function read_csv_into_array_of_classs() {
    #<?php                                          # VER: read_csv_into_array_of_classs
    class Student {                                 # VER: read_csv_into_array_of_classs
      public $forename;                             # VER: read_csv_into_array_of_classs
      public $surname;                              # VER: read_csv_into_array_of_classs
      public $dob;                                  # VER: read_csv_into_array_of_classs
    }                                               # VER: read_csv_into_array_of_classs
                                                    # VER: read_csv_into_array_of_classs
    $filename = "test.csv";                         # VER: read_csv_into_array_of_classs
    $students = array();                            # VER: read_csv_into_array_of_classs
                                                    # VER: read_csv_into_array_of_classs
    $file = fopen($filename, "r");                  # VER: read_csv_into_array_of_classs
    while($line=fgets($file)) {                     # VER: read_csv_into_array_of_classs
      $line_split = explode(",", $line);            # VER: read_csv_into_array_of_classs
      $new_student = new Student();                 # VER: read_csv_into_array_of_classs
      $new_student->forename = $line_split[0];      # VER: read_csv_into_array_of_classs
      $new_student->surname  = $line_split[1];      # VER: read_csv_into_array_of_classs
      $new_student->date     = $line_split[2];      # VER: read_csv_into_array_of_classs
      $students[] = $new_student;                   # VER: read_csv_into_array_of_classs
    }                                               # VER: read_csv_into_array_of_classs
    fclose($file);                                  # VER: read_csv_into_array_of_classs
    echo "Loaded ".count($students)." students\n";  # VER: read_csv_into_array_of_classs
    #? >                                            # VER: read_csv_into_array_of_classs
}

function _sleep() {
    
}


#-------------------------------------------------------------------------------

function title($title) {
    echo "-".$title."-\n";
}
$file = fopen("_function_order.txt", "r");
while($line=fgets($file)) {
    $line = trim($line);
    title($line);
    $line();
}
fclose($file);
