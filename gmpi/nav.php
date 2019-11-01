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

       ?>
    </ol>
</nav>
<hr>
