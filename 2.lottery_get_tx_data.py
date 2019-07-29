from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
import json

print("Loading transactions ...")
transactions = json.loads(open("transactions.json", "r").read())

# Creates an IconService instance using the HTTP provider and set a provider.
icon_service = IconService(HTTPProvider("https://wallet.icon.foundation", 3))

results = json.loads(open("results.json", "r+").read())

for index, txHash in enumerate(transactions):

    print("%d / %d ..." % (index, len(transactions)))
    if txHash in results:
        print("%s already present" % txHash)
        continue

    tx_result = icon_service.get_transaction(txHash)

    if tx_result['dataType'] and tx_result['dataType'] == 'call':
        results[txHash] = {
            'from': tx_result['from'],
            'timestamp': tx_result['timestamp'],
            'txHash': tx_result['txHash'],
            'blockHeight': tx_result['blockHeight'],
            'method': tx_result['data']['method']
        }
        open("results.json", "w+").write(json.dumps(results))

print("Saving database ...")
open("results.json", "w+").write(json.dumps(results))
