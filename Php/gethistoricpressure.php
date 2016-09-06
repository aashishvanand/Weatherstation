<?php
error_reporting(-1);
ini_set('display_errors', 'On');

$response = array("error" => FALSE);
$servername = "localhost"; //db host
$username = "root"; //db username
$password = "password"; //db password
$dbname = "temperature"; //db name
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
}
$temp_array = array();
$time_array = array();
$sql = "SELECT pressure,time FROM temperature ORDER BY id DESC LIMIT 30";
$result1 = $conn->query($sql);
if ($result1->num_rows > 0) {
$response["error"] = FALSE;
    // output data of each row
    while($result = $result1->fetch_assoc()) {
$temp = $result["pressure"];
$time = $result["time"];
array_push($temp_array,$temp);
array_push($time_array,$time);
}
$response["pressure"] = $temp_array;
$response["time"] = $time_array;
}
else
{
$response["error"] = true;
}

echo json_encode($response);
$conn->close();
?>
