<%inherit file="_project.mako"/>


<%def name="init()">
<%
    self.titlebar_active        = 'projects'
    self.text_title             = 'Chat'
    self.text_title_description = 'Send messages to the other side of the planet (or just the person across the room)'

%>
</%def>

## ----------------------------------------------
<% self.section_title('Setup') %>
    <h2>Setup</h2>
    <p>Explanation of IP adress</p>
    <p>Download <a href="/static/projects/net/server.py">server.py</a> (only in python, quite compicated, if you think this is discraceful then build up some code kung fu and submit additional server implementations on github)</p>
    <p>start the server - examples</p>
    <p>replace localhost with server address</p>
    <p><a href="#">Lesson Plan</a> for teachers</p>
</section>

##python3 ~/code/TeachProgramming/teachprogramming/lib/make_ver.py chat.html --target_ver_name 1,send_one,send,recv,send_recv,gui,gui_recv,gui_scroll,gui_username > t.html

## ----------------------------------------------
<% self.category = 'Console Interface' %>

<%self:code_section
    prev_ver_name   = ""
    target_ver_name = "base"
    title          = "Base"
>
    <%def name="before_code_py()">
        <p>Create a file called chat.py</p>
    </%def>

    <%def name="before_code_html()">
        <p>Create a file called chat.html</p>
    </%def>
    <%def name="after_code_html()">
        <p>Open chat.html in firefox</p>
        <p>Reload the page each addition by pressing CTRL+F5</p>
    </%def>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "base"
    target_ver_name = "connect"
    title          = "Connect"
>
    <%def name="before_code_py()">
        <p>Replace localhost with the servers IP address example: 192.168.0.1</p>
    </%def>
    
    <%def name="before_code_html()">
        <p>Replace localhost with the servers IP address example: ws://192.168.0.1:9873/</p>
    </%def>
    <%def name="after_code()">
        <p>Look at the server to see if your IP address connected</p>
    </%def>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "connect"
    target_ver_name = "send_one"
    title          = "Connect + send one message"
>
    <%def name="after_code()">
        <p>Look at the server to see if it received your message</p>
    </%def>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "send_one"
    target_ver_name = "send"
    title          = "Send messages"
>
    <%def name="before_code_py()">
        <p>Press CTRL+C to exit</p>
    </%def>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "send"
    target_ver_name = "recv"
    title          = "Receive messages"
>
    <%def name="before_code_html()">
        <p>Tools->Web Developer->Web Console</p>
    </%def>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "recv"
    target_ver_name = "send_recv"
    title          = "Send and Recice messages"
>
</%self:code_section>


## ----------------------------------------------
<% self.category = 'Graphical User Interface' %>


<%self:code_section
    prev_ver_name   = "send_recv"
    target_ver_name = "gui"
    title          = "GUI"
>
</%self:code_section>

<%self:code_section
    prev_ver_name   = "gui"
    target_ver_name = "gui_recv"
    title          = "GUI Receve"
>
</%self:code_section>


<%self:code_section
    prev_ver_name   = "gui_recv"
    target_ver_name = "gui_scroll"
    title          = "GUI Receve (Scrolling)"
>
</%self:code_section>

<%self:code_section
    prev_ver_name   = "gui_scroll"
    target_ver_name = "gui_username"
    title          = "GUI with Username"
>
</%self:code_section>


## Old Java Worksheet ----------------------------------------------------------

<%doc>

<h2>Part 0: Setup</h2>
Before we Begin
Install Java
Copy needed “Network Connection” files
Know how to compile java files


<h2>Part 1: Simple Messages</h2>


<h3>Connecting to a server</h3>
Create a new .java file based on the code below

<pre>
import GameLib.Net.AbstractNetworkConnection;

public class ????? extends AbstractNetworkConnection {

    public ?????() {
        networkConnect("?network address?");
    }
  
    public static void main(String[] args) {new ????();}
}
</pre>
<p>Note: ???? must be the name of the file (CASE SENSETIVE) e.g if your file is called “ChatClient.java” ????? would be “ChatClient”</p>
<p>Run this code and try to connect to someone’s server. You should see on the servers screen a message that you connected.</p>
<p>(To find your IP address type “ifconfig” in Linux or “ipconfig” in Windows)</p>
<p>(To run a server type “java GameLib/GameServer show_messages”)</p>
<p>Press Ctrl-C to exit</p>


<h3>Sending A “hello” message to the server</h3>
<pre>
public class ?????? extends AbstractNetworkConnection {

    public ?????() {
        networkConnect("?network address?");
        networkSend("Hello everyone! Mr.T has connected");
    }

    public static void main(String[] args) {new ????();}
}
</pre>

<p>Adding this line will send a message when you first connect. You can see it on the server screen</p>
<p>BUT! We haven’t written code to SEE messages ….</p>

<h3>Receiving messages and displaying them</h3>

<pre>
    public void networkRecieve(String message) {
        System.out.println(message);
    }
  
    public static void main(String[] args) {new ????();}
</pre>
<p>THINK! Where would you put this code? Look at the indentation.</p>
<p>NOW! With your friends try connecting and disconnecting and try to see each others connect message.</p>

