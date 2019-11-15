<?php
include "top.php";
?>

<article id='main'>
<h1>Network</h1>
</article>

<h2>Addresses</h2>

<?php
$IPpy = "/~/../../var/www/network/IP.py";
$nmapPy = "/~/../../var/www/network/nmap.py";
$cmd = escapeshellcmd($IPpy);
$output = shell_exec($cmd);
echo $ouput;

$cmd = escapeshellcmd($nmapPy);
$output = shell_exec($cmd);
echo $output;
?>

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

<h2>Nmap Capture</h2>

<?php
$nmapCapture = "/~/../../var/www/network/nmapcapture.txt";
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
    echo "Unable to open nmapcature.txt";
}
?>

<?php
include "bot.php";
?>


