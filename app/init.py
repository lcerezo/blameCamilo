from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def camilo():
    return render_template('blamecamilo.html')