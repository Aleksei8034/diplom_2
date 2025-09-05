from faker import Faker


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_correct = {
        "email": 'lexa.d.nik@yandex.ru',
        "password": "123456"}

    data_negative = {
        "email": 'nik.d.lexa@yandex.ru',
        "password": "654321"}

    data_double = {
        "email": 'lexa.d.nik@yandex.ru',
        "password": "123456",
        "name": "lexa"}

    data_without_email = {
        "email": '',
        "password": "123456",
        "name": "lexa"}

    data_without_password = {
        "email": 'lexa.d.nik@yandex.ru',
        "password": "",
        "name": "lexa"}

    data_without_name = {
        "email": 'lexa.d.nik@yandex.ru',
        "password": "123456",
        "name": ""}

    data_updated = {
        "email": 'lexa.d.nik@yandex.ru',
        "password": "123456",
        "name": "nelexa"}
