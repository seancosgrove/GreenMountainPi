<?
include "top.php";

$nmapFile = fopen("nmapCapture.txt","r") or die("Unable to open file.");
echo fread($nmapFile,filesize("nmapCapture.txt","r"));
fclose($nmapFile);

include "bot.php";
?>
