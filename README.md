# Blockchair API Dogecoin Address Balance Extractor

## Background

This Python script imports Dogecoin addresses from a `.csv` file generated via [`dumpwallet`](https://bitcoincore.org/en/doc/0.16.0/rpc/wallet/dumpwallet/) and utilizes [Blockchair's API](https://blockchair.com/api) to export the address balances (and other stats) to a `.txt` file.

## Dependencies
- Python (obviously) and the Python modules imported in `lines 1-3`
- A `.csv` file exported from that contains the data generated from [`dumpwallet`](https://bitcoincore.org/en/doc/0.16.0/rpc/wallet/dumpwallet/)

## Usage
1. Place your `.csv` file within the same directory as `blockapi.py`
2. Rename your `.csv` file to `addresses.csv`
3. Remove all beginning data in the `addresses.csv` to ensure ONLY the address data is included
a. AKA your first line should look like: `QRnA5dfgrWLaSohFeUpEKb9j3uyX1aDXN93zxEzm8esVn4fd5NoE,2016-11-06T08:25:40Z,change=1,#,addr=D5HNvX9sXcMw3a4H7Abvi121Te1BBdNa1d,` (this is a dummy private key so go ahead and try to steal it)
4. Run the Python script: `python3 blockapi.py`
