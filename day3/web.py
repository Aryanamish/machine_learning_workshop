from cProfile import label
from flask import Flask, redirect, url_for, request, render_template
import os

from graphviz import render
from model import Model

app = Flask(__name__)

pk1 = Model()
pk1.train()

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        lables = [x for x in request.values]
        data = []
        data_dict = {}
        for i in lables:
            data_dict[i] = request.form[i]
            data.append(request.form[i])
        result = pk1.predict([data])
        if result[0] == 0:
            return render_template('index.html', result="You Do not Have Diabities", **data_dict) 
        else:
            return render_template('index.html', result="You Have Diabities", **data_dict)
            
    return render_template('index.html') 

if __name__ == '__main__':
   app.run()