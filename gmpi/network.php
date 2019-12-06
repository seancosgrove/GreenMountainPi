<!-- Sean Cosgrove and Emery Wollerscheid -->
<!-- Green Mountain Pi -->
<!-- CS 121 Final Project -->
<!-- network.php -->

<?php
include "top.php";
?>

<article id='main'>
    <h1>Network</h1>
</article>
    <div class="container">
        <div class="row justify-content-md-center">
            <div class="col-md-3">
                <h2>Directions</h2>
            </div>
            <div class="col-md-9">
                <p>The Addresses section displays connected Inet addresses where:</p>
                <p>    wlan0 = connected Wifi network</p>
                <p>    eth0 = laptop connected through ethernet</p>
                <p>    lo = Green Mountain Pi device</p>
                <p>The Nmap Capture Section displays data from scanning TCP ports and identifies the HTTP service</p>
            </div>
        </div>
        <hr>
        <div class="row justify-content-md-center">
            <div class="col-md-3">
                <h2>Addresses</h2>
            </div>
            <div class="col-md-9">
                <?php
                $IPtxt = "/~/../../var/www/network/IP.txt";
                $IPfile = fopen($IPtxt,"r") or die("Unable to open file.");
                echo fread($IPfile,filesize($IPtxt,"r"));
                if ($IPfile) {
                    while (($line = fgets($IPfile)) !== false) {
                        echo "<p>";
                        echo $line;
                        echo "</p>";
                    }
                    fclose($IPfile);
                } else {
                    echo "Unable to open IP.txt";
                }
                ?>
            </div>
        </div>
        <hr>
        <div class="row justify-content-md-center">
            <div class="col-md-3">
                <h2>Nmap Capture</h2>
            </div>
            <div class="col-md-9">
                <?php
                $nmapCapture = "/~/../../var/www/network/nmapCaptureLog.txt";
                $nmapFile = fopen($nmapCapture,"r") or die("Unable to open file.");
                echo fread($nmapFile,filesize($nmapCapture,"r"));
                if ($nmapFile) {
                    while (($line = fgets($nmapFile)) !== false) {
                        echo "<p>";
                        echo $line;
                        echo "</p>";
                    }
                    fclose($nmapFile);
                } else {
                    echo "Unable to open nmapCapture.txt";
                }
                ?>
            </div>
        </div>
    </div>

<?php
include "bot.php";
?>


