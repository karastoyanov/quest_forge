from client import client
import json
import requests

def generate_quest(format, examples):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": f'Generate me a unique Python exercise task in the following format:\n' + format + examples}],
        temperature=0.9
    )
    
    result = response.choices[0].message.content
    try:
        start_idx = result.find("{")
        end_idx = result.rfind("}") + 1
        result_json = result[start_idx:end_idx]
        result_dict = json.loads(result_json)
        return result_dict
    except Exception as e:
        raise ValueError(f"Failed to extract and parse JSON from the response: {e}")




def format_task(task_dict):
    try:
        specific_part = {
            'title': task_dict['title'],
            'description': task_dict['description'],
            'function_template': task_dict['function_template']
        }
        return specific_part
    except KeyError as e:
        return f"Error formatting the quest: Missing key - {e}"
    except Exception as e:
        return f"Error formatting the quest: {e}"




# print(generate_quest(format))
# format_task(generate_quest(format, example_tasks))