#!/usr/bin/python3

# touch messages.py && chmod 744 messages.py && curl -O https://raw.githubusercontent.com/calaldees/TeachProgramming/master/teachprogramming/static/projects/web/web_cgi.py && chmod 755 web_cgi.py && ln -s ./ cgi-bin && touch messages.txt   # VER: run_notes
# python -m CGIHTTPServer 8000       # python2  # VER: run_notes
# python3 -m http.server --cgi 8000  # python3  # VER: run_notes
# http://localhost:8000/cgi-bin/messages.py     # VER: run_notes


from web_cgi import Webpage, env
w = Webpage()

if 'logout' in w.params:                            # VER: logout
    del w.cookie['username']                        # VER: logout
if 'username' in w.params:                          # VER: login
    w.cookie['username'] = w.params['username']     # VER: login
    w.cookie['username']['max-age'] = 3600          # VER: login
                                                    # VER: login
w.print_headers()

print("<html><head>")
print("  <title>Python Message Board</title>")
print("</head><body>")
print("")
print("<h1>Message Board</h1>")
print("")
                                                                        # VER: login
#if True:                                                               # VER: textarea NOT login
if 'username' not in w.cookie:                                          # VER: login
    print("<form action='' method='post'>")                             # VER: login
    print("  Username:<input type='text' name='username' />")           # VER: login
    print("  <input type='submit' value='Login' />")                    # VER: login
    print("</form>")                                                    # VER: login
else:                                                                   # VER: login
    print("<p>you are logged in as %s" % w.cookie['username'].value)    # VER: login
    print("<form action='' method='post'>")                             # VER: textarea
    #print("  Username:<input type='text' name='username' />")          # VER: username NOT login
    print("  Message:<textarea name='message'></textarea>")             # VER: textarea
    print("  Logout: <input type='checkbox' name='logout' />")          # VER: logout
    print("  <input type='submit'   value='Post Message'  />")          # VER: textarea
    print("</form>")                                                    # VER: textarea
                                                                                              # VER: save_message
    messageboard_filename = "messages.txt"                                                    # VER: save_message
                                                                                              # VER: save_message
    ## If there is a message then append it to the end of the file                             # VER: save_message
    if 'message' in w.params:                                                                 # VER: save_message
        file = open(messageboard_filename, 'a')                                               # VER: save_message
        #file.write("<p>%s</p>\n" % (w.params['message']))                                    # VER: save_message NOT username
        #file.write("<p>%s: %s</p>\n" % (w.params['username'], w.params['message']))    # VER: username     NOT login
        file.write("<p>%s: %s</p>\n" % (w.cookie['username'].value, w.params['message']))     # VER: login
        file.close()                                                                          # VER: save_message
                                                      # VER: show_messages
    try:                                              # VER: show_messages
        file = open(messageboard_filename, 'r')       # VER: show_messages
        text = file.read()                            # VER: show_messages
        file.close()                                  # VER: show_messages
        print(text)                                   # VER: show_messages
    except:                                           # VER: show_messages
        pass                                          # VER: show_messages

print("")
print("</body></html>")
