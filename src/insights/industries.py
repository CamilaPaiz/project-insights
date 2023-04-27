from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    path_reader_data = read(path)
    return {
        type["industry"] for type in path_reader_data if type["industry"] != ""
    }


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    return [type for type in jobs if type["industry"] == industry]
