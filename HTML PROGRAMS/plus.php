<?php
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$regno = $_POST['regno'];
$email = $_POST['email'];
$password = $_POST['password'];

//database connection
$conn = new mysqli('localhost','root','','regestration');
if($conn->connect_error){
    die('Connection Failed :'.$conn->connect_error);
}else{
    $stmt = $conn->prepare("insert into signup(firstname,lastname,regno,email,password) values(?,?,?,?,?)");
    $stmt->bind_param("sssss",$firstname,$lastname,$regno,$email,$password);
    $stmt->execute();
    echo "registration successfully....";
    $stmt->close();
    $conn->close();
}
?>
