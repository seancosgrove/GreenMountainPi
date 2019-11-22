<?php
include "top.php";
?>

<article id='main'>
	<h1>Network</h1>
	<div class="container">
	<div class="row justify-content-md-center">
	    <div class="col-md-3">
	        <h2>Addresses</h2>
	    </div>
	    <div class="col-md-9">

<?php
$IPpy = "/~/../../var/www/network/IP.py";
$nmapPy = "/~/../../var/www/network/nmap.py";
shell_exec('sudo -u www-data python3 /var/www/network/IP.py');
shell_exec('sudo -u www-data python3 ' + $IPpy);

$cmd2 = "sudo -u www-data python3 " + $nmapPy;
shell_exec('sudo -u www-data python3 /var/www/network/nmap.py');
shell_exec('sudo -u www-data python3 ' + $nmapPy);
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
    </div>
</div>
<div class="row">
    <div class="col-md-3">
        <h2>Nmap Capture</h2>
    </div>
    <div class="col-md-9">
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
    </div>
</div>
</div>

<?php
include "bot.php";
?>


