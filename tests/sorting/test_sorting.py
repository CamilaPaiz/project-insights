from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    job_list = [
        {
            "date_posted": "2000-5-7",
            "max_salary": 2000,
            "min_salary": 1000,
        },
        {
            "date_posted": "2000-5-6",
            "max_salary": 2500,
            "min_salary": 1010,
        },
        {
            "date_posted": "2000-5-8",
            "max_salary": 1000,
            "min_salary": 500,
        },
    ]
    max_salary_sorted = [
        {
            "date_posted": "2000-5-6",
            "max_salary": 2500,
            "min_salary": 1010,
        },
        {
            "date_posted": "2000-5-7",
            "max_salary": 2000,
            "min_salary": 1000,
        },
        {
            "date_posted": "2000-5-8",
            "max_salary": 1000,
            "min_salary": 500,
        },
    ]
    min_salary_sorted = [job_list[2], job_list[0], job_list[1]]
    date_posted_sorted = [job_list[2], job_list[0], job_list[1]]

    sort_by(job_list, "max_salary")  # decrescente
    assert job_list == max_salary_sorted

    sort_by(job_list, "min_salary")  # crescente
    assert job_list == min_salary_sorted

    sort_by(job_list, "date_posted")  # decrescente
    assert job_list == date_posted_sorted
