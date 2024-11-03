from util.registration import Registrtion
from util.logger import Logger


class TestRegKoshelekPass():

    test_name = "Тестирование поля ввода пароля пользователя."

    def test_reg_pass_null(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail.ru',
            'pass': '',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя без указания пароля."
        print(descr_test)
        expected_result = 'Поле не заполнено'
        result = True if response['pass'] == expected_result else False
        Logger.test_logger(TestRegKoshelekPass.test_name,
                           descr_test, dict_reg, response, result)
        assert result

    def test_reg_pass_less_than_8(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaco2@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя длиной пароля менее 8 символов."
        print(descr_test)
        expected_result = 'Пароль должен содержать минимум 8 символов'
        result = True if response['pass'] == expected_result else False
        Logger.test_logger(TestRegKoshelekPass.test_name,
                           descr_test, dict_reg, response, result)
        assert result

    def test_reg_pass_more_than_64(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@Anaconda2024@Anaconda2024@Anaconda2024@Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя длиной пароля более 64 символов."
        print(descr_test)
        expected_result = 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'
        result = True if response['pass'] == expected_result else False
        Logger.test_logger(TestRegKoshelekPass.test_name,
                           descr_test, dict_reg, response, result)
        assert result

    def test_reg_pass_not_capital(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail.ru',
            'pass': 'anaconda2024',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя длиной пароля без заглавной буквы."
        print(descr_test)
        expected_result = 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'
        result = True if response['pass'] == expected_result else False
        Logger.test_logger(TestRegKoshelekPass.test_name,
                           descr_test, dict_reg, response, result)
        assert result

    def test_reg_pass_not_num(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя длиной пароля без цифры."
        print(descr_test)
        expected_result = 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'
        result = True if response['pass'] == expected_result else False
        Logger.test_logger(TestRegKoshelekPass.test_name,
                           descr_test, dict_reg, response, result)
        assert result
