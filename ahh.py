from block import Block
from chain import Chain

from flask import Flask, request
import requests
import simplejson as json

app = Flask(__name__)
chain = Chain()

@app.route('/chain', methods=['GET'])
def getChain():
    data = []
    for block in Chain.chain:
        data.append(block.__dict__)
    return json.dumps({"Length": len(data), "Chain": data})

app.run(debug=True, port=8080)