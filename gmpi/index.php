<!-- Sean Cosgrove and Emery Wollerscheid -->
<!-- Green Mountain Pi -->
<!-- CS 121 Final Project -->
<!-- index.php -->

<?php
include "top.php";
?>

<h1>Home</h1>

<div class="container">
    <h2>About the GMPi</h2>

    <p>The Green Mountain Pi is a network and security device with multiple layers of functionality.
    Our goal is to implement multiple methods and applications of security on the RPi and on this UI screen for the user to interact with.
    For network monitoring, we use Raspbian system commands and Nmap to locate networks and perform two different scans.
    To increase cyber security, we implemented a firewall, the antimalware software Rootkit Hunter, and a virtual private network switch.
    Our intrustion detection system is developed off of using iptables to configure firewall settings and the Rootkit Hunter software.
    </p>

    <h2>Our Vision</h2>
    <p>With a larger budget, the concepts used on the GMPi could be upgraded for better performance and more functionality.
    Given an operating system with more compatibility, we could build an intrustion prevention system, layer on different types of antivirus/antimalware, use different networking tools such as Wireshark, and implement a live camera feed. 
    </p>

    <figure>
        <h1><img class="box" 
            src="/img/repomap.jpg"
            alt="Project repository map"
            width="auto"
            height="auto"
        </h1>
    </figure>

</div>

<?php
include "bot.php";
?>


