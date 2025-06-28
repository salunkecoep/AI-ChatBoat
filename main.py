from flask import Flask, render_template, request

# Start flask app and set to ngrok
app = Flask(__name__)

@app.route('/')
def initial():
  return render_template('index.html', response="")

@app.route('/submit-prompt', methods=['POST'])
def generate_response():
  
  prompt = request.form['prompt-input']
  res = prompt
  
  return render_template('index.html', response=res)

if __name__ == '__main__':
    app.run(debug=True)




