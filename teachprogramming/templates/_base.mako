## -*- coding: utf-8 -*-
<%
    self.text_title             = 'Title'
    self.text_title_description = 'Test a little bit of make and shake'
%>\
<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Meta -->
        <meta charset="utf-8">
        <title>${project()}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="Allan Callaghan">
        
        <!-- Styles -->
        <link href="/static/site/bootstrap/css/bootstrap.css"            rel="stylesheet">
        <link href="/static/site/main.css"                               rel="stylesheet">
        <link href="/static/site/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
        
        <!-- IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
            <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        
        <!-- Fav and touch icons -->
        <link rel="shortcut icon" href="/static/favicon.ico">
        ##<link rel="apple-touch-icon-precomposed" sizes="144x144" href="../assets/ico/apple-touch-icon-144-precomposed.png">
        ##<link rel="apple-touch-icon-precomposed" sizes="114x114" href="../assets/ico/apple-touch-icon-114-precomposed.png">
        ##<link rel="apple-touch-icon-precomposed" sizes="72x72"   href="../assets/ico/apple-touch-icon-72-precomposed.png" >
        ##<link rel="apple-touch-icon-precomposed"                 href="../assets/ico/apple-touch-icon-57-precomposed.png" >
    </head>
    
    <body>
        <!-- Navbar -->
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container-fluid">
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </a>
                    <a class="brand" href="#">${project()}</a>
                    
                    <div class="nav-collapse collapse">
                        <p class="navbar-text pull-right">
                            Logged in as <a href="#" class="navbar-link">Username</a>
                        </p>
                        <ul class="nav">
                            <li class="active"><a href="#"       >Home    </a></li>
                            <li               ><a href="#about"  >Projects</a></li>
                            <li               ><a href="#contact">Contact </a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        
        <header class="jumbotron subhead" id="overview">
            <div class="container">
                <h1>${self.text_title}</h1>
                <p class="lead">${self.text_title_description}</p>
            </div>
        </header>
        
        <%doc>
        <div>
            <ul class="breadcrumb">
                <li><a href="#">Home</a> <span class="divider">/</span></li>
                <li><a href="#">Library</a> <span class="divider">/</span></li>
                <li class="active">Data</li>
            </ul>
        </div>
        </%doc>
        
        
        <!-- Body -->
        <div class="container-fluid">
            ${next.body()}
        </div>
        
        <!-- Scripts -->
        <script type="text/javascript" src ="/static/site/jquery/jquery-1.8.0.min.js"   ></script>
        ##<script type="text/javascript" src="/static/site/jquery/jquery-1.7.2.min.js"   ></script>
        <script type="text/javascript" src="/static/site/bootstrap/js/bootstrap.min.js"></script>
        <script type="text/javascript" src="/static/site/prettify/prettify.js"></script>
        <!--
        <script src="assets/js/bootstrap-transition.js"></script>
        <script src="assets/js/bootstrap-alert.js"></script>
        <script src="assets/js/bootstrap-modal.js"></script>
        <script src="assets/js/bootstrap-dropdown.js"></script>
        <script src="assets/js/bootstrap-scrollspy.js"></script>
        <script src="assets/js/bootstrap-tab.js"></script>
        <script src="assets/js/bootstrap-tooltip.js"></script>
        <script src="assets/js/bootstrap-popover.js"></script>
        <script src="assets/js/bootstrap-button.js"></script>
        <script src="assets/js/bootstrap-collapse.js"></script>
        <script src="assets/js/bootstrap-carousel.js"></script>
        <script src="assets/js/bootstrap-typeahead.js"></script>
        <script src="assets/js/bootstrap-affix.js"></script>
        -->
        <script type="text/javascript" src="/static/site/main.js"></script>

    </body>
    
</html>

<%def name="project()">Learn Programming</%def>