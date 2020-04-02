import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
    limite = 100
    nprimos = 2
    numero = 3
    primos = '1,2,'

    while nprimos < limite:
        vprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                vprimo = 0
                break
        if (vprimo):
            primos = primos + str(numero) + ','
            nprimos += 1
            if (nprimos % 10 == 0):
                primos = primos + '->' + str(nprimos) + '\n'
        numero += 1
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

