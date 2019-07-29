import json
import sys

lucky = int(sys.argv[1])

results = json.loads(open("results.json", "r").read())

send_bombs = []
for txHash in results:
    tx = results[txHash]
    if tx['method'] == 'send_bomb':
        send_bombs.append(tx)

print('The winner is ... *drum rolls* ...')
print(" >> " + send_bombs[lucky]['from'] + " << ")
print("Congratulations !")
print("\nFull transaction information:")
print(json.dumps(send_bombs[lucky], indent=4))
