
def corpFlightBookings(bookings, n):
    res = [0] * (n+1)  # Flights go from 1 to n
    for first, last, seats in bookings:
        res[first] += seats  # Range starts
        if last < n:
            res[last+1] -= seats  # Range ends
    _sum = 0
    for i in range(n+1):
        _sum += res[i]
        res[i] = _sum
    return res[1:]



print(corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))  # [10,55,45,25,25]
print(corpFlightBookings(bookings=[[1, 2, 10], [2, 2, 15]], n=2))  # [10,25]
