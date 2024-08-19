
def averageWaitingTime(customers):
    n = len(customers)
    waiting_time_sum, chef_finish = 0, 0
    for customer in customers:
        if chef_finish <= customer[0]:
            chef_finish = customer[0] + customer[1]
            waiting_time_sum += customer[1]
        else:
            chef_finish += customer[1]
            waiting_time_sum += (chef_finish - customer[0])
    return round(float(waiting_time_sum) / n, 5)


print(averageWaitingTime([[1, 2], [2, 5], [4, 3]]))  # 5
print(averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))  # 3.25
