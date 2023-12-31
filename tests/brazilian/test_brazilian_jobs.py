from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    jobs = read_brazilian_file(path)
    for itens in jobs:
        assert "title" in itens
        assert "salary" in itens
        assert "type" in itens
