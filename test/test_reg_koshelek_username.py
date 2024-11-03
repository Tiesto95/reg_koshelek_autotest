from util.registration import Registrtion
from util.logger import Logger


class TestRegKoshelekUserName():
    test_name = "Тестирование поля ввода имени пользователя."

    def test_reg_username_less_5(self):
        dict_reg = {
            'user_name': 'besla',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя с именем меньше 6 символов."
        print(descr_test)
        expected_result = 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
        result = True if response['user_name'] == expected_result else False
        Logger.test_logger(TestRegKoshelekUserName.test_name,
                           descr_test, dict_reg, response, result)
        assert response['user_name'] == expected_result

    def test_reg_username_is_33_characters(self):
        dict_reg = {
            'user_name': 'beslanzaurbaevbeslabeslanzaurbaev',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя с именем больше 32 символов."
        print(descr_test)
        expected_result = 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
        result = True if response['user_name'] == expected_result else False
        Logger.test_logger(TestRegKoshelekUserName.test_name,
                           descr_test, dict_reg, response, result)
        assert response['user_name'] == expected_result

    def test_reg_username_is_kiril(self):
        dict_reg = {
            'user_name': 'Беслан',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя с именем на кириллице."
        print(descr_test)
        expected_result = 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
        result = True if response['user_name'] == expected_result else False
        Logger.test_logger(TestRegKoshelekUserName.test_name,
                           descr_test, dict_reg, response, result)
        assert response['user_name'] == expected_result

    def test_reg_username_is_spec(self):
        dict_reg = {
            'user_name': 'Beslan$#',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя с использованием спец. символов при написании имени пользователя."
        print(descr_test)
        expected_result = 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
        result = True if response['user_name'] == expected_result else False
        Logger.test_logger(TestRegKoshelekUserName.test_name,
                           descr_test, dict_reg, response, result)
        assert response['user_name'] == expected_result

    def test_reg_username_is_null(self):
        dict_reg = {
            'user_name': '',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': True
        }

        response = Registrtion.chek(dict_reg)
        descr_test = "Проверка регистрации нового пользователя оставив пустым поле имя пользователя."
        print(descr_test)
        expected_result = 'Поле не заполнено'
        result = True if response['user_name'] == expected_result else False
        Logger.test_logger(TestRegKoshelekUserName.test_name,
                           descr_test, dict_reg, response, result)
        assert response['user_name'] == expected_result

    # Капча не позволяет произвести проверку.

    # def test_reg_username_taken(self):
    #     dict_reg = {
    #         'user_name': 'beslan2024',
    #         'email': 'beslan-2010@mail.ru',
    #         'pass': 'Anaconda2024@',
    #         'ref': 'mzbd',
    #         'acceptance': True
    #     }

    #     response = Registrtion.chek(dict_reg)
        # descr_test = "Проверка регистрации нового пользователя c именем уже зарегистрированного пользователя."
        # print(descr_test)
        # expected_result = 'Имя пользователя уже занято'
        # result = True if response['user_name'] == expected_result else False
        # Logger.test_logger(TestRegKoshelekUserName.test_name, descr_test, dict_reg, response, result)
        # assert response['user_name'] == expected_result
