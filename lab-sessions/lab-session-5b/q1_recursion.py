"""
Lab Session 5B - Question 1: Recursive Problem Solving (30 pts)
See README.md for the full description.

Implement the function marked `# YOUR CODE HERE`.
Do NOT modify the test block at the bottom - it prints the expected output.
"""


def tower_of_hanoi(n, src, dst, aux):
    """Solve Tower of Hanoi for n disks.
    Print each move as "Move disk from {src} to {dst}" and return the
    total number of moves made."""
    # YOUR CODE HERE
    pass


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Tower of Hanoi ===")

    print("\nMoves for 3 disks:")
    moves = tower_of_hanoi(3, 'A', 'C', 'B')
    print(f"Total moves: {moves}")
