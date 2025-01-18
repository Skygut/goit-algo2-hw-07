import random
import time
from functools import lru_cache


# Functions without cache
def range_sum_no_cache(array, L, R):
    return sum(array[L : R + 1])


def update_no_cache(array, index, value):
    array[index] = value


# Functions with LRU cache
@lru_cache(maxsize=1000)
def range_sum_with_cache(array_tuple, L, R):
    array = list(array_tuple)
    return sum(array[L : R + 1])


def update_with_cache(array, index, value):
    array[index] = value
    range_sum_with_cache.cache_clear()


# Test setup
N = 100_000
Q = 50_000
array = [random.randint(1, 100) for _ in range(N)]
queries = []
for _ in range(Q):
    if random.choice([True, False]):
        L, R = sorted(random.sample(range(N), 2))
        queries.append(("Range", L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 100)
        queries.append(("Update", index, value))

# Benchmark without cache
start_no_cache = time.time()
for query in queries:
    if query[0] == "Range":
        range_sum_no_cache(array, query[1], query[2])
    elif query[0] == "Update":
        update_no_cache(array, query[1], query[2])
end_no_cache = time.time()

# Reset cache
range_sum_with_cache.cache_clear()
array_tuple = tuple(array)

# Benchmark with cache
start_with_cache = time.time()
for query in queries:
    if query[0] == "Range":
        range_sum_with_cache(array_tuple, query[1], query[2])
    elif query[0] == "Update":
        update_with_cache(array, query[1], query[2])
        array_tuple = tuple(array)
end_with_cache = time.time()

# Results
print(f"Execution time without cache: {end_no_cache - start_no_cache:.2f} seconds")
print(f"Execution time with LRU cache: {end_with_cache - start_with_cache:.2f} seconds")
