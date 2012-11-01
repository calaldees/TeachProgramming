## -*- coding: utf-8 -*-
<%
    self.titlebar_active       = ''
    self.text_title             = 'Title'
    self.text_title_description = 'Test a little bit of make and shake'
%><%def name="init()"></%def>${self.init()}\
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
    
    <body data-spy="scroll" data-target=".navbar">
        <!-- Navbar -->
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container-fluid">
                    
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </a>
                    
                    
                    <a class="brand" href="/">${project()}</a>
                    
                    <div class="nav-collapse collapse">
                        
                        <ul class="nav pull-right">
                            <li class="dropdown">
                                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                                <ul class="dropdown-menu" role="menu" aria-labelledby="dLabel">
                                    <li><a tabindex="-1" href="#">Action</a></li>
                                    <li><a tabindex="-1" href="#">Another action</a></li>
                                    <li><a tabindex="-1" href="#">Something else here</a></li>
                                    <li class="divider"></li>
                                    <li><a tabindex="-1" href="#">Separated link</a></li>
                                    <%doc>
                                        <% fileexts = resorce_helper.get_project_langs('game',p) %>
                                        % for lang in constants.file_type_to_lang.keys():
                                            % if lang in fileexts:
                                                <a href="/project/game/${p}.${lang}" class="lang_icon lang_${lang} icon16 i_${lang}"><span>${lang}</span></a>
                                            % endif
                                        % endfor
                                    </%doc>
                                </ul>
                            </li>
                        </ul>
                    
                        ##<p class="navbar-text pull-right">
                        ##    Logged in as <a href="#" class="navbar-link">Username</a>
                        ##</p>
                        <ul class="nav">
                            <%
                            titlebar = [
                                #('/'          ,'about'     ),
                                ('/projects'  ,'projects'  ),
                                ('/activities','activities'),
                                ('/reference' ,'reference' ),
                                ('/contact'   ,'contact'   ),
                            ]
                            %>
                            % for url, title in titlebar:
                            <% class_active = ' class="active"' if self.titlebar_active==title else '' %>
                            <li${class_active}><a href="${url}">${title.title()}</a></li>
                            % endfor
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
        <script type="text/javascript" src="/static/site/jquery/jquery-1.8.0.min.js"   ></script>
        <script type="text/javascript" src="/static/site/bootstrap/js/bootstrap.min.js"></script>
        <script type="text/javascript" src="/static/site/prettify/prettify.js"         ></script>
        <script type="text/javascript" src="/static/site/main.js"                      ></script>

    </body>
    
</html>

<%def name="project()">Learn Programming</%def>