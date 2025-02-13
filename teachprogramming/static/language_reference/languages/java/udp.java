// Inspired by https://www.baeldung.com/udp-in-java#Client

import java.net.DatagramSocket;     // VER: network_udp_send,network_udp_recv
import java.net.DatagramPacket;     // VER: network_udp_send,network_udp_recv
import java.net.InetSocketAddress;  // VER: network_udp_send,network_udp_recv
import java.net.SocketException;
import java.io.IOException;

// `javac udp.java && java udp`
public class udp {
    public static void main(String[] args) {
try {  // VER: network_udp_send,network_udp_recv
    var sock = new DatagramSocket(null);                     // VER: network_udp_send,network_udp_recv

    var addr = new InetSocketAddress("127.0.0.1", 5005);     // VER: network_udp_send
    byte[] data = "Hello World!".getBytes();                 // VER: network_udp_send
    sock.send(new DatagramPacket(data, data.length, addr));  // VER: network_udp_send
    System.out.println("Bound to: " + sock.getLocalSocketAddress());  // VER: network_udp_send

    //sock.bind(new InetSocketAddress("0.0.0.0", 5005));                      // VER: network_udp_recv
    byte[] buf = new byte[1024];                                          // VER: network_udp_recv
    while (true) {                                                            // VER: network_udp_recv
        DatagramPacket packet = new DatagramPacket(buf, buf.length);          // VER: network_udp_recv
        sock.receive(packet);                                                 // VER: network_udp_recv
        String msg = new String(packet.getData(), 0, packet.getLength());     // VER: network_udp_recv
        System.out.println(String.format(                                     // VER: network_udp_recv
            "received bytes: %s from %s", msg, packet.getSocketAddress()));   // VER: network_udp_recv
        if (msg.isBlank()) {break;}
    } // VER: network_udp_recv
    /*
    UdpClient udp = new UdpClient();
    udp.send("Hello World!");
    System.out.println(udp.recv());
    udp.close();
    */
} catch (Exception e) {System.out.println("Error: " + e.getMessage());}  // VER: network_udp_send,network_udp_recv
    }
}

class UdpClient {
    private final DatagramSocket socket;
    private final InetSocketAddress socket_address;

    public UdpClient() throws SocketException {
        socket = new DatagramSocket();
        socket_address = new InetSocketAddress("localhost", 5005);
        System.out.println("Bound to: "+socket.getLocalSocketAddress());
    }

    public void send(String msg) throws IOException {
        byte[] buf = msg.getBytes();
        DatagramPacket packet = new DatagramPacket(buf, buf.length, socket_address);
        //try {socket.send(packet);} catch (IOException e) {}
        socket.send(packet);
        System.out.println("sent: " + msg);
    }

    public String recv() throws IOException{
        byte[] buf = new byte[1024];
        DatagramPacket packet = new DatagramPacket(buf, buf.length);
        //try {socket.receive(packet);} catch (IOException e) {}
        socket.receive(packet);
        String msg = new String(packet.getData(), 0, packet.getLength());
        return msg;
    }

    public void close() {
        socket.close();
    }
}