import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as file:
        path_reader = csv.DictReader(file)
        data = [row for row in path_reader]
    return data


def get_unique_job_types(path: str) -> List[str]:
    job_type_data = read(path)
    job_type_set = set()
    for job in job_type_data:
        job_type_set.add(job["job_type"])
    job_type_list = list(job_type_set)
    return job_type_list


print(get_unique_job_types("data/jobs.csv"))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
