import sys
import BTCAddress

def main():
    print("main")
    addy = BTCAddress.BTCAddress()
    addy.generate_address("hello")

    addy2 = BTCAddress.BTCAddress()
    addy2.generate_address("world")

    addy3 = BTCAddress.BTCAddress()
    addy3.generate_address("viresh")

if __name__ == "__main__":
	main()