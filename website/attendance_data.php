<?php
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database_name";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>

<?php
// Get the name and date from the form
$name = $_POST['name'];
$date = date("Y-m-d");

// Insert the attendance record into the table
$sql = "INSERT INTO attendance (name, date) VALUES ('$name', '$date')";

if ($conn->query($sql) === TRUE) {
    echo "Attendance marked successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close the connection
$conn->close();
?>
