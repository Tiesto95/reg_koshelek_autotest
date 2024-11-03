Для запуска приложения для автоматического тестирования формы регистрации на сайте koshelek.ru выполните следующие шаги:

1) Создайте виртуальное окружение:

python -m venv myautotest

2) Активируйте созданное окружение:

myautotest\Scripts\activate

3) Перейдите в папку с окружением:

cd myautotest

4) Склонируйте репозиторий в окружение командой:

git clone git@github.com:Tiesto95/reg_koshelek_autotest.git

Либо создайте папку, скачайте архив и разархивируйте приложение в папку.

5) При необходимости обновите pip:

python.exe -m pip install --upgrade pip

6) Установите все необходимые библиотеки:

pip install -r requirements.txt

7) Запустите тесты:

python -m pytest -s -v

8) В приложении указаны драйвера браузера Chrome, для работы в других браузерах необходимо в файле registration.py импортировать и подключить соответствующий драйвер. 

Во время выполнения тестов в консоли отображается прогресс, а также ведется подробное логирование в файле log_дата_время.log в папке logs.

Чтобы увидеть процесс тестирования в браузере, закомментируйте или удалите строку options.add_argument('--headless') в файле registration.py.

Приложение включает 16 тестов. Оценить полноту тестового покрытия невозможно, так как отсутствуют доступ к требованиям к форме регистрации.
