"""Lab Session 4B — Q1 Solution: Closures and Function Factories"""


def make_raise_calculator(percent):
    """Returns a function that raises an employee's salary by `percent`%."""
    def apply_raise(employee):
        new_salary = int(employee["salary"] * (1 + percent / 100))
        return {**employee, "salary": new_salary}
    return apply_raise


def make_department_filter(department):
    """Returns a predicate that is True for employees in `department`."""
    def is_in_department(employee):
        return employee["department"] == department
    return is_in_department


def make_salary_total(department):
    """Returns a function that sums salaries of all employees in `department`."""
    def total(employees):
        return sum(e["salary"] for e in employees if e["department"] == department)
    return total


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    employees = [
        {"name": "Alice Johnson", "department": "Engineering", "salary": 75000, "years": 5},
        {"name": "Bob Smith",     "department": "Marketing",   "salary": 45000, "years": 2},
        {"name": "Carol Brown",   "department": "Engineering", "salary": 82000, "years": 7},
        {"name": "David Wilson",  "department": "Sales",       "salary": 52000, "years": 3},
        {"name": "Eva Davis",     "department": "Engineering", "salary": 68000, "years": 4},
        {"name": "Frank Miller",  "department": "Marketing",   "salary": 38000, "years": 1},
    ]

    print("=== Closures and Function Factories ===")

    apply_10_raise = make_raise_calculator(10)
    raised = list(map(apply_10_raise, employees))

    print("\nAfter 10% raise:")
    for original, updated in zip(employees, raised):
        print(f"  {original['name']}: ${original['salary']} → ${updated['salary']}")

    assert all(e["salary"] == orig["salary"] for e, orig in zip(employees, employees))

    is_engineering = make_department_filter("Engineering")
    is_marketing   = make_department_filter("Marketing")

    eng_employees = list(filter(is_engineering, employees))
    mkt_employees = list(filter(is_marketing,   employees))

    print("\nEngineering employees:")
    for e in eng_employees:
        print(f"  {e['name']}: ${e['salary']}")

    print("\nMarketing employees:")
    for e in mkt_employees:
        print(f"  {e['name']}: ${e['salary']}")

    calc_eng_total = make_salary_total("Engineering")
    calc_mkt_total = make_salary_total("Marketing")
    calc_sal_total = make_salary_total("Sales")

    print("\nDepartment salary totals:")
    print(f"  Engineering: ${calc_eng_total(employees)}")
    print(f"  Marketing:   ${calc_mkt_total(employees)}")
    print(f"  Sales:       ${calc_sal_total(employees)}")
