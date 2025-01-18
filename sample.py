import random
import statistics

def calculation_of_consecutive_heads(n):
    flips = 0
    consecutive_heads = 0
    while consecutive_heads < n:
        flips += 1
        if random.random() < 0.5:  # Heads
            consecutive_heads += 1
        else:  # Tails
            consecutive_heads = 0
    return flips

def final_output(n, num_tri=500):
    results = [calculation_of_consecutive_heads(n) for _ in range(num_tri)]
    mean = statistics.mean(results)

    print("Number of trials:", num_tri)
    print(f"Mean flips required:", mean)


if __name__ == "__main__":
    n = 6
    final_output(n)