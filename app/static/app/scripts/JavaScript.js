document.addEventListener('DOMContentLoaded', function () {
    // Получаем кнопку отправки формы
    const submitButton = document.querySelector('button[type="submit"]');

    // Получаем все поля ввода
    const inputFields = document.querySelectorAll('input[type="text"], input[type="email"]');

    // Добавляем обработчики событий для кнопки
    submitButton.addEventListener('mouseover', function () {
        this.style.color = 'yellow'; // Изменяем цвет текста при наведении
    });

    submitButton.addEventListener('mouseout', function () {
        this.style.color = ''; // Восстанавливаем исходный цвет текста
    });

    // Добавляем обработчики событий для полей ввода
    inputFields.forEach(function (input) {
        input.addEventListener('focus', function () {
            this.style.backgroundColor = 'lightblue'; // Изменяем цвет фона при фокусе
        });

        input.addEventListener('blur', function () {
            this.style.backgroundColor = ''; // Восстанавливаем исходный цвет фона
        });
    });
});
