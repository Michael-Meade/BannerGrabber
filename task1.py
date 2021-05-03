import socket
import optparse
class BannerGrab:
	# the class needs to have IP and port arguments
	def __init__(self, ip, port):
		self.ip   = ip
		self.port = port

	def get_banner(self):
		s = socket.socket()
		s.connect((self.ip, self.port))
		# gets the first 1024 bytes 
		banner = s.recv(1024)
		return banner

def main():
	parser = optparse.OptionParser("usage: python3 bannergrab.py -H <host> -P <port")
	parser.add_option("-H", dest='ip', type="string", help="IP")
	parser.add_option("-P", dest="p", type=int, help="port")
	(options, args) = parser.parse_args()
	# creates strings with the values of the input
	ip   = options.ip
	port = options.p
	# checks to make sure they are not empty
	if (ip == None) | (port == None):
		print(parser.usage)
		exit(0)

	# run the banner grabber code
	a = BannerGrab(ip, port)
	print(a.get_banner())




