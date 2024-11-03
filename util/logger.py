import datetime


class Logger():
    file_name = 'logs/log_' + \
        str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.log'

    @classmethod
    def write_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as log_file:
            log_file.write(data)

    @classmethod
    def test_logger(cls, test_name: str, descr: str, data_test: dict, response: dict, result: bool):
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"description: {descr}\n"
        data_to_add += f"Test data: {data_test}\n"
        data_to_add += f"Response data: {response}\n"
        data_to_add += f"Результат теста: " + \
            ("Пройден" if result else "Провален")
        data_to_add += "\n"

        cls.write_file(data_to_add)
