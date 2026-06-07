"""
Lab Session 5B - Question 1: Recursive Problem Solving - SOLUTION
YZM1022 Advanced Programming
"""


def tower_of_hanoi(n, src, dst, aux):
    """Solve Tower of Hanoi for n disks.
    Print each move as "Move disk from {src} to {dst}" and return the
    total number of moves made."""
    if n == 1:
        print(f"Move disk from {src} to {dst}")
        return 1
    # Move n-1 disks out of the way, move the big disk, then move n-1 back
    moves = tower_of_hanoi(n - 1, src, aux, dst)
    print(f"Move disk from {src} to {dst}")
    moves += 1
    moves += tower_of_hanoi(n - 1, aux, dst, src)
    return moves


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Tower of Hanoi ===")

    print("\nMoves for 3 disks:")
    moves = tower_of_hanoi(3, 'A', 'C', 'B')
    print(f"Total moves: {moves}")
