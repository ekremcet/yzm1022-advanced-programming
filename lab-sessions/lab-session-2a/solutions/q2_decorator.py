"""Lab Session 2 — Q2 Solution: Logging Decorators"""
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> str:
        pass


class ConsoleLogger(Logger):
    def log(self, message: str) -> str:
        return f"[LOG] {message}"


class LoggerDecorator(Logger):
    def __init__(self, wrapped: Logger):
        self._wrapped = wrapped

    def log(self, message: str) -> str:
        return self._wrapped.log(message)


class TimestampDecorator(LoggerDecorator):
    def log(self, message: str) -> str:
        return self._wrapped.log(f"[2026-04-14] {message}")


class UpperCaseDecorator(LoggerDecorator):
    def log(self, message: str) -> str:
        return self._wrapped.log(message.upper())


class PrefixDecorator(LoggerDecorator):
    def __init__(self, wrapped: Logger, prefix: str):
        super().__init__(wrapped)
        self.prefix = prefix

    def log(self, message: str) -> str:
        return self._wrapped.log(f"[{self.prefix}] {message}")


if __name__ == "__main__":
    print("=== Logging Decorators ===")
    base = ConsoleLogger()
    ts = TimestampDecorator(ConsoleLogger())
    upper = UpperCaseDecorator(ConsoleLogger())
    prefix = PrefixDecorator(ConsoleLogger(), "INFO")
    combined = UpperCaseDecorator(TimestampDecorator(PrefixDecorator(ConsoleLogger(), "ERROR")))

    print(f"Simple: {base.log('server started')}")
    print(f"Timestamp: {ts.log('server started')}")
    print(f"Uppercase: {upper.log('server started')}")
    print(f"Prefix: {prefix.log('server started')}")
    print(f"Combined: {combined.log('disk full')}")
