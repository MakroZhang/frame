import socket
import struct

def socket_connect():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("", 20083)
    tcp_server_socket.bind(addr)
    tcp_server_socket.listen(8)
    client_socket, client_addr = tcp_server_socket.accept()
    req = struct.pack('8B', int('3F', 16), int('20', 16), int('63',16), int('31',16), int('0D',16), int('0A',16), int('0D',16), int('0A',16))
    print(req)
    client_socket.sendll(req)
    
    client_socket.close()

def to_hex(byte):
    return int(byte, 16)

def pack_hex(hex_string):
    byte_string = ''
    hex_stream = b''
    while hex_string:
        byte_string = hex_string[0:2]
        s = to_hex(byte_string)
        hex_stream += struct.pack('B', s)
        hex_string = hex_string[2:]
    return hex_stream

def read_frame(data, file_path):
    for line in open(file_path, "r"):
        data.append(line)



if __name__ == "__main__":
    socket_connect()
