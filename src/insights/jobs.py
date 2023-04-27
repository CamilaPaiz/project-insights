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
    """job_type_data = read(path)
    job_type_set = set()
    for type in job_type_data:
        job_type_set.add(type["job_type"])
    return job_type_set"""
    job_type_data = read(path)
    return {type["job_type"] for type in job_type_data}


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """type_list = []
    for type in jobs:
        if type["job_type"] == job_type:
            type_list.append(type)
    return type_list
    """
    return [type for type in jobs if type["job_type"] == job_type]
