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

        <?php
//-----------------------
// DEBUG AND PATH SET UP
//-----------------------
        $debug = false;
        if (isset($_GET['debug'])) {
            $debug = true;
        }

        $domain = '//';
        $server = htmlentities($_SERVER['SERVER_NAME'], ENT_QUOTES, 'UTF-8');
        $domain .= $server;

        if ($debug) {
            print '<p>php Self: ' . $phpSelf;
            print '<p>Path Parts<pre>';
            print_r($path_parts);
            print '</pre></p>';
        }
        ?>

    </head>

    <?php
    print '<bodyid="' . $path_parts['filename'] . '">';
    include 'header.php';
    include 'nav.php';

    if ($debug) {
        print '<p>DEBUG MODE IS ON</p>';
    }
    ?>
