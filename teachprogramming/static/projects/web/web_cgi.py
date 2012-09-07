"""
Lightweight CGI framework to give cookie and session control to a basic Python 2.2+ scripts

Example Use:

from web_cgi import Webpage, env
w = Webpage()
#w.cookie['my_field']='my value' # (optional)
w.print_headers()

"""

# References
#  - http://code.activestate.com/recipes/325484-a-very-simple-session-handling-example/
#  - http://www.doughellmann.com/PyMOTW/Cookie/

# Imports/Dependecys -----------------------------------------------------------

import sys, os, pickle          # System imports
import cgi                      # For accessing web form data
import cgitb; cgitb.enable()    # If there is an error in the script show it as an HTML page for web debugging
import Cookie                   # Cookie's - WAIT! Maybe we should tell the EU and the user, we are breaking the law, such a filthy criminal I am

env = os.environ

class Webpage():
    def __init__(self, *args, **kwargs):
        """
        Setup a new webpage with cookies, session and params
        """
        self.session_path = kwargs.get('session_path','.sessions')
        
        # Setup .sessions folder to store session data in static files
        if not os.path.exists(self.session_path):
            os.mkdir(self.session_path)
        
        # Import GET/POST params
        class form(dict):
            def __init__(self, fields):
                dict.__init__(self, fields)
                for k, v in self.items(): self[k] = v.value
        self.params = form(cgi.FieldStorage())  # Get web form data as form

        # Setup webpage variables
        self.cookie  = Cookie.SimpleCookie(env.get('HTTP_COOKIE',''))
        self.session = {}
        self.headers = {'Content-type':'text/html'}

        # Get or Generate session_id
        if 'sid' in self.cookie:
            self.session_id = self.cookie['sid'].value
            del self.cookie['sid']
        else:
            import sha, time
            self.session_id = sha.new(str(time.time())).hexdigest()
            self.cookie['sid'] = self.session_id
            
        # Load session_id file
        if os.path.exists(os.path.join(self.session_path, self.session_id)):
            session_file = open(os.path.join(self.session_path, self.session_id), 'rb')
            self.session = pickle.load(session_file)
            session_file.close()

    def print_headers(self):
        """
        Write headers/cookie - once this is done no cookie editing can occour
        """
        for k, v in self.headers.items():
            print('%s: %s' % (k, v))
        if self.cookie:
            print(self.cookie)
        sys.stdout.write('\n')

        #self.cookie = None

    def session_save(self):
        """
        Save the current session to static session file
        """
        session_file = open(os.path.join(self.session_path, self.session_id), 'wb')
        pickle.dump(self.session, session_file, 1)
        session_file.close()


