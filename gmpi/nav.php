<hr>
<nav>
    <ol>
        <?php
        print'<li class="';
        if ($path_parts['filename'] == "index") {
            print ' activePage ';
        }
        print '">';
        print '<a href="index.php">Home</a>';
        print '</li>';

	print'<li class="';
        if ($path_parts['filename'] == "network") {
            print ' activePage ';
        }
        print '">';
        print '<a href="network.php">Network</a>';
        print '</li>';

        print'<li class="';
        if ($path_parts['filename'] == "security") {
                print ' activePage ';
        }
        print '">';
        print '<a href="security.php">Security</a>';
        print '</li>';

	print'<li class="';
	if ($path_parts['filename'] == "surveillance") {
		print ' activePage ';
	}
	print '">';
	print '<a href="surveillance.php">Surveillance</a>';
	print '</li>';

       ?>
    </ol>
</nav>
<hr>
