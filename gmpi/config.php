<?php
$credentialsTxt="/credentials.txt";
$credentialsFile = fopen($credentialsTxt, "r") or die ("Unable to open file.");
echo fread($credentialsFile,filesize($credentialsTxt,"r"));
$credentials = array();
if ($credentialsFile) {
    while (($line = fgets($credentialsTxt)) !== false) {
        array_push($credentials, $line);
        print_r($credentials,);
    }
} else {
    echo "Unable to open credentials.txt";
}
?>
