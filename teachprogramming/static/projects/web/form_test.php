<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" >
<head>
  <title>PHP test</title>
</head>

<body>

<h1>Form Test</h1>

<form action="" method="post">
  Enter Username:<input type="text" name="username">
  <input type="submit" value="button name">
</form>

<?php
if ($_POST['username'] == "martin") {
  echo "I DONT LIKE MARTIN!";
}
else {
  echo "your name is " . $_POST['username'];
}
?>

</body>
</html>

