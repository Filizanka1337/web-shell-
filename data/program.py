import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form.get('command')
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return render_template('index.html', result=output)
    except Exception as e:
        return render_template('index.html', error=str(e))

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.system('shutdown -s -t 2')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6547)
