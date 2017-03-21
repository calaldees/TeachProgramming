#include <cstdio>

#ifdef __WIN32__

#include <winsock2.h>

#else
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <netdb.h>
#include <io.h>
#endif

const char *HOSTNAME = "localhost";
const int PORT = 7000;

int main() {
	SOCKET socket_fd = socket(AF_INET, SOCK_STREAM, 0);
	if (socket_fd < 0) {
		perror("Socket could not be open\n");
		return 0;
	}

	struct hostent *server = gethostbyname(HOSTNAME);
	if (server == nullptr) {
		perror("Host not found\n");
		return 0;
	}

	struct sockaddr_in serv_addr;
	memset((char *) &serv_addr, sizeof(serv_addr), 0);

	serv_addr.sin_family = AF_INET;
	memcpy(&serv_addr.sin_addr.s_addr, server->h_addr, server->h_length);
	serv_addr.sin_port = htons(PORT);

	if (connect(socket_fd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
		perror("Could not connect\n");
		return 0;
	}

	const char *message = "Im a message\n";
	int write_result;
#ifdef WIN32
	write_result = send(socket_fd, message, sizeof(message), 0);
#else
	write_result = write(socket_fd, message, sizeof(message));
#endif

	if (write_result >= 0) {
		char buffer[256];
		memset(buffer, 256 * sizeof(char), 0);

		int read_result;
#ifdef WIN32
		read_result = recv(socket_fd, buffer, 255, 0);
#else
		read_result = read(socket_fd, buffer, 255);
#endif

		if (read_result >= 0) { // replace with fgets if reading until \n
			printf("Read from socket");
			printf(buffer);
			printf("\n");
		} else {
			perror("Could not read\n");
		}
	} else {
		perror("Could not write\n");
	}

#ifdef WIN32
	closesocket(socket_fd);
#else
	close(socket_fd);
#endif

	return 0;
}
