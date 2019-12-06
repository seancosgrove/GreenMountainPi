<?php
include "top.php"
?>
<article id="main">
    <h1>Security</h1>
</article>
   <div class="container">
        <div class="row justify-content-md-center">
            <div class="col-md-3">
                <h2>Directions</h2>
            </div>
            <div class="col-md-9">
                <p>The Firewall section displays the firewall logs in reverse so the most recent activity is at the top.</p>
                <p>The Antimalware section displays the rkhunter logs.</p>
                <p>The Nmap Scan section displays data from a scan of UDP ports that are used in DDos reflection attacks.</p>
            </div>
        </div>
        <hr>
        <div class="row justify-content-md-center">
            <div class="col-md-5">
                <h2>Firewall</h2>
            </div>
        </div>
        <div class="scrollBar">
            <?php
            $firewallLogTxt = "/~/../../var/www/firewall/currentFirewallLog.txt";
            $firewallLogFile = fopen($firewallLogTxt,"r") or die("Unable to open file.");
            echo fread($firewallLogFile,filesize($firewallLogTxt,"r"));
            if ($firewallLogFile) {
                while (($line = fgets($firewallLogFile)) !== false) {
                    $length = strlen($line);
                    $messageLength = 15 - $length;
                    $timestamp = substr($line, 0, 15);
                    $message = substr($line, $messageLength);
                    echo '<div class="row justify-content-md-center">'; 
                    echo '<div class="col-md-3">';
                    echo "<p>";
                    echo $timestamp;
                    echo "</p>";
                    echo "</div>";
                    echo '<div class="col-md-9">';
                    echo "<p>";
                    echo $message;
                    echo "</p>";
                    echo "</div>";
                    echo "</div>";
                    echo "<hr>";
                    }
                    fclose($firewallLogFile);
                } else {
                    echo "Unable to open currentFirewallLog.txt";
                }
                ?>
        </div>
        <hr>
        <div class="row justify-content-md-center">
            <div class="col-md-5">
                <h2>Firewall Warnings</h2>
            </div>
        </div>
        <div class="scrollBar">
            <?php
            $firewallLogWarningsTxt = "/~/../../var/www/firewall/firewallLogWarnings.txt";
            $firewallLogWarningsFile = fopen($firewallLogWarningsTxt,"r") or die("Unable to open file.");
            echo fread($firewallLogWarningsFile,filesize($firewallLogWarningsTxt,"r"));
            if ($firewallLogWarningsFile) {
                while (($line = fgets($firewallLogWarningsFile)) !== false) {
                    $length = strlen($line);
                    $messageLength = 15 - $length;
                    $timestamp = substr($line, 0, 15);
                    $message = substr($line, $messageLength);
                    echo '<div class="row justify-content-md-center">';
                    echo '<div class="col-md-3">';
                    echo "<p>";
                    echo $timestamp;
                    echo "</p>";
                    echo "</div>";
                    echo '<div class="col-md-9">';
                    echo "<p>";
                    echo $message;
                    echo "</p>";
                    echo "</div>";
                    echo "</div>";
                    echo "<hr>";
                    }
                    fclose($firewallLogWarningsFile);
                } else {
                    echo "Unable to open firewallLogWarnings.txt";
                }
                ?>
        </div>
        <hr>
        <div class="row justify-content-md-center">
            <div class="col-md-3">
                <h2>Antimalware</h2>
            </div>
        </div>
        <div class="scrollBar">
            <?php
            $rootkitHunterLogTxt = "/~/../../var/www/anti/rootkitHunterLog.txt";
            $rootkitHunterLogFile = fopen($rootkitHunterLogTxt,"r") or die("Unable to open file.");
            echo fread($rootkitHunterLogFile,filesize($rootkitHunterLogTxt,"r"));
            if ($rootkitHunterLogFile) {
                while (($line = fgets($rootkitHunterLogFile)) !== false) {
                    echo '<div class="d-flex flex-row bd-highlight mb-3">';
                    echo "<p>";
                    echo $line;
                    echo "</p>";
                    echo "</div>";
                    echo "<hr>";
                }
                fclose($rootkitHunterLogFile);
            } else {
                echo "Unable to open rootkitHunterLog.txt";
            }
            ?>
        </div>
        <hr>
        <div class="row justify-content-md-center">
            <div class="col-md-5">
                <h2>Rootkit Hunter Warnings</h2>
            </div>
        </div>
        <div class="scrollBar">
            <?php
            $rootkitHunterLogWarningsTxt = "/~/../../var/www/anti/rootkitHunterLogWarnings.txt";
            $rootkitHunterLogWarningsFile = fopen($rootkitHunterLogWarningsTxt,"r") or die("Unable to open file.");
            echo fread($rootkitHunterLogWarningsFile,filesize($rootkitHunterLogWarningsTxt,"r"));
            if ($rootkitHunterLogWarningsFile) {
                while (($line = fgets($rootkitHunterLogWarningsFile)) !== false) {
                    echo '<div class="d-flex flex-row bd-highlight mb-3">';
                    echo "<p>";
                    echo $line;
                    echo "</p>";
                    echo "</div>";
                    echo "<hr>";
                }
                fclose($rootkitHunterLogWarningsFile);
            } else {
                echo "Unable to open rootkitHunterLogWarnings.txt";
            }
            ?>
        </div>
        <hr>
        <div class="row justify-content-md-center">
            <div class="col-md-3">
                <h2>Nmap Scan</h2>
            </div>
            <div class="col-md-9">
                <?php
                $nmapScan = "/~/../../var/www/network/nmapScanLog.txt";
                $nmapFile = fopen($nmapScan,"r") or die("Unable to open file.");
                echo fread($nmapFile,filesize($nmapScan,"r"));
                if ($nmapFile) {
                    while (($line = fgets($nmapFile)) !== false) {
                        echo "<p>";
                        echo $line;
                        echo "</p>";
                    }
                    fclose($nmapFile);
                } else {
                    echo "Unable to open nmapScan.txt";
                }
                ?>
            </div>
        </div>
    </div>

<?php
include "bot.php"
?>

