from util.registration import Registrtion
from util.logger import Logger


class TestRegKoshelekAcceptance():

    test_name = "Тестирование Checkbox поля (принятия пользовательского соглашения)."

    def test_reg_accep_off(self):
        dict_reg = {
            'user_name': 'beslan2026',
            'email': 'beslan-2010@mail.ru',
            'pass': 'Anaconda2024@',
            'ref': 'mzbd',
            'acceptance': False
        }

        response = Registrtion.check(dict_reg)
        descr_test = "Проверка регистрации нового пользователя без принятия условий пользовательского соглашения."
        print(descr_test)
        expected_result = '$checkboxErrorDark'
        result = True if expected_result in response['acceptance'] else False
        Logger.test_logger(TestRegKoshelekAcceptance.test_name,
                           descr_test, dict_reg, response, result)
        assert result
