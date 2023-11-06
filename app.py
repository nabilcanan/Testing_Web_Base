from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-script', methods=['POST'])
def run_script():
    # Define the path to your main.py script
    script_path = 'H:/PythonProjects/Sorting_Creation_Updated/main.py'

    # Run the script and collect the output
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        return jsonify({'success': True, 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
