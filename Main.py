import sys
import BTCAddress

def main():
	print("main")
	addy = BTCAddress.BTCAddress()
	addy.generate_address("hello")

if __name__ == "__main__":
	main()