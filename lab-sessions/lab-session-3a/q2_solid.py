"""
Lab Session 3A — Question 2: SOLID Refactoring (30 pts)
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME:
STUDENT ID:
"""


# YOUR CODE HERE


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== SOLID Refactoring ===")

    repo = UserRepository()
    validator = EmailValidator()
    email_svc = EmailService()
    report_svc = UserReportService()

    manager = UserManager(repo, validator, email_svc)
    manager.add_user("Alice", "alice@example.com")
    manager.add_user("Bob", "bob@example.com")

    print("\nUsers:")
    for user in repo.all():
        print(f"  {user['email']}")

    print(f"\nTotal users: {len(repo.all())}")

    print("\nError: ", end="")
    try:
        manager.add_user("Charlie", "not-an-email")
    except ValueError as e:
        print(e)
