class Solution:
    def corpFlightBookings(self, bookings, n: int):
        delta = ['!']+ [0]* n
        #print(delta)
        for booking in bookings:
            #print(booking)
            delta[booking[0]] += booking[2]
            if booking[1] + 1 < len(delta):
                delta[booking[1] + 1] -= booking[2]
        #print(delta)
        temp, total = 0, []
        for i in range(1, n+1):
            temp += delta[i]
            total.append(temp)
        
        return total

if __name__ == '__main__':
    sol = Solution()
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    ret = sol.corpFlightBookings(bookings, n)
    print(ret)