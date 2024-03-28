from flask import Flask, request, jsonify
from mes_server_2 import setup  # Import your backend function

app = Flask(__name__)
Flag=True
@app.route('/process', methods=['POST'])
def process():
    data = request.json  # Assuming the input will be provided in JSON format
    input_string = data['input']
    print('Flag Status:',Flag)
    output_string = setup(input_string, Flag)  # Call your backend function
    print("Type of the output string in api:",output_string)
    answer = [
        {
        'output': output_string
    }
    ]
    print("The type of the answer file is:",answer)
    print("type of this file is:",jsonify({"output":output_string}) )
    return output_string

if __name__ == '__main__':
    app.run(debug=True)
