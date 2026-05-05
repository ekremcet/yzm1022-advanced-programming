"""Lab Session 3 — Q2 Solution: SOLID Refactoring"""


class EmailValidator:
    def validate(self, email: str) -> bool:
        return "@" in email

    def validate_or_raise(self, email: str):
        if not self.validate(email):
            raise ValueError("Invalid email format")


class EmailService:
    def send_welcome(self, email: str):
        print(f"Sending welcome email to {email}")


class UserRepository:
    def __init__(self):
        self._users = []

    def add(self, name: str, email: str):
        self._users.append({"name": name, "email": email})

    def find(self, name: str):
        return next((u for u in self._users if u["name"] == name), None)

    def all(self) -> list:
        return self._users.copy()


class UserReportService:
    def generate(self, repo: UserRepository) -> str:
        return "\n".join(f"{u['name']}: {u['email']}" for u in repo.all())


class UserManager:
    def __init__(self, repo: UserRepository, validator: EmailValidator, email_service: EmailService):
        self._repo = repo
        self._validator = validator
        self._email_svc = email_service

    def add_user(self, name: str, email: str):
        self._validator.validate_or_raise(email)
        self._repo.add(name, email)
        self._email_svc.send_welcome(email)

    def get_user(self, name: str):
        return self._repo.find(name)

    def generate_report(self) -> str:
        return UserReportService().generate(self._repo)


if __name__ == "__main__":
    print("=== SOLID Refactoring ===")
    repo = UserRepository()
    validator = EmailValidator()
    email_svc = EmailService()
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
