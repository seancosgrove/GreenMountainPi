<?php
$phpSelf = htmlentities($_SERVER['PHP_SELF'], ENT_QUOTES, "UTF-8");
$path_parts = pathinfo($phpSelf);
?>
<!DOCTYPE html>
<html lang='en'>
    <head>
        <title>Green Mountain Pi</title>

        <meta charset='utf-8'>
        <meta name='author' content='Sean Cosgrove and Emery Wollerscheid'>
        <meta name='description' content='Final project for CS 121'>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel="stylesheet" href="/css/gmpi.css" type="text/css" media="screen">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    </head>

    <?php
    include 'header.php';
    include 'nav.php';
    ?>
