from block import Block
from chain import Chain

from flask import Flask, request
import requests
import json

app = Flask(__name__)
theChain = Chain()

@app.route('/chain', methods=['GET'])
def getChain():
    data = []
    for block in theChain.chain:
        data.append(block.__dict__)
    return json.dumps({"Length": len(data), "Chain": data})

app.run(debug=True, port=5000)