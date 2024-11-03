from util.registration import Registrtion
from util.logger import Logger


class TestRegKoshelekRef():

    test_name = "Тестирование поля ввода реф. ссылки"

    def test_reg_ref_less_than_4(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzb',
            'acceptance': True
        }

        response = Registrtion.check(dict_reg)
        descr_test = "Проверка регистрации нового пользователя с указанием реф. ссылки менее 4 символов"
        print(descr_test)
        expected_result = 'Неверный формат ссылки'
        result = True if response['ref'] == expected_result else False
        Logger.test_logger(TestRegKoshelekRef.test_name,
                           descr_test, dict_reg, response, result)
        assert result

    def test_reg_ref_less_than_8(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzbnadefd',
            'acceptance': True
        }

        response = Registrtion.check(dict_reg)
        descr_test = "Проверка регистрации нового пользователя с указанием реф. ссылки более 8 символов"
        print(descr_test)
        expected_result = 'Неверный формат ссылки'
        result = True if response['ref'] == expected_result else False
        Logger.test_logger(TestRegKoshelekRef.test_name,
                           descr_test, dict_reg, response, result)
        assert result
