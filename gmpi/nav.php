<hr>
<nav>
    <ol>
        <?php
        print'<li class="';
        if ($path_parts['filename'] == "index") {
            print ' activePage ';
        }
        print '">';
        print '<ahref="index.php">Home</a>';
        print '</li>';

	print'<li class="';
        if ($path_parts['filename'] == "network") {
            print ' activePage ';
        }
        print '">';
        print '<ahref="network.php">Nmap Capture</a>';
        print '</li>';

       ?>
    </ol>
</nav>
<hr>
