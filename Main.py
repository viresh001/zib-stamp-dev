import sys
import BTCAddress

def main():
    print("main")
    addy = BTCAddress.BTCAddress()
    addy.generate_address("hello")

    addy2 = BTCAddress.BTCAddress()
    addy2.generate_address("world")

if __name__ == "__main__":
	main()