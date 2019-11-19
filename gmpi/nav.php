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
	if ($path_parts['filename'] == "surveilance") {
		print ' activePage ';
	}
	print '">';
	print '<a href="surveilance.php">Surveilance</a>';
	print '</li>';

       ?>
    </ol>
</nav>
<hr>
