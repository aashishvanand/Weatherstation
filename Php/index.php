<?php
error_reporting(-1);
ini_set('display_errors', 'On');
require_once 'include/db_functions.php';
$db = new db_functions();


if (isset($_POST['temperature']) && isset($_POST['pressure']) && isset($_POST['seapressure']) && isset($_POST['humidity'])&& isset($_POST['latitude']) && isset($_POST['longitude'])&& isset($_POST['altitude'])&& isset($_POST['lightintensity'])&& isset($_POST['co2'])&& isset($_POST['rainfall']) ) {
    // receiving the post params
    $temperature = $_POST['temperature'];
    $pressure = $_POST['pressure'];
    $seapressure = $_POST['seapressure'];
    $humidity = $_POST['humidity'];
    $latitude = $_POST['latitude'];
    $longitude = $_POST['longitude'];
    $altitude = $_POST['altitude'];
    $lightintensity = $_POST['lightintensity'];
    $co2 = $_POST['co2'];
    $rainfall = $_POST['rainfall'];

    // Store the data from Python Script
    $db->storeData($temperature, $pressure, $seapressure, $humidity, $latitude, $longitude, $altitude, $lightintensity, $co2, $rainfall);

}
?>
