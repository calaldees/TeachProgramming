#!/usr/bin/python

# ln -s ./ cgi-bin
# chmod 755 /cgi-bin/messages.py
# chmod 755 /cgi-bin/web_cgi.py
# python -m CGIHTTPServer 8000
# python -m webbrowser -t "http://localhost:8000/cgi-bin/messages.py"

from web_cgi import Webpage, env
w = Webpage()

if 'logout' in w.params:
    del w.cookie['username']
if 'username' in w.params:
    w.cookie['username'] = w.params['username']
    w.cookie['username']['max-age'] = 3600

w.print_headers()

print("<html><head>")
print("  <title>Python Message Board</title>")
print("</head><body>")
print("")
print("<h1>Message Board</h1>")
print("")

if 'username' not in w.cookie:
    print("<form action='' method='post'>")
    print("  Username:<input type='text' name='username' />")
    print("  <input type='submit' value='Login' />")
    print("</form>")
else:
    print("<p>you are logged in as %s" % w.cookie['username'].value)
    print("<form action='' method='post'>")
    print("  Message:<input type='textarea' name='message'       />")
    print("  Logout: <input type='checkbox' name='logout'        />")
    print("          <input type='submit'   value='Post Message' />")
    print("</form>")

    messageboard_filename = "messages.txt"

    # If there is a message then append it to the end of the file
    if 'message' in w.params:
        file = open(messageboard_filename, 'a')
        file.write("<p>%s: %s</p>\n" % (w.cookie['username'].value, w.params['message']))
        file.close()

    try:
        # Open the file in read mode
        file = open(messageboard_filename, 'r')
        text = file.read()
        file.close()

        # Print the text file
        print(text)
    except:
        pass

print("")
print("</body></html>")
