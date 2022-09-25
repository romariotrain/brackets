import pytest
from main import *
from parameterized import parameterized


tests = [('[([])((([[[]]])))]{()}', 'Сбалансированно'),
         ('(((([{}]))))', 'Сбалансированно'),
         ('}{}', 'Несбалансированно'),
         ('{{[(])]}}', 'Несбалансированно'),
         ('[[{())}]', 'Несбалансированно'),
         ('{}{}{[{{{{}]}}dmsakda', 'Несбалансированно'),
         ('((([(]))))', 'Несбалансированно')]

@pytest.mark.parametrize('a, result', tests)
def test_check_brackets(a, result):
    check_result = check_brackets(a)
    assert check_result == result


check_brackets('[([])((([[[]]])))]{()}')



