document.addEventListener('DOMContentLoaded', function () {
    // �������� ������ �������� �����
    const submitButton = document.querySelector('button[type="submit"]');

    // �������� ��� ���� �����
    const inputFields = document.querySelectorAll('input[type="text"], input[type="email"]');

    // ��������� ����������� ������� ��� ������
    submitButton.addEventListener('mouseover', function () {
        this.style.color = 'yellow'; // �������� ���� ������ ��� ���������
    });

    submitButton.addEventListener('mouseout', function () {
        this.style.color = ''; // ��������������� �������� ���� ������
    });

    // ��������� ����������� ������� ��� ����� �����
    inputFields.forEach(function (input) {
        input.addEventListener('focus', function () {
            this.style.backgroundColor = 'lightblue'; // �������� ���� ���� ��� ������
        });

        input.addEventListener('blur', function () {
            this.style.backgroundColor = ''; // ��������������� �������� ���� ����
        });
    });
});
