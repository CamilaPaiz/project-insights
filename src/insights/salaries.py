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

    if not isinstance(min_salary, int) or not isinstance(max_salary, int):
        raise ValueError

    if int(min_salary) > int(max_salary):
        raise ValueError

    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs


# me parece que de alguma forma esta verificação acima está errada e aceita
# valor que não deveria no filter
