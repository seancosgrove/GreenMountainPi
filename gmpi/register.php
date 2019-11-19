<?php
// include config file
// include "config.php";

// initialize variables
$email = "";
$username = "";
$password = "";
$confirmPassword = "";
$emailError = false;
$usernameError = false;
$passwordError = false;
$confirmPasswordError = false;
$errorMsg = array();
$accountData = array();
$mailed = false;

// process for when form is submitted
if (isset($_POST["btnSubmit])) {

    $email = filter_var($_POST["txtEmail"], FILTER_SANITIZE_EMAIL);
    $accountData[] = $email;

    $username = htmlentities($_POST["txtUsername"], ENT_QUOTES, "UTF-8");
    $accountData[] = $username;

    $password = htmlentities($_POST["txtPassword"], ENT_QUOTES, "UTF-8");
    $accountData[] = $password;

    $confirmPassword = htmlentities($_POST["txtConfirmPassword"], ENT_QUOTES, "UTF-8");
    $accountData[] = $confirmPassword;

    // validate data
    if ($email == ""){
        $errorMsg[] = "Please enter a valid email address.";
        $emailError = true;
    }

    if ($username == ""){
        $errorMsg[] = "Please enter a username.";
        $emailError = true;
    }

    if ($password == ""){
        $errorMsg[] = "Please enter a password.";
        $emailError = true;
    }

    if ($confirmPassword == ""){
        $errorMsg[] = "Please confirm your password.";
        $emailError = true;
    }
/*
    // if (!$errorMsg) {
        // if ($debug) {
            print '<p>Form is valid</p>';
        // }

        // save data
        $directory = '';
        $file = 'users';
        $fileExt = 'csv';
        $filename = $directory . $file . $fileExt;
        // if ($debug) {
            print '<p>filename is ' . $filename . '</p>';
        // }
        $file = fopen($filename, 'a');
        fputcsv($file, $accountData);
        fclose($file);
    // }
*/
}
?>

<?php
include "top.php";
?>

<article id='main'>
<h1>Register</h1>
</article>

<form action="submit"
          id = "frmRegister"
          method = "post">
        <fieldset>
            <legend>Join Us</legend>
            <p>
                <label class="required text-field" for="txtEmail">Email:</label>
                <input
                // <?php if ($emailError) print 'class="mistake"'; ?>
                    id = "txtEmail"
                    maxlength = "45"
                    name="txtEmail"
                    onfocus="this.select()"
                    placeholder="Enter your email address"
                    tabindex="10"
                    type="text"
                    value="<?php print $email; ?>"
                    >
            </p>
            <p>
                <label class="required text-field" for="txtUsername">Username:</label>
                <input
                // <?php if ($usernameError) print 'class="mistake"'; ?>
                    id = "txtUsername"
                    maxlength = "25"
                    name="txtUsername"
                    onfocus="this.select()"
                    placeholder="Enter your username"
                    tabindex="20"
                    type="text"
                    value="<?php print $username; ?>"
                    >
            </p>
            <p>
                <label class="required text-field" for="txtPassword">Password:</label>
                <input
                // <?php if ($passwordError) print 'class="mistake"'; ?>
                    id = "txtPassword"
                    minlength = "8"
                    maxlength = "25"
                    name="txtPassword"
                    onfocus="this.select()"
                    placeholder="Enter a password"
                    tabindex="30"
                    type="text"
                    value="<?php print $password; ?>"
                    >
            </p>
            <p>
                <label class="required text-field" for="txtConfirmPassword">Confirm Password:</label>
                <input
                // <?php if ($confirmPasswordError) print 'class="mistake"'; ?>
                    id = "txtConfirmPassword"
                    minlength = "8"
                    maxlength = "25"
                    name="txtConfirmPassword"
                    onfocus="this.select()"
                    placeholder="Confirm your password"
                    tabindex="40"
                    type="text"
                    value="<?php print $confirmPassword; ?>"
                    >
            </p>
        </fieldset>
        <fieldset>
            <legend></legend>
            <input class="button" id="btnSubmit" name="btnSubmit" tabindex="100" type="submit" value="Register">
        </fieldset>
    </form>
<?php
    // }
?>
<?php
include "bot.php";
?>



