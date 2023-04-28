from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    path_reader_data = read(path)
    return max(
        [
            int(data_salary["max_salary"])
            for data_salary in path_reader_data
            if data_salary["max_salary"].isdigit()
        ]
    )


def get_min_salary(path: str) -> int:
    path_reader_data = read(path)
    return min(
        [
            int(data_salary["min_salary"])
            for data_salary in path_reader_data
            if data_salary["min_salary"].isdigit()
        ]
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    min_salary = job.get("min_salary", None)
    max_salary = job.get("max_salary", None)

    if min_salary is None or max_salary is None:
        raise ValueError

    if not isinstance(min_salary, (int)) or not isinstance(max_salary, (int)):
        raise ValueError

    if int(min_salary) > int(max_salary):
        raise ValueError

    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
