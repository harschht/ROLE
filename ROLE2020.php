<!DOCTYPE html>
<html>

<body>

<!-- What to do with form received from "ROLE2020.py" -->

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$response = $_POST['response'];
	if (empty($response)) {
	$check = $_POST['display'];
	echo "<iframe src='iframe_test.html' height='200' width='300' title='Display'></iframe>";
	} else {
		echo "Query Response: " .  $response;
		echo "<br><br>";
	  }
}
?>

<!-- Form setup: sends to "talk_to_me.php" -->

<div>
<form method="post" action="<?php echo "talk_to_me.php";?>">
	Enter Command: <input type="text" name="command"><br>
	Importance Level: <input type="text" name="importance"><br>
	Instrument Name: <input type="text" name="name"><br>
	<input type="submit">
</form>
</div>

<br><br>

<!-- Buttons! -->

<div>
<form method="post" action="<?php echo "talk_to_me.php";?>">
	<button name="command" value="?IDN">Button One</button>
</form>

<br><br>

<form method="post" action="<?php echo "talk_to_me.php";?>">
	<button name="command" value="?IDN">Button Two</button>
</form>

<br><br>

<form method="post" action="<?php echo "talk_to_me.php";?>">
	<button name="command" value="?IDN">Button Three</button>
</form>
</div>

<br><br>


</body>
</html>
