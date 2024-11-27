# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('expected, test', (pytest.param(1, (10, 10), marks=pytest.mark.smoke),
                         pytest.param(None, (10, 0), marks=pytest.mark.skip('skip')),
                         pytest.param(-1, (10, -10), marks=pytest.mark.acceptance),
                         pytest.param(10, (10, 1), marks=pytest.mark.acceptance),
                         pytest.param(1, (1000000, 10, 10, 10, 10, 10, 10), marks=pytest.mark.acceptance)))
def test_division(expected, test):
    assert all_division(*test) == expected


