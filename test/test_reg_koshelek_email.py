from util.registration import Registrtion
from util.logger import Logger


class TestRegKoshelekEmail():

    test_name = "Тестирование поля ввода электронной почты(Email)."

    def test_reg_email_null(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': '',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя не указав E-mail."
        print(descr_test)
        expected_result = "Поле не заполнено"
        result = True if response['email'] == expected_result else False
        Logger.test_logger(TestRegKoshelekEmail.test_name,
                           descr_test, dict_reg, response, result)
        assert result

    def test_reg_email_not_dog(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя с указанием E-mail несоответствующего формата (без @)."
        print(descr_test)
        expected_result = 'Формат e-mail: username@test.ru'
        result = True if response['email'] == expected_result else False
        Logger.test_logger(TestRegKoshelekEmail.test_name,
                           descr_test, dict_reg, response, result)
        assert result

    def test_reg_email_not_ru(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя с указанием E-mail несоответствующего формата (без указания домена первого уровня.)."
        print(descr_test)
        expected_result = 'Формат e-mail: username@test.ru'
        result = True if response['email'] == expected_result else False
        Logger.test_logger(TestRegKoshelekEmail.test_name,
                           descr_test, dict_reg, response, result)
        assert result
