<%inherit file="_project.mako"/>

<%def name="init()">
<%
    vername = {
        'base1'          :'1',
        'background'     :'1,background',
        'copter'         :'1,background,copter',
        'colision_single':'1,background,copter,colision_single',
        'colision_multi' :'1,background,copter,colision_single,colision_multi',
        'level'          :'1,background,copter,colision_single,level',
        'physics'        :'1,background,copter,physics',
        'paralax'        :'1,background,paralax',
        'full'           :'1,background,copter,physics,colision_single,colision_multi,paralax',
    }
    self.vername = vername
    
    code_sections = [
        dict(title='Base'                 , category='Base Compoents', heading_level=2, prev_version=None                      , target_version=vername[          'base1']),
        dict(title='Background'           , category='Base Compoents', heading_level=2, prev_version=vername[          'base1'], target_version=vername[     'background']),
        dict(title='Copter'               , category='Base Compoents', heading_level=2, prev_version=vername[     'background'], target_version=vername[         'copter']),
        dict(title='Colide (Single Point)', category='Base Compoents', heading_level=2, prev_version=vername[         'copter'], target_version=vername['colision_single']),
        dict(title='Level advancing'      , category='Choices'       , heading_level=2, prev_version=vername['colision_single'], target_version=vername[          'level']),
        dict(title='Physics'              , category='Choices'       , heading_level=2, prev_version=vername[         'copter'], target_version=vername[        'physics']),
        dict(title='Paralax'              , category='Advanced'      , heading_level=2, prev_version=vername[     'background'], target_version=vername[        'paralax']),
        dict(title='Colide (Multi Point)' , category='Advanced'      , heading_level=2, prev_version=vername['colision_single'], target_version=vername[ 'colision_multi']),
    ]
    self.code_sections = code_sections

%>
</%def>



<h1>Copter</h1>
demo
${parent.web_demo(self.vername['full'])}

% for code_section in self.code_sections:
    <%self:code_section
        prev_version   = "${code_section[  'prev_version']}"
        target_version = "${code_section['target_version']}"
        title          = "${code_section[         'title']}"
        heading_level  = "${code_section[ 'heading_level']}"
    ></%self:code_section>
% endfor


##<img src="/static/projects/images/CopterLevel1.gif">