<h3>Text input</h3>
<p>TODO: use console input to send messages</p>


<h2>Part 2: Creating a GUI to type in</h2>

<p>Creating a TextField Box</p>
<p>We need a GUI (Graphical User Interface) to type messages into.</p>
<p>We need to IMPORT Java objects to make our interface</p>

<pre>
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
</pre>

<p>Put this code at the very beginning of your file</p>
<p>Before you networkConnect setup a Java Frame (JFrame) and Java TextField (JTextField)</p>

<pre>
  private JTextField text_field;

  public ?????() {
    JFrame frame = new JFrame("Martins Mega Chat Client");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    text_field = new JTextField();
    frame.add(text_field,BorderLayout.SOUTH);
    
    frame.pack();
    frame.setVisible(true);
    
    networkConnect("?network address?");
    networkSend("Hello everyone! Mr.T has connected");
  }
</pre>
<p>You should see a box pop up! Good work!</p>
<p>But it doesn’t work. Why?</p>
<p>Creating a Listener for our JTextField</p>
<pre>
public class ChatClient extends AbstractNetworkConnection implements ActionListener {
…
    text_field = new JTextField();
    text_field.addActionListener(this);
    frame.add(text_field,BorderLayout.SOUTH);
…
  public void actionPerformed(ActionEvent event) {
    networkSend(text_field.getText());
  }
</pre>

<p>Use the code to make the JTextField send a message when you press enter.</p>
<p>BUT! What is wrong? (It doesn’t work like we want, why?)</p>
<h3>Resetting the JTextField</h3>
<p>Can you fix the bug but using the Java API (Application Programming Interface)</p>
<p>Google for “Java API”</p>
<p>Find the documentation for JTextField</p>
<p>Find the command to use, remember you want to “set the text in the box to nothing”</p>

<pre>
  public void actionPerformed(ActionEvent event) {
    networkSend( text_field.getText() );
    text_field.????;
  }
</pre>

<h2>Part 3: Creating a GUI to view received messages</h2>
<p>Creating a JTextArea box</p>

<pre>
  private JTextField text_field;  
  private JTextArea  text_area;

  public ?????() {
    JFrame frame = new JFrame("Martins Mega Chat Client");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    text_field = new JTextField();
    frame.add(text_field,BorderLayout.SOUTH);

    text_area = new JTextArea();
    frame.add(text_area,BorderLayout.CENTER);
    
    frame.pack();
…
</pre>

<p>Run it and resize your chat window and check your JTextArea is there (it will be plain white)</p>
<p>Receiving messages to the JTextArea</p>
<pre>
  public void networkRecieve(String message) {
    text_area.append(message + "\n");
  }
</pre>
<p>Check your program receives messages</p>
<p>BUT! What is wrong? (It doesn’t work like we want, why?)</p>

<h3>Scrolling the JTextArea</h3>
<pre>
…
    text_area = new JTextArea();
    JScrollPane scroll = new JScrollPane(text_area, 
                                         JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
                                         JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
    frame.add(scroll,BorderLayout.CENTER);
    
    frame.pack();
…
</pre>

<h2>Final Bugs</h2>
<p>There are a few more bugs to squash (use the “reference”/”useful code” section below)</p>
<ol>
    <li>We can type over the received messages area</li>
    <li>We want lines to wrap to the next line if they are too long</li>
    <li>When a message is received we always want it scrolled to the bottom</li>
</ol>
<p>Look at the next Reference section. Can you fix the bugs?</p>

<h2>Challenges</h2>
<p>See the reference section below + teacher for hints</p>
<ol>
    <li>Extreme Challenge: can you get it to connect to servers by "java ChatClient 192.168.0.12" </li>
    <li>Can you make it so it puts your name in front of every message that you type?</li>
    <li>Ultimate Challenge: can you make it "java ChatClient 192.168.0.12 Ninja" (where Ninja the name it will print before each line)</li>
    <li>Think: What could be done to improve this system if it was going to be used for real?</li>
</ol>


<h2>Reference</h2>
<h3>Useful code</h3>
<pre>
text_area.setEditable(false);
text_area.setLineWrap(true);

text_field.setText("");

text_area.setCaretPosition(text_area.getDocument().getLength());
<pre>

<h3>Network Connection Methods Reference</h3>
Method
Type
Description
networkConnect(String)


networkDisconnect()


networkSend(Object)


networkIsConnected()


public void networkRecieve(String message) {
You write it

public void networkConnected() {
You write it

public void networkDisconnecting() {
You write it


<h3>Extreme Challenge Help</h3>
<pre>
…
  public ChatClient(String server_address) {
…
    networkConnect(?);
  }
…
  public static void main(String[] args) {
    new ChatClient(args[0]);
  }
…
</pre>

<h3>Ultimate Challenge Help</h3>
<pre>
  private String username;
…
  public ChatClient(String server_address, String new_username) {
    username = new_username;
…
    networkConnect(?);
  }
…
    networkSend(username + ": " + text_field.getText());
…
  public static void main(String[] args) {
    new ChatClient(args[0],args[1]);
  }
…
</pre>


</%doc>