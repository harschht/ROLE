<!DOCTYPE html>
<html>

<body>

<?php
if (isset($_POST['answer'])) {
	$answer = $_POST['answer'];
	if (empty($answer)) {
	echo "Query Unsuccessful...<br>";
	} else {
		// Uncomment the line below to see the value of the variable $answer.
		//echo $answer;
		}
}
?>

<!-- Use this button to return to ROLE2020.php. -->

<form method="post" action="<?php echo "ROLE2020.php";?>">
	<button name="response" value="<?php echo "$answer";?>">Back to ROLE!</button>
</form>

<!-- Use this button if an SCPI cpommand to display instrument screen is used. -->

<form method="post" action="<?php echo "ROLE2020.php";?>">
	<button name="display" value="<?php echo "Check";?>">Display!</button>
</form>

</body>
</html>

