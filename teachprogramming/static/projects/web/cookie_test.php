<?php
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

<h1>Cookie Test</h1>

<form action='' method='post'>
  Username:<input type='text'   name='username' />
           <input type='submit' value='Login'   />
</form>

last time you told me you were <?php echo ($_COOKIE['username']); ?>

</body>
</html>

