import requests
import json

start_block = 6324000
end_block = 6410400
pageIndex = 1
transactions = []
contract = "cx353599f61f3b14373658958d79fbbe5001533a00"
running = True

while running:
    print("Loading page %d ..." % pageIndex)
    url = "https://tracker.icon.foundation/v3/contract/txList?page=%d&count=100&addr=%s" % (pageIndex, contract)

    page = json.loads(requests.get(url).text)

    if not page["data"]:
        print("No more data")
        break

    # Add the transactions
    for tx in page["data"]:
        height = int(tx['height'])

        # Check if the block height is in event time bound
        if start_block < height < end_block:
            transactions.append(tx['txHash'])

        if height < start_block:
            # We reached the end of the event, stop saving
            running = False
            break

    pageIndex += 1

print("Saving database ...")
open("transactions.json", "w+").write(json.dumps(transactions))
