<!DOCTYPE html>
<html>

<body>

<!-- what to do with form received from "ROLE2020.php"-->

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	// Collect value of input field
	$request = $_POST['command'];
	$impo = $_POST['importance'];
	$name = $_POST['name'];
	if (empty($request)) {
		echo "No Request Detected...";
	}
	else {
		// Feeds python file ROLE2020.py $request and $impo and adds it to MySQL table, then queries instrument $name.
		echo "You requested: " . $request . ". Importance level: " . $impo . ".<br>Sending to: " . $name . "<br>";
		$output = shell_exec("python3 ROLE2020.py '$request' '$impo' '$name'");
	echo "<br>" . $output . "<br>";
	}
}
?>

<!-- For debugging purposes: lets you know if $answer is empty, or allows you to see the value of $answer. -->
<!-- ONLY USE THIS IF: the url in ROLE2020.py has been changed from "hold_answer.php" to "talk_to_me.php" -->

<br><br>

<?php
if (isset($_POST['answer'])) {
	$answer = $_POST['answer'];
	if (empty($answer)) {
	echo "-empty";
	} else {
		// Uncomment the line below to see the value of the variable $answer.
		//echo $answer;
	}
}
?>

</body>
</html>
