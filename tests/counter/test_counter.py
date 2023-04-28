from src.pre_built.counter import count_ocurrences


def test_counter():
    "verifica sucesso para ocorrências da palavra 'Python'"
    assert count_ocurrences("data/jobs.csv", "Python") == 1639
    assert count_ocurrences("data/jobs.csv", "Python") != ""
