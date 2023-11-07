def brute_calculate_largest_sum(arr):
    n = len(arr)
    max_sum = 0
    a_day = 0
    d_day = 0
    for i in range(n):
        curr_sum = 0
        # for every i we check if the curr_sum is greater than max_sum and then update accordingly
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
                a_day = i
                d_day = j

    return max_sum, a_day + 1, d_day + 1

def kadane_calculate_largest_sum(arr):
    curr_sum = 0
    max_sum = -1
    a_day = 0
    d_day = 0
    temp_a_day = 0
    for i in range (len(arr)):
        curr_sum = curr_sum + arr[i]
        # if current sum becomes negative, we bring back the variable to 0
        if(curr_sum < 0):
            curr_sum = 0
            temp_a_day = i + 1
        # update max sum if the current sum exceeds this value
        if curr_sum > max_sum:
            max_sum = max(curr_sum, max_sum)
            a_day = temp_a_day
            d_day = i
    # return + 1 because index starts with 0
    return max_sum, a_day + 1, d_day + 1


def get_max_crossing_sum(arr, low, mid, high):
    # initialising the left sum to negative infinity
    l_sum = float("-inf")
    sum = 0
    left_max_index = mid
    # taking the sum from mid to low
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > l_sum:
            l_sum = sum
            left_max_index = i
    # initialising the right sum to negative infinity
    r_sum = float("-inf")
    sum = 0
    right_max_index = mid + 1
    # taking the sum from mid to high
    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > r_sum:
            r_sum = sum
            right_max_index = i
    # return the sum of left and right sub array over the crossing
    return l_sum + r_sum, left_max_index + 1, right_max_index + 1

def get_max_subarray_sum(arr, low, high):
    if low == high:
        return arr[low], low, high
    # use merger sort type divide and conquer
    mid = (low + high) // 2
    # using the left to mid in the initial call
    l_sum, l_start, l_end = get_max_subarray_sum(arr, low, mid)
    # using the mid to right in the next call
    r_sum, r_start, r_end = get_max_subarray_sum(arr, mid + 1, high)
    cross_sum, cross_start, cross_end = get_max_crossing_sum(arr, low, mid, high)

    # if the left sum is greater than the right and cross sum, return left sum
    if l_sum >= r_sum and l_sum >= cross_sum:
        return l_sum, l_start + 1, l_end + 1

    # if the right sum is greater than the left and cross sum, return right sum
    elif r_sum >= l_sum and r_sum >= cross_sum:
        return r_sum, r_start + 1, r_end + 1

    # if the cross sum is greater than the right and left sum, return cross sum
    else:
        return cross_sum, cross_start, cross_end

def divide_n_conq_calculate_largest_sum(arr):
    low = 0
    high = len(arr) - 1
    # getting the results using divide and conquer method
    max_sum, start_day, end_day = get_max_subarray_sum(arr, low, high)
    return max_sum, start_day, end_day

earnings_day = [-9, 10, -8, 10, 5, -4, -2, 5]
max_earn, a_day, d_day = brute_calculate_largest_sum(earnings_day)
print("Maximum earning found by BRUTE FORCE is {} with arrival day on {} and departing by {}".format(max_earn, a_day, d_day))

max_earn, a_day, d_day = divide_n_conq_calculate_largest_sum(earnings_day)
print("Maximum earning found by DIVIDE AND CONQUER is {} with arrival day on {} and departing by {}".format(max_earn, a_day, d_day))

max_earn, a_day, d_day = kadane_calculate_largest_sum(earnings_day)
print("Maximum earning found by KADANE'S algo is {} with arrival day on {} and departing by {}".format(max_earn, a_day, d_day))
