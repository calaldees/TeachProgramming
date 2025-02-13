// https://learn.microsoft.com/en-us/dotnet/framework/network-programming/using-udp-services

// https://stackoverflow.com/a/77632611/3356840
// dotnet run --p StartupObject=UdpNamespace.Udp

using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace UdpNamespace {
public class Udp {
    Udp() {
        Socket sock = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

        // ping host.docker.internal -> 192.168.5.2
        //IPEndPoint addr = new IPEndPoint(IPAddress.Parse("192.168.5.2"), 64488);
        /*
        IPEndPoint addr = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 5005);
        byte[] data = Encoding.ASCII.GetBytes("Hello World!");
        sock.SendTo(data, addr);
        Console.WriteLine($"Bound to {sock.LocalEndPoint}");
        */

        sock.Bind(new IPEndPoint(IPAddress.Any, 5005));
        byte[] buf = new byte[1024];
        while (true) {
            int bytesReceived = sock.Receive(buf);
            String msg = System.Text.Encoding.UTF8.GetString(buf, 0, bytesReceived);
            Console.WriteLine($"received bytes: {msg} from ???");
        }
    }
    public static void Main(string[] args) {new Udp();}
}
} // end namespace