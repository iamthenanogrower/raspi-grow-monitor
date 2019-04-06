<?php

//db details
$dbname = 'raspi-grow-monitor';
$dbuser = 'your_username';
$dbpass = 'your_password';
$dbhost = 'localhost';

//setup sql
$link = mysqli_connect($dbhost, $dbuser, $dbpass) or die("Unable to Connect to '$dbhost'");
mysqli_select_db($link, $dbname) or die("Could not open the db '$dbname'");

//temp
$test_query = "SELECT value FROM devices WHERE device='temp1'";
$result = mysqli_query($link, $test_query);
$row = mysqli_fetch_array($result);
$temp = $row["value"];

//moist
$test_query = "SELECT value, datetime FROM devices WHERE device='moist1'";
$result = mysqli_query($link, $test_query);
$row = mysqli_fetch_array($result);
$moistval = $row["value"];
$moistdt = $row["datetime"];

//nice, let's output this
echo "<h1>" . $temp . " &#176;C";
echo "<br>";
echo $moistval . " SOIL</h1>";
echo "<br>";
echo "<h2>SINCE " . $moistdt . "</h2>";

?>

