from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    job_list_not_sorted = [
        {"date:2000-5-5", "max_salary:2000", "min_salary:1000"},
        {"date:2000-5-5", "max_salary:2500", "min_salary:1000"},
        {"date:2000-5-5", "max_salary:1000", "min_salary:5000"},
    ]
    job_list_sorted = [
        {"date:2000-5-5", "max_salary:1000", "min_salary:1000"},
        {"date:2000-5-5", "max_salary:2000", "min_salary:1000"},
        {"date:2000-5-5", "max_salary:2500", "min_salary:5000"},
    ]
    assert sort_by(job_list_not_sorted, "max_salary") == job_list_sorted
