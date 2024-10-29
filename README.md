# EduWise
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>EduWise - Learn Smarter</title>
    <link rel="stylesheet" href="/static/styles.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>EduWise chatbot</h1>
    <input type="text" id="user-input" placeholder="Введите сообщение">
    <button onclick="sendMessage()">Отправить</button>
    <div id="chat-output"></div>
    <script>
        function sendMessage() {
            const userInput = document.getElementById('user-input').value;
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userInput }),
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('chat-output').innerHTML += `<p>Вы: ${userInput}</p>`;
                document.getElementById('chat-output').innerHTML += `<p>Бот: ${data.reply}</p>`;
                document.getElementById('user-input').value = ''; // Очистить поле ввода
            });
        }
    </script>
</body>
     <script>
        $(document).ready(function() {
            $('#send-button').click(function() {
                const userMessage = $('#user-input').val();
                if (userMessage.trim() === '') return;
                // Отображаем сообщение пользователя
                $('#chat').append('<div class="user-message">Вы: ' + userMessage + '</div>');
                $('#user-input').val('');
                // Отправляем сообщение на сервер
                $.ajax({
                    url: '/chat',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ message: userMessage }),
                    success: function(data) {
                        // Отображаем ответ бота
                        $('#chat').append('<div class="bot-response">ИИ: ' + data.reply + '</div>');
                        // Прокручиваем вниз, чтобы увидеть новый ответ
                        $('#chat').scrollTop($('#chat')[0].scrollHeight);
                    },
                    error: function() {
                        $('#chat').append('<div class="bot-response">Произошла ошибка при получении ответа.</div>');
                    }
                });
            });
            // Отправка сообщения по нажатию клавиши Enter
            $('#user-input').keypress(function(event) {
                if (event.which === 13) {
                    $('#send-button').click();
                }
            });
        });
    </script>
</body>
</html>
