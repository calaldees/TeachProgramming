import java.net.Socket;
import java.io.*;
/*
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;
*/
//

public class chat {
    
    Socket         network_socket = null;
    BufferedWriter network_writer = null; //BufferedWriter
    DataInputStream  network_reader = null; //BufferedReader
    
    public static void main(String[] args) {new chat("localhost", 9872);}
    
    public chat(String host, int port) {
        connect(host,port);
        send("HelloWorld");
    }

    public void connect(String host, int port) {
        try {
            network_socket = new Socket(host, port);
            network_writer = new BufferedWriter(new OutputStreamWriter( network_socket.getOutputStream() )); // new DataOutputStream( 
            network_reader = new DataInputStream(  network_socket.getInputStream()  ); //new BufferedReader(new InputStreamReader( 
            new ReciveThread(this);
        }
        catch (Exception e) {}
    }
    
    public void disconnect() {
        try {network_writer.flush(); network_writer.close(); network_writer=null;} catch (Exception e) {}//e.printStackTrace();}
        try {                        network_reader.close(); network_reader=null;} catch (Exception e) {}//e.printStackTrace();}
        try {                        network_socket.close(); network_socket=null;} catch (Exception e) {}//e.printStackTrace();}
    }
    
    public boolean send(String msg) {
        try                 {network_writer.write(msg); network_writer.flush(); return true; } 
        catch (Exception e) {                           return false;}
    }
    
    public void receive(String msg) {
        System.out.println(msg);
    }
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
            try {
                //int bytes_avalable = c.network_reader.available();
                //if (bytes_avalable>0) {
                //    byte[] b = new byte[bytes_avalable];
                //    c.network_reader.read(b);
                //    c.network_reader.skipBytes(bytes_avalable);
                //    System.out.println(new String(b));
                //}
                System.out.println(c.network_reader.read());
            }
            catch (Exception e) {}
            //try                 {c.receive(c.network_reader.readLine());}
            //catch (Exception e) {c.disconnect();}
            //try                 {sleep(0);}
            //catch (Exception e) {}
        }
    }
}
