<?
include "top.php";

$nmapFile = fopen("/home/pi/Desktop/final-project/network/nmapcapture.txt","r") or die("Unable to open file.");
echo fread($nmapFile,filesize("/home/pi/Desktop/final-project/network/nmapcapture.txt","r"));
fclose($nmapFile);

include "bot.php";
?>
</body>
</html>
