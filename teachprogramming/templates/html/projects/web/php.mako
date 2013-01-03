<%inherit file="_project.mako"/>


<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'PHP'
    self.text_title_description = 'php bits'
%>
</%def>

<%
    path = 'teachprogramming/static/projects/web/'
%>

<html>
    <head>
        <title>PHP</title>
    </head>
    <body>


<h1>PHP Introduction Workshop</h1>
<h2>Setup</h2>
Install PHP5 using Synaptic package manager
Run the command 
sudo gedit /var/www/testphp.php

<h2>Test PHP</h2>
<pre>
<?php 
  phpinfo(); 
?>
</pre>
<h2>Task 1: Test PHP</h3>
Make a new file in /var/www/
Save it as testphp.php
Go to the webpage http://localhost/testphp.php to test if PHP is working

MyFirst PHP
${h.include_file_(path+'helloworld.php')}


<h2>Task 2: Tell me my IP</h2>
Get your webpage to tell you your IP address by creating a new variable
$ip_address = $_SERVER[‘REMOTE_ADDR’];
Task 3: Test the webserver
Get a friend to visit your webserver by going to http://ipaddress/pagename.php what is their IP address?
Form Input

${h.include_file_(path+'form_test.php')}

<h2>Simple Message Board</h2>


${h.include_file_(path+'messages.php')}

<%doc>
<h1>Simple Message Board</h1>

<form action="" method="post">
  Name:<input type="text" name="username" />
  Message:<input type="textarea" name="message" />
  <input type="submit" value="button name" />
</form>

<?php

$messageboard_filename = "messages.txt";

if ($_POST['username'] != null && $_POST['message']) {
  $file = fopen($messageboard_filename, "a");  #open the file in adding mode
  fwrite($file, "<p>" . $_POST['username'] .  ": " . $_POST['message'] . "</p>\n");
  fclose($file); #close the file
}

$file = fopen($messageboard_filename, "r");  #open the file in read mode
$text = fread($file, filesize($messageboard_filename));
fclose($file);  #close the file

echo ($text);

?>
Note: Like “+” will add numbers together “.” Will add text together
Task 5: Highlight the name
Cookies
Cookies are variables your web browser will remember every time you visit the page (even if you close your web browser)
<?php
  if ($_POST['username']!=null) {
    setcookie ("username", $_POST['username'], time()+36000);
    $_COOKIE['username']=$_POST['username'];
  }
?>
</%doc>

${h.include_file_(path+'cookie_test.php')}

<%doc>
<html>
<head>
  <title>Cookie test</title>
</head>

<body>

<h1>Cookie Test</h1>

<form action='' method='post'>
  Username:<input type='text'   name='username' />
           <input type='submit' value='Login'   />
</form>

last time you told me you were <?php echo ($_COOKIE['username']); ?>

</body>
</html>
</pre>

<h3>User Login</h3>
<p>At the VERY BEGGING of your file (before the &gt;html) you can set Cookies.</p>
<p>Cookies can only be set at the beginning of the file.</p>

<pre>
<?php
  if ($_POST['username']!=null) {
    setcookie ("username", $_POST['username'], time()+36000);
    $_COOKIE['username']=$_POST['username'];
  }
?>

<?php

  if ($_COOKIE['username']==null) {
    echo "<form action='' method='post'>";
    echo "  Username:<input type='text'   name='username' />";
    echo "           <input type='submit' value='Login' />";
    echo "</form>";
  }
  else {
    echo "<p>you are logged in as ".$_COOKIE['username'];
    echo "display a form to enter a message”;


    $messageboard_filename = "messages.txt";

    #If there is a message then write it to the file
    if ($_POST['message']) {
      $file = fopen($messageboard_filename, "a");
      fwrite($file, "<p>" .?.  ": " .?. "</p>\n");
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
</%doc>

<h3>Task 6: Logout</h3>
<p>Can you make a logout button with help from the follow code</p>
<%doc>
  if ($_POST['logout']!=null) {
    setcookie ("username", null, time()+36000);
    $_COOKIE['username'] = null;
  }

    echo "  Logout: <input type='checkbox' name='logout'        />";
</%doc>

<h2>Further PHP Workshop Ideas<h2>

calculator
Random images
User name messages
Calculator
You have visited x – _session _cokie?
Login - you are Andrew
Message board

    </body>
</html>