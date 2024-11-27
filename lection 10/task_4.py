# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import datetime

import pytest
import time


@pytest.mark.usefixtures('test_start_time')
class Test:
    def test1(self, test_execution_time):
        time.sleep(5)

    def test2(self):
        time.sleep(5)
