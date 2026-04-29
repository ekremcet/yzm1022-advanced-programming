"""
Lab Session 3B — Question 2: Order Management SOLID Refactoring
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