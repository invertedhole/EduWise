$(document).ready(function() {
    $('#send-button').click(function() {
        var userMessage = $('#user-input').val().trim();
        if (userMessage === "") {
            alert("Пожалуйста, введите сообщение."); // Проверка на пустое сообщение
            return;
        }
        $('#chatbox').append('<div>Вы: ' + userMessage + '</div>');
        $('#user-input').val('');

        $.ajax({
            url: '/chat',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ message: userMessage }),
            success: function(data) {
                $('#chatbox').append('<div>Бот: ' + data.reply + '</div>');
                $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight); // Прокрутка вниз
            },
            error: function() {
                $('#chatbox').append('<div>Ошибка при получении ответа от бота.</div>');
            }
        });
    });

    // Обработка нажатия клавиши Enter
    $('#user-input').keypress(function(e) {
        if (e.which == 13) { // Код клавиши Enter $('#send-button').click();
        }
    });
});