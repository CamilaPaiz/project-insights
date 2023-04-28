from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    jobs = read_brazilian_file(path)
    for itens in jobs:
        assert "title" in itens
        assert "salary" in itens
        assert "type" in itens


# como mockar o retorno esperado sendo que em mocks é feita uma função que lê
# de jobs de insight,onde ver mais exemplos de testes?
