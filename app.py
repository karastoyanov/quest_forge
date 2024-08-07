import json
from flask import Flask, jsonify
from python_quest_generator import generate_quest

app = Flask(__name__)

# Generate a Python Quest
@app.route('/generate_py_task', methods=['GET', 'POST'])
def generate_py_task():
    # Read the format and examples from the files
    with open('format.txt', 'r') as format_file:
        format_content = format_file.read()
    
    with open('example_tasks.txt', 'r') as examples_file:
        examples_content =  examples_file.read()
        
    
    # Generate the quest
    try:
        result_dict = generate_quest(format_content, examples_content)
        specific_part = {
            'title': result_dict['title'],
            'description': result_dict['description'],
            'task_difficulty': result_dict['task_difficulty'],
            'function_template': result_dict['function_template'],
            'inputs': result_dict['example_inputs'],
            'outputs': result_dict['example_outputs']
        }
        return jsonify({'generated_task': specific_part}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5005)