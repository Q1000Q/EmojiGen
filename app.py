from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from groq import Groq

# Inits flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

load_dotenv()

# Init groq from env varible
groq_client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@app.route('/', methods=['GET'])
def method_name():
    input = request.args.get('input')
    level = request.args.get('level')
    
    if input:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f'Convert this text to emojis at level {level} (from 0 to 5): "{input}" (Do not give any additional text exept emojis or maybe some original text, DO NOT INCLUEDE NOTHING LIKE here is a xyz DO ONLY INCLUDE OUTPUT)',
                }
            ],
            model="llama3-8b-8192",
        )
        
        output = chat_completion.choices[0].message.content
        
        return render_template('index.html', output=output, level=level)
    else:
        return render_template('index.html', level=3) 

if __name__ == "__main__":
    # Imports waitress and serve app
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)