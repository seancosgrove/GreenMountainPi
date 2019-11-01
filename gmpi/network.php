<?php
include "top.php";
?>

<article id='main'>
<h1>Network</h1>
</article>

<h2>Nmap Capture</h2>

<?php
$nmapFile = fopen("/home/pi/Desktop/final-project/network/nmapcapture.txt","r") or die("Unable to open file.");
echo fread($nmapFile,filesize("/home/pi/Desktop/final-project/network/nmapcapture.txt","r"));
fclose($nmapFile);
?>

<?php
include "bot.php";
?>
</body>
</html>

