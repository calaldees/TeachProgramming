<?php                                                               # VER: login
    if ($_POST['logout']!=null) {                                   # VER: logout
        setcookie ("username", null, time()+36000);                 # VER: logout
        $_COOKIE['username'] = null;                                # VER: logout
    }                                                               # VER: logout
    if ($_POST['username']!=null) {                                 # VER: login
        setcookie ("username", $_POST['username'], time()+36000);   # VER: login
        $_COOKIE['username']=$_POST['username'];                    # VER: login
    }                                                               # VER: login
?>                                                               <!-- VER: login -->
<html>
    <head>
        <title>PHP Message Board</title>
    </head>

    <body>
        <h1>Message Board</h1>
        <!-- Launch server on OSX with
        python -m webbrowser -t "http://localhost:8000/messages.php" && touch messages.txt && php -S 127.0.0.1:8000 -t .
        -->

<?php                                                                           # VER: textarea
    if ($_COOKIE['username']==null) {                                           # VER: login
        echo "<form action='' method='post'>";                                  # VER: login
        echo "  Username:<input type='text' name='username' />";                # VER: login
        echo "  <input type='submit' value='Login' />";                         # VER: login
        echo "</form>";                                                         # VER: login
    }                                                                           # VER: login
    else {                                                                      # VER: login
        echo "<p>you are logged in as ".$_COOKIE['username'];                   # VER: login
        echo "<form action='' method='post'>";                                  # VER: textarea
        #echo "  Username:<input type='text' name='username'          />";      # VER: username NOT login
        echo "  Message :<textarea name='message'></textarea>";                 # VER: textarea
        echo "  Logout  :<input type='checkbox' name='logout'        />";       # VER: logout
        echo "           <input type='submit'   value='Post Message' />";       # VER: textarea
        echo "</form>";                                                         # VER: textarea
                                                                                # VER: textarea
        $messageboard_filename = "messages.txt";                                  # VER: save_message
                                                                                  # VER: save_message
        #If there is a message then append it to the end of the file              # VER: save_message
        if ($_POST['message']) {                                                  # VER: save_message
            $file = fopen($messageboard_filename, "a"); #Open file in append mode # VER: save_message
            #fwrite($file, "<p>".$_POST['message']."</p>\n");                           # VER: save_message NOT username
            #fwrite($file, "<p>".$_POST['username'].": ".$_POST['message']."</p>\n");   # VER: username     NOT login
            fwrite($file, "<p>".$_COOKIE['username'].": ".$_POST['message']."</p>\n");  # VER: login
            fclose($file);                                                        # VER: save_message
        }                                                                         # VER: save_message
                                                                                # VER: show_messages
        $file = fopen($messageboard_filename, "r"); #Open the file in read mode # VER: show_messages
        $text = fread($file, filesize($messageboard_filename));                 # VER: show_messages
        fclose($file);                                                          # VER: show_messages
        echo ($text); #Print the text file                                      # VER: show_messages
    }                                                                           # VER: login
?>                                                                           <!-- VER: textarea -->
    </body>
</html>
