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
    try:
        min_salary = int(job.get("min_salary"))
        max_salary = int(job.get("max_salary"))
        salary = int(salary)
        if min_salary > max_salary:
            raise ValueError
    except (TypeError, KeyError):
        raise ValueError
    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except (TypeError, ValueError):  # captura a exceção e continua
            pass

    return filtered_jobs


# me parece que de alguma forma esta verificação acima está errada e aceita
# valor que não deveria no filter
