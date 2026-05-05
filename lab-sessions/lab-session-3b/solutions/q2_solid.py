"""
Lab Session 3B — Question 2: Order Management SOLID Refactoring
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME: Solution
STUDENT ID: 000000
"""


class OrderValidator:
    def validate(self, customer, items, total):
        return bool(customer and items and total > 0)
    
    def validate_or_raise(self, customer, items, total):
        if not customer:
            raise ValueError("Invalid order: customer cannot be empty")
        if not items:
            raise ValueError("Invalid order: items cannot be empty")
        if total <= 0:
            raise ValueError("Invalid order: total must be positive")


class OrderRepository:
    def __init__(self):
        self.orders = []
    
    def add(self, order):
        order_with_id = order.copy()
        order_with_id['id'] = len(self.orders) + 1
        self.orders.append(order_with_id)
        return order_with_id['id']
    
    def find(self, order_id):
        for order in self.orders:
            if order['id'] == order_id:
                return order
        return None
    
    def count(self):
        return len(self.orders)
    
    def all(self):
        return self.orders.copy()


class NotificationService:
    def send_confirmation(self, customer, total):
        print(f"Email sent to {customer}: Your order for ${total:.2f} is confirmed")


class OrderReportService:
    def generate_summary(self, repo):
        count = repo.count()
        if count == 0:
            return "No orders found"
        
        orders = repo.all()
        total_value = sum(order['total'] for order in orders)
        avg_value = total_value / count
        
        return f"Total orders: {count}\nAverage order value: ${avg_value:.2f}"


class OrderProcessor:
    def __init__(self, repo, validator, notifier):
        self.repo = repo
        self.validator = validator
        self.notifier = notifier
    
    def process_order(self, customer, items, total):
        # Validate
        self.validator.validate_or_raise(customer, items, total)
        
        # Create order
        order = {
            'customer': customer,
            'items': items,
            'total': total,
            'status': 'processed'
        }
        
        order_id = self.repo.add(order)
        
        # Send notification
        self.notifier.send_confirmation(customer, total)
        
        return f"Order #{order_id} processed for {customer}"


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Order Management SOLID Refactoring ===")

    # Create dependencies
    repo = OrderRepository()
    validator = OrderValidator()
    notifier = NotificationService()
    report_service = OrderReportService()

    # Create processor with dependency injection
    processor = OrderProcessor(repo, validator, notifier)

    # Test valid orders
    print("\nProcessing valid order...")
    result = processor.process_order("Alice", ["laptop", "mouse"], 99.99)
    print(result)

    print("\nProcessing another order...")
    result = processor.process_order("Bob", ["phone", "case"], 149.50)
    print(result)

    # Test reporting
    print(f"\nOrder summary:")
    summary = report_service.generate_summary(repo)
    print(summary)

    # Test validation error
    print("\nProcessing invalid order...")
    try:
        processor.process_order("", ["item"], 50.0)
    except ValueError as e:
        print(f"Error: {e}")