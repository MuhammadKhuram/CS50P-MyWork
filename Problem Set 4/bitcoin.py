import requests
import sys
import json


def main():

    while True:
        try:
            if isinstance(float(sys.argv[1]), float):
                response = requests.get(
                    "https://rest.coincap.io/v3/assets/bitcoin?apiKey=1973e1e54ccc2be349c14b6f09c18e09b414150849ca27f49046d9c71010ec5e")
                price = float(response.json()["data"]["priceUsd"])
                total = price * float(sys.argv[1])
                print(f"${total:,.4f}")
                break

        except IndexError:
            sys.exit("Missing command-line argument")

        except ValueError:
            sys.exit("Command-line argument is not a number")


main()
