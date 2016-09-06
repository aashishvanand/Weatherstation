<?php
error_reporting(-1);
ini_set('display_errors', 'On'); 
class db_functions {

    private $conn;

    // constructor
    function __construct() {
        require_once 'db_connect.php';
        // connecting to database
        $db = new db_connect();
        $this->conn = $db->connect();
    }

    // destructor
    function __destruct() {

   }
 /**
     * Storing new user
     * returns user details
     */
    public function storeData($temperature, $pressure, $seapressure, $humidity, $latitude, $longitude, $altitude, $lightintensity, $co2, $rainfall) {

        $stmt = $this->conn->prepare("INSERT INTO temperature(temperature, pressure, seapressure, humidity, latitude, longitude, altitude, lightintensity, co2, rainfall, time) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NOW())");
        $stmt->bind_param("ssssssssss", $temperature, $pressure, $seapressure, $humidity, $latitude, $longitude,$altitude, $lightintensity, $co2, $rainfall);
        $result = $stmt->execute();
        $stmt->close();
    }

}

?>
