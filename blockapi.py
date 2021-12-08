import requests
import json
import csv

# Opens/imports a walletdump CSV file exported from Dogecoin-qt.exe
temp = open('addresses.csv')
addresses_csv = csv.reader(temp)

# Iterates through each row in the CSV file
for row in addresses_csv:

    # Pulls out the raw Dogecoin addresses - Change the interger as needed if your .csv is different
    addressloop = row[4].replace('addr=', '')

    # Prints the raw Dogecoin address for debugging
    print("Pulling data for " + addressloop)

    # Initiates an API request to blockchair with the Dogecoin address
    response = requests.get('https://api.blockchair.com/dogecoin/dashboards/address/'+addressloop)

    # Formats the response into JSON
    jsonresponse = response.json()

    # Prints out select content (wallet address, balance, etc) from the request
    filteredjsonresponse = jsonresponse["data"][addressloop]["address"]
    # Writes filtered content in step above to an output file
    with open('response.txt', 'a') as outfile:
        outfile.write(addressloop+"\n")
        outfile.write(str(filteredjsonresponse)+"\n \n")
