import java.net.Socket;
import java.io.*;

import java.util.Scanner;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;


public class chat implements ActionListener {
//public class chat {
    
    Socket         network_socket = null;
    BufferedWriter network_writer = null;
    BufferedReader network_reader = null;
    
    Scanner console = new Scanner(System.in);
    
    JTextField text_field;
    JTextArea  text_area;
    
    public void connect(String host, int port) {
        try {
            network_socket = new Socket(host, port);
            network_writer = new BufferedWriter(new OutputStreamWriter( network_socket.getOutputStream() ));
            network_reader = new BufferedReader(new InputStreamReader(  network_socket.getInputStream()  )); 
            new ReciveThread(this);
        }
        catch (Exception e) {}
    }
    
    public void disconnect() {
        try {
            network_writer.flush();
            network_writer.close();
            network_reader.close();
            network_socket.close();
        }
        catch (Exception e) {}//e.printStackTrace();}
    }
    
    public boolean send(String msg) {
        try {
            network_writer.write(msg);
            network_writer.write("\n");
            network_writer.flush();
            return true;
        } 
        catch (Exception e) {
            return false;
        }
    }
    
    public void receive(String msg) {
        //System.out.println(msg);
        text_area.append(msg + "\n");
        text_area.setCaretPosition(text_area.getDocument().getLength());
    }
    
    public void actionPerformed(ActionEvent event) {
        send(text_field.getText());
        text_field.setText("");
    }
    
    public chat(String host, int port) {
        JFrame frame = new JFrame("Chat Client");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        text_field = new JTextField();
        text_field.addActionListener(this);
        frame.add(text_field,BorderLayout.SOUTH);
        
        text_area = new JTextArea();
        text_area.setEditable(false);
        text_area.setLineWrap(true);
        //frame.add(text_area,BorderLayout.CENTER);
        JScrollPane scroll = new JScrollPane(text_area, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
        frame.add(scroll,BorderLayout.CENTER);
        
        frame.pack();
        frame.setVisible(true);
        
        connect(host,port);
        //send("HelloWorld");
        while (network_socket.isConnected()) {
            send(console.nextLine());
        }
    }

    public static void main(String[] args) {new chat("localhost", 9872);}
}


class ReciveThread extends Thread {

    private final chat c;
  
    public ReciveThread(chat c) {
        super();
        this.c = c;
        start();
    }

    public void run() {
        while (c.network_socket.isConnected()) {
            try                 {c.receive(c.network_reader.readLine());}
            catch (Exception e) {c.disconnect();}
            try                 {sleep(0);}
            catch (Exception e) {}
        }
    }
}
