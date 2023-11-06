from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-script')
def run_script():
    # This will execute your Python script and return its output
    try:
        output = subprocess.check_output(['python', 'H:\\PythonProjects\\Sorting_Creation_Updated\\main.py'])
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return "Error executing script: " + str(e)


if __name__ == "__main__":
    app.run()
