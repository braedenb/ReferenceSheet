import memoize

# The name is different here, due to the import above.
@memoize.memoize
def unbounded_knapsack(capacity, values, weights):
    if capacity is 0:
        return 0

    best_value = 0

    for value, weight in zip(values, weights):
        if weight > capacity:
            continue

        # is taking this item better than leaving it?
        take_value = value + unbounded_knapsack(capacity - weight, values, weights)
        best_value = max(best_value, take_value)

    return best_value

values = (10, 5, 2)
weights = (5, 3, 2)

print(unbounded_knapsack(42, values, weights))
