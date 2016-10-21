###
# The zero/one knapsack problem is a variant in which you can only take an item
# *once*, rather than as many times as needed
###
def zero_one_knapsack(capacity, values, weights):
    # memo[i, w] is maximum weight attainable using up (but excluding) index i
    # with max weight w, along with the items that were taken
    memo = {}
    for weight in range(capacity + 1):
        memo[ 0, weight ] = 0, tuple()

    for index, value, weight in zip(range(len(values)), values, weights):
        for current_capacity in range(capacity + 1):
            if weight > current_capacity:
                memo[index + 1, current_capacity] = memo[index, current_capacity]
            else:
                leave = memo[index, current_capacity]
                taken_new_weight = memo[index, current_capacity - weight][0] + value
                taken_new_item_list = memo[index, current_capacity - weight][1] + (index,)
                take = taken_new_weight, taken_new_item_list

                memo[index + 1, current_capacity] = max(leave, take, key=lambda x : x[0])
    return memo

values = (10, 5, 2)
weights = (5, 8, 1)
capacity = 15
result = knapsack(capacity, values, weights)
print(result[len(values), capacity])
