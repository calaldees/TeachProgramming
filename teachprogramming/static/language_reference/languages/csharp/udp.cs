// https://learn.microsoft.com/en-us/dotnet/framework/network-programming/using-udp-services

// https://stackoverflow.com/a/77632611/3356840
// dotnet run --p StartupObject=UdpNamespace.Udp

using System;
using System.Net;           // VER: network_udp_send,network_udp_recv
using System.Net.Sockets;   // VER: network_udp_send,network_udp_recv
using System.Text;          // VER: network_udp_send,network_udp_recv
                            // VER: network_udp_send,network_udp_recv
namespace UdpNamespace {
public class Udp {
    Udp() {


Socket sock = new Socket(                                              // VER: network_udp_send,network_udp_recv
    AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);   // VER: network_udp_send,network_udp_recv

// ping host.docker.internal -> 192.168.5.2
//IPEndPoint addr = new IPEndPoint(IPAddress.Parse("192.168.5.2"), 64488);

IPEndPoint addr = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 5005); // VER: network_udp_send
byte[] data = Encoding.ASCII.GetBytes("Hello World!");                // VER: network_udp_send
sock.SendTo(data, addr);                                              // VER: network_udp_send
Console.WriteLine($"Bound to {sock.LocalEndPoint}");                  // VER: network_udp_send

/*
verified with
    docker exec -it e0cdcbd43842 /bin/sh
    nc -u 127.0.0.1 5005
So it's something wrong with udp to the container
*/

//sock.Bind(new IPEndPoint(IPAddress.Any, 5005));        // VER: network_udp_recv
byte[] buf = new byte[1024];                             // VER: network_udp_recv
while (true) {                                           // VER: network_udp_recv
    //Console.WriteLine($"Read {sock.LocalEndPoint}");
    int len = sock.Receive(buf);               // VER: network_udp_recv
    String msg = System.Text.Encoding.UTF8.GetString(buf, 0, len);  // VER: network_udp_recv
    Console.WriteLine($"received bytes: {msg} from ???"); // VER: network_udp_recv
}                                                         // VER: network_udp_recv

    }
    public static void Main(string[] args) {new Udp();}
}
} // end namespace