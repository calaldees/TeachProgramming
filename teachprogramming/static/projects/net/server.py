#!/usr/bin/env python

import re
import hashlib, base64
import threading, time


# Python 2.x compatability
try:
    import socketserver
except ImportError as e:
    import SocketServer as socketserver


# Constants---------------------------------------------------------------------
__version__ = 0.1
recv_size   = 4096

log_params = {}
def log(catagory, msg):
    if log_params[catagory]:
        print(msg.strip())

# Binary Helpers ---------------------------------------------------------------

def ByteToHex( byteStr ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    return ''.join( [ "%02X " % x for x in byteStr ] ).strip() #ord( x )

def get_bit(number, bit):
    """
    The bit patern for the number 4 is '00000100'
    The third bit is True
    
    >>> get_bit(4,1)
    False
    >>> get_bit(4,2)
    False
    >>> get_bit(4,3)
    True
    >>> get_bit(4,4)
    False
    """
    return number &  pow(2,bit-1) != 0


# WebSocket --------------------------------------------------------------------

OPCODE_CONTINUATION =  0
OPCODE_TEXT         =  1
OPCODE_BINARY       =  2
OPCODE_CLOSE        =  8
OPCODE_PING         =  9
OPCODE_PONG         = 10

WEBSOCKET_HANDSHAKE_HYBI10 = """HTTP/1.1 101 Switching Protocols\r
Upgrade: websocket\r
Connection: Upgrade\r
Sec-WebSocket-Accept: %(websocket_accept)s\r\n\r\n"""

# HYBI10 ----

def websocket_frame_decode_hybi10(data):
    """
    http://tools.ietf.org/html/rfc6455#section-5.2
    """
    # Convert data to python 'int's to use bitwise operators
    data = [ord(i) for i in data]
    
    # Extract control bits
    fin            = get_bit(data[0], 8)
    opcode         = data[0] % pow(2,4)
    masked         = get_bit(data[1], 8)
    payload_length = data[1] % pow(2,7)
    #print ("fin:%s opcode:%s masked:%s payload_length:%s" % (fin, opcode, masked, payload_length))
    
    if not fin:
        raise Exception('unsuported fragmented frames')
    
    # Payload Length
    data_start_point = 2
    if   payload_length == 126:
        extended_payload_length = 2
        data_start_point += extended_payload_length
        raise Exception('unsuported payload length')
    elif payload_length == 127:
        extended_payload_length = 8
        data_start_point += extended_payload_length
        raise Exception('unsuported payload length')
    
    # Mask
    masking_key = [0,0,0,0]
    if masked:
        masking_key = data[data_start_point:data_start_point+4]
        data_start_point += 4
    
    # Convert payload_data to python type
    data_convert_function = chr #lambda i: i # AllanC - close frames can have data in, int's cant be concatinated with b''.join ... humm
    if opcode == OPCODE_TEXT:
        data_convert_function = chr
    if opcode == OPCODE_BINARY:
        #raise Exception('untested binary characters')
        pass
    
    payload_data = b''.join([data_convert_function(item^masking_key[index%4]) for index, item in enumerate(data[data_start_point:])])
    
    return payload_data, opcode


def websocket_frame_encode_hybi10(data, opcode=OPCODE_TEXT, fin=True, masked=False):
    if not fin:
        raise Exception('unsuported fragmented frames')
    
    # Create control byte
    control = int(fin) << 7 | opcode #'\x81'
    
    # Create payload_length and extended_payload_length bytes
    payload_length = len(data)
    if payload_length > 65535:
        payload_length = 127
        raise Exception('unsuported payload length')
    elif payload_length > 125:
        payload_length = 126
        raise Exception('unsuported payload length')
    payload_length = int(masked) << 7 | payload_length 
    
    # Create mask bytes
    if masked:
        raise Exception('unsuported masked')
    
    return chr(control) + chr(payload_length) + data

# HYBI00 ----

WEBSOCKET_HANDSHAKE_HYBI00 = """HTTP/1.1 101 Web Socket Protocol Handshake\r
Upgrade: WebSocket\r
Connection: Upgrade\r
WebSocket-Origin: %(origin)s\r
WebSocket-Location: %(location)s\r
WebSocket-Protocol: sample\r\n\r\n"""

#GET /demo HTTP/1.1
#Upgrade: WebSocket
#Connection: Upgrade
#Host: example.com
#Origin: http://example.com
#WebSocket-Protocol: sample

#HTTP/1.1 101 Web Socket Protocol Handshake
#Upgrade: WebSocket
#Connection: Upgrade
#WebSocket-Origin: http://example.com
#WebSocket-Location: ws://example.com/demo
#WebSocket-Protocol: sample

def websocket_frame_decode_hybi00(data):
    return data, OPCODE_TEXT
    
def websocket_frame_encode_hybi00(data):
    return '\x00' + data + '\xff'


# Connection Handlers ----------------------------------------------------------

clients = {'websocket':[],'tcp':[],'udp':[]}

def clients_send(data, source=None):
    """
    Send the data to all known clients
    """
    
    log('message', '%s:%s '%source + data)
    
    def send(client, data):
        try   : client.request.send(data)
        except: print('error echoing to client %s:%s'%client.client_address)
    
    #websocket_data_frame_hybi00 = websocket_frame_encode_hybi00(data) # AllanC - could preprocess data frames here ... but thats an optimisation for later
    #websocket_data_frame_hybi10 = websocket_frame_encode_hybi10(data)
    for websocket_client in clients['websocket']:
        send(websocket_client, websocket_client.frame_encode_func(data))
        
    for tcp_client in clients['tcp']:
        send(tcp_client, data)
    
    for udp_client in clients['udp']:
        pass
    


class WebSocketEchoRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        websocket_request = str(self.request.recv(recv_size))
        
        # HyBi 10 handshake
        if 'Sec-WebSocket-Key' in websocket_request:
            websocket_key     = re.search(r'Sec-WebSocket-Key:\s?(.*)', websocket_request).group(1).strip()
            websocket_accept  = base64.b64encode(hashlib.sha1(('%s%s'%(websocket_key ,'258EAFA5-E914-47DA-95CA-C5AB0DC85B11')).encode('utf-8')).digest()).decode('utf-8')
            handshake_return  = (WEBSOCKET_HANDSHAKE_HYBI10 % {'websocket_accept':websocket_accept}).encode('utf-8')
            self.frame_encode_func = websocket_frame_encode_hybi10
            self.frame_decode_func = websocket_frame_decode_hybi10
        
        # HyBi 00 handshake
        elif False:
            print(websocket_request)
            header_match = re.search(r'GET (?P<location>.*?) HTTP.*Origin:\s?(?P<origin>.*?)\s', websocket_request, flags=re.MULTILINE)
            print(header_match.groupdict())
            handshake_return  = (WEBSOCKET_HANDSHAKE_HYBI00 % {'origin':'TEMP', 'location':'TEMP'}).encode('utf-8')
            self.frame_encode_func = websocket_frame_encode_hybi00
            self.frame_decode_func = websocket_frame_decode_hybi00
        
        self.request.send(handshake_return)
        #print(handshake_return)
        clients['websocket'].append(self)
        log('connection','%s:%s connected' % self.client_address)
    
    def handle(self):
        while True:
            time.sleep(0)
            data_recv = self.request.recv(recv_size)
            
            if not data_recv:
                continue
            
            data, opcode = self.frame_decode_func(data_recv)
            if opcode == OPCODE_TEXT:
                clients_send(data, self.client_address)
            elif opcode == OPCODE_CLOSE:
                self.request.send(self.frame_encode_func(data, opcode=OPCODE_CLOSE))
                break
            elif opcode == OPCODE_PING:
                self.request.send(self.frame_encode_func(data, opcode=OPCODE_PONG ))

    def finish(self):
        clients['websocket'].remove(self)
        log('connection','%s:%s disconnected' % self.client_address)


class TCPEchoRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        clients['tcp'].append(self)
        log('connection','%s:%s connected' % self.client_address)
    
    def handle(self):
        while True:
            data = self.request.recv(recv_size)
            
            if not data:
                #self.request.close()
                break
                
            clients_send(data, self.client_address)
                
            #time.sleep(0)
    
    def finish(self):
        #self.request.send('bye ' + str(self.client_address) + '\n')
        clients['tcp'].remove(self)
        log('connection','%s:%s disconnected' % self.client_address)


class UDPEchoRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # TODO - clients need to register with the UDP handler
        data = self.request[0].strip()
        socket = self.request[1]
        #log('message',"{} wrote:".format(self.client_address[0]))
        #log('message',data)
        client_send(data, self.client_address)
        socket.sendto(data.upper(), self.client_address)



# Threaded Servers -------------------------------------------------------------

servers = []
def start_server(server):
    server.allow_reuse_address = True
    server_thread = threading.Thread(target=server.serve_forever) 
    server_thread.daemon = True # Exit the server thread when the main thread terminates
    server_thread.start() # Start a thread with the server -- that thread will then start one more thread for each request
    servers.append(server)
    #print("Server loop running in thread:", server_thread.name)

def stop_servers():
    for server in servers:
        #server.shutdown()
        server.server_close()

# Command Line Arguments -------------------------------------------------------

def bool_(value):
    value = value.lower()
    for t in ['yes', 'true','y']:
        if t in value:
            return True
    return False


def get_args():
    import argparse
    parser = argparse.ArgumentParser(
        prog        = "EchoMultiServe",
        description = "Lightweight Echo server for UDP, TCP and WebSockets",
        epilog      = "@calaldees"
    )
    parser.add_argument('--version', action='version', version="%.2f"%__version__)
    parser.add_argument('-s','--serve', nargs='+', choices=['udp', 'tcp', 'websocket'], metavar='SERVER_TYPE', default=['udp','tcp','websocket'])
    parser.add_argument('-u','--udp_port'      , type=int, help='UDP port'      , default=9871)
    parser.add_argument('-t','--tcp_port'      , type=int, help='TCP port'      , default=9872)
    parser.add_argument('-w','--websocket_port', type=int, help='WebSocket port', default=9873)
    parser.add_argument(     '--show_status'     , type=bool_, default=True , help='Display status')
    parser.add_argument('-c','--show_connections', type=bool_, default=True , help='Display connections')
    parser.add_argument('-m','--show_messages'   , type=bool_, default=False, help='Display messages recived')
    return parser.parse_args()

# Main -------------------------------------------------------------------------

if __name__ == "__main__":
    args = get_args()
    log_params['status'    ] = args.show_status
    log_params['message'   ] = args.show_messages
    log_params['connection'] = args.show_connections
    for server_type in args.serve:
        if server_type=='websocket':
            start_server(socketserver.ThreadingTCPServer(('', args.websocket_port), WebSocketEchoRequestHandler))
            log('status','WebSocket Server on %d' % args.websocket_port)
        if server_type=='tcp':
            start_server(socketserver.ThreadingTCPServer(('', args.tcp_port      ), TCPEchoRequestHandler      ))
            log('status','TCP Server on %d' % args.tcp_port)
        if server_type=='udp':
            start_server(socketserver.UDPServer         (('', args.udp_port      ), UDPEchoRequestHandler      ))
            log('status','UDP Server on %d' % args.udp_port)
    
    ip = []    
    #import socket
    #ip = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
    try:
        # sudo apt-get install python-netifaces
        from netifaces import interfaces, ifaddresses, AF_INET    
        for ifaceName in interfaces():
            ip += [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':''}] )]
            #print '%s: %s' % (ifaceName, ', '.join(addresses))
    except:
        pass

    log('status','Server Running on %s' % (ip))
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt as e:
        pass
    stop_servers()
    print("")

#-------------------------------------------------------------------------------
# Working
#-------------------------------------------------------------------------------

"""

import time

# Handle Connection
def connection(client):
    websocket_request = client.recv(4096)
    websocket_key     = re.search(r'Sec-WebSocket-Key:\s?(.*)', websocket_request).group(1).strip()
    websocket_accept  = base64.b64encode(hashlib.sha1('%s%s' % (websocket_key ,'258EAFA5-E914-47DA-95CA-C5AB0DC85B11')).digest())
    client.send(handshake % {'websocket_accept':websocket_accept})
    
    while True:
        data_recv = client.recv(4096)
        
        data, opcode = decode_frame(data_recv)
        if opcode == OPCODE_TEXT:
            #msg_send.append(data)
            print(data)
            client.send(encode_frame(data))
        elif opcode == OPCODE_CLOSE:
            break
        elif opcode == OPCODE_PING:
            client.send(encode_frame('pong', opcode=OPCODE_PONG))
        
        time.sleep(0)
    
    client.close()

# Setup Server Socket

import socket, threading
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', port))
sock.listen(5)

print "TCPServer Waiting for clients on port %d" % port
while True:
    client, address = sock.accept()
    threading.Thread(target=connection, args=(client,)).start()
"""
#server = SocketServer.ThreadingTCPServer(('', port), WebSocketEchoRequestHandler)
#server.serve_forever()

