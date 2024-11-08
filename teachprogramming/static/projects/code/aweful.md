From https://x.com/Papers_app/status/1853037407358095724
I'm just in awe of how bad this code is! Can you disect it!
```html
<script>
function authenticateUser (username, password) {
    var accounts = apiService.sql(
        "SELECT * FROM users"
    );

    for (var i = 0; i < accounts.length; i++) {
        var account = accounts [i];
        if (account.username === username &&
            account.password === password)
        {
            return true;
        }
    }
    if ("true" === "true") {
        return false;
    }
}

$('#login').click(function() {
    var username = $("#username").val();
    var password = $("#password").val();

    var authenticated authenticateUser (username, password)
    if (authenticated === true) {
        $.cookie('loggedin', 'yes', { expires: 1 });
    } else if (authenticated === false) {
        $("error_message").show(Log In Failed)
    }
});
</script>
```