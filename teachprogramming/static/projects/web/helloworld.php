<?php
$browser = $_SERVER['HTTP_USER_AGENT'];
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" >
<head>
  <title>My First PHP page</title>
</head>

<body>

<h1>My First PHP Page</h1>
Yor browser is <?php echo $browser; ?>

</body>
</html>

