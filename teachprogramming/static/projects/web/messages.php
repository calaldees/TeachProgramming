<?php
  if ($_POST['logout']!=null) {
    setcookie ("username", null, time()+36000);
    $_COOKIE['username'] = null;
  }
  if ($_POST['username']!=null) {
    setcookie ("username", $_POST['username'], time()+36000);
    $_COOKIE['username']=$_POST['username'];
  }
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" >
<head>
  <title>PHP test</title>
</head>

<body>

<h1>Form Test</h1>


<?php

  if ($_COOKIE['username']==null) {
    echo "<form action='' method='post'>";
    echo "  Username:<input type='text'   name='username' />";
    echo "           <input type='submit' value='Login' />";
    echo "</form>";
  }
  else {
    echo "<p>you are logged in as ".$_COOKIE['username'];
    echo "<form action='' method='post'>";
    echo "  Message:<input type='textarea' name='message'       />";
    echo "  Logout: <input type='checkbox' name='logout'        />";
    echo "          <input type='submit'   value='Post Message' />";
    echo "</form>";


    $messageboard_filename = "messages.txt";

    #If there is a message then write it to the file
    if ($_POST['message']) {
      $file = fopen($messageboard_filename, "a");
      fwrite($file, "<p>" . $_COOKIE['username'] .  ": " . $_POST['message'] . "</p>\n");
      fclose($file);
    }

    #Open the file in read mode
    $file = fopen($messageboard_filename, "r");
    $text = fread($file, filesize($messageboard_filename));
    fclose($file);

    #Print the text file
    echo ($text);
  }


?>

</body>
</html>

