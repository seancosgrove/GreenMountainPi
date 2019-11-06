<?php
include "top.php";
?>

<article id='main'>
<h1>Network</h1>
</article>

<h2>Nmap Capture</h2>

<?php
$nmapFile = fopen("/../network/nmapcapture.txt","r") or die("Unable to open file.");
echo fread($nmapFile,filesize("/../network/nmapcapture.txt","r"));
fclose($nmapFile);
echo "Done";
?>

<?php>
file_get_contents("/../network/nmapcapture.txt");
echo "Done";
?>

<?php
include "bot.php";
?>
</body>
</html>

