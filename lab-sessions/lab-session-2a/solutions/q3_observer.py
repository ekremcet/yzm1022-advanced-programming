"""Lab Session 2 — Q3 Solution: Stock Market Observer"""
from abc import ABC, abstractmethod


class StockObserver(ABC):
    @abstractmethod
    def update(self, ticker: str, price: float, change: float):
        pass


class Investor(StockObserver):
    def __init__(self, name: str, portfolio: list):
        self.name = name
        self.portfolio = portfolio

    def update(self, ticker: str, price: float, change: float):
        if ticker in self.portfolio:
            print(f"  {self.name}: {ticker} is now ${price:.2f} ({change:+.2f}%)")


class NewsAgency(StockObserver):
    def __init__(self, name: str):
        self.name = name

    def update(self, ticker: str, price: float, change: float):
        print(f"  BREAKING: {ticker} moved {change:+.2f}% to ${price:.2f}")


class StockMarket:
    def __init__(self):
        self._prices = {}
        self._subscribers = {}

    def set_price(self, ticker: str, price: float):
        self._prices[ticker] = price

    def subscribe(self, ticker: str, observer: StockObserver):
        self._subscribers.setdefault(ticker, []).append(observer)

    def unsubscribe(self, ticker: str, observer: StockObserver):
        if ticker in self._subscribers:
            self._subscribers[ticker].remove(observer)

    def update_price(self, ticker: str, new_price: float):
        old = self._prices.get(ticker, new_price)
        change = ((new_price - old) / old) * 100 if old != 0 else 0
        self._prices[ticker] = new_price
        for obs in self._subscribers.get(ticker, []):
            obs.update(ticker, new_price, change)


if __name__ == "__main__":
    print("=== Stock Market Observer ===")
    market = StockMarket()
    market.set_price("AAPL", 150.0)
    market.set_price("TSLA", 240.0)

    alice = Investor("Alice", ["AAPL", "MSFT"])
    bob = Investor("Bob", ["TSLA", "AAPL"])
    reuters = NewsAgency("Reuters")

    market.subscribe("AAPL", alice)
    market.subscribe("AAPL", reuters)
    market.subscribe("TSLA", bob)
    market.subscribe("TSLA", reuters)

    print("\nAAPL price update: $155.00")
    market.update_price("AAPL", 155.0)
    print("\nTSLA price update: $250.00")
    market.update_price("TSLA", 250.0)
    print("\nAAPL price update: $148.00")
    market.update_price("AAPL", 148.0)
