## -*- coding: utf-8 -*-
<%
    self.titlebar_active       = ''
    self.text_title             = 'Title'
    self.text_title_description = 'Test a little bit of make and shake'

%><%def name="init()"></%def>${self.init()}\
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>${project_title()}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="Allan Callaghan">
        
        <!-- Styles -->
        <link href="/static/site/bootstrap/css/bootstrap.css"            rel="stylesheet"/>
        <link href="/static/site/prettify/prettify.css"                  rel="stylesheet"/>
        <link href="/static/site/main.css"                               rel="stylesheet"/>
        <link href="/static/site/bootstrap/css/bootstrap-responsive.css" rel="stylesheet"/>
        
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
    
    <body data-spy="scroll" data-target=".sidebar-nav-container" data-offset="60">
        <!-- Navbar -->
        <div class="navbar navbar-fixed-top">
            ## navbar-inverse ##navbar-lang-${selected_lang}
            <div class="navbar-inner">
                <div class="container-fluid">
                    
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </a>
                    
                    
                    <a class="brand" href="${request.route_path('root', _query=dict(selected_lang=selected_lang))}">${project_title()}</a>
                    
                    <div class="nav-collapse collapse">
                        
                        <ul class="nav pull-right lang_select">
                            
                            <li class="dropdown">
                                <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="icon-lang-${selected_lang}"></i>${h.constants.file_type_to_lang[selected_lang]}<b class="caret"></b></a>
                                <ul class="dropdown-menu">                            
                                <%
                                    try:
                                        avalable_langs = h.get_project_langs(project_type, project)
                                    except:
                                        avalable_langs = []
                                %>
                                % for lang, language_name in h.langs():
                                    <% _class = 'current' if lang==selected_lang else '' %>
                                    % if lang in avalable_langs:
                                    <li class='avalable ${_class}'>
                                    % else:
                                    ##<li class='unavalable'><i class="icon-lang-${lang}"></i><span>${language_name}</span></li>
                                    <li class='unavalable ${_class}'>
                                    % endif
                                        <a tabindex="-1" href="${request.current_route_path(_query=dict(selected_lang=lang))}" onclick="apply_active_anchor($(this)); return true;"><i class="icon-lang-${lang}"></i><span>${language_name}</span></a>
                                        ##<a tabindex="-1" href="${request.route_path('select_language_redirect', selected_lang=lang)}"><i class="icon-lang-${lang}"></i><span>${language_name}</span></a>
                                    </li>
                                % endfor
                                ##<li class="divider"></li>
                                
                                </ul>
                            </li>

                        </ul>
                        
                        <%doc>
                        <ul class="nav pull-right">
                            <li class="dropdown">
                                ##<a href="#" class="dropdown-toggle" data-toggle="dropdown">Language <b class="caret"></b></a>
                                ##<ul class="dropdown-menu" role="menu" aria-labelledby="dLabel">
                            </li>
                        </ul>
                        </%doc>
                    
                        ##<p class="navbar-text pull-right">
                        ##    Logged in as <a href="#" class="navbar-link">Username</a>
                        ##</p>
                        <ul class="nav">
                            <%
                            titlebar = [
                                #('/'          ,'about'     ),
                                ('projects'  ,'projects'  ),
                                ('activities','activities'),
                                ('reference' ,'reference' ),
                                ('units'     ,'teaching units'),
                                ('contact'   ,'contact'   ),
                            ]
                            %>
                            % for route_path, title in titlebar:
                            <% class_active = ' class="active"' if self.titlebar_active==title else '' %>
                            <li${class_active}><a href="${request.route_path(route_path, _query=dict(selected_lang=selected_lang))}">${title.title()}</a></li>
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
            <div class="row">
                ${next.body()}
            </div>
        </div>
        
        <!-- Scripts -->
        <script type="text/javascript" src="/static/site/jquery/jquery-1.8.0.min.js"   ></script>
        <script type="text/javascript" src="/static/site/bootstrap/js/bootstrap.min.js"></script>
        <script type="text/javascript" src="/static/site/prettify/prettify.js"         ></script>
        <script type="text/javascript">
            //<pre class="prettyprint linenums">
            window.prettyPrint && prettyPrint();
        </script>
        <script type="text/javascript" src="/static/site/main.js"                      ></script>

    </body>
    
</html>

<%def name="project_title()">Learn Programming</%def>
