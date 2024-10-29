from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Настройка клиента OpenAI
openai.api_key = 'sk-hJwXsYxunDy1Knm1A300A9AfD173476f91DbEdD21862B44e'
openai.api_base = 'https://api.rockapi.ru/openai/v1'

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # Замените на 'gpt-4', если у вас есть доступ
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_response = generate_response(user_message)
    return jsonify({'reply': bot_response})

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Ошибка: {str(e)}")
