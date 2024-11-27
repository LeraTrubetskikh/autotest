import pytest
import datetime
import time


@pytest.fixture(scope='class')
def test_start_time():
    print(f"\nstart time: {datetime.datetime.now().time()}")
    yield
    print(f"\nend time: {datetime.datetime.now().time()}")


@pytest.fixture()
def test_execution_time():
    start = time.time()
    yield
    print(f"\nexecution_time: {time.time() - start}")
