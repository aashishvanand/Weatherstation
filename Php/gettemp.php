<?php
error_reporting(-1);
ini_set('display_errors', 'On');

$response = array("error" => FALSE);
$servername = "localhost"; //db host
$username = "root"; //db user
$password = "password"; //db password
$dbname = "temperature"; //db name
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM temperature ORDER BY id DESC LIMIT 1";
$result1 = $conn->query($sql);
if ($result1->num_rows > 0) {
    // output data of each row
    while($result = $result1->fetch_assoc()) {

$response["error"] = FALSE;
$response["temperature"] = $result["temperature"];
$response["pressure"] = $result["pressure"];
$response["seapressure"] = $result["seapressure"];
$response["humidity"] = $result["humidity"];
$response["latitude"] = $result["latitude"];
$response["longitude"] = $result["longitude"];
$response["altitude"] = $result["altitude"];
$response["lightintensity"] = $result["lightintensity"];
$response["co2"] = $result["co2"];
$response["rainfall"] = $result["rainfall"];
$response["lastupdated"] = $result["time"];
}
}
else
{
$response["error"] = true;
}

echo json_encode($response);
$conn->close();
?>
