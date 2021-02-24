import bisect

class ExamRoom:
    def __init__(self, N: int):
        self.num_pos = N
        #self.queue = OrderedDict()
        #self.queue = deque()
        self.queue = []

    def seat(self) -> int:
        #print(self.queue)
        if len(self.queue) == 0:
            pos = 0
        else:
            #for left, right in zip(self.queue, self.queue[1:]):
            d = -float('inf')
            for left, right in zip(self.queue, self.queue[1:]):
                if (right - left) // 2 > d:
                    d = (right - left) // 2
                    #pos = left + (right - left) // 2
                    pos = (left + right) // 2

            ### check start first
            if self.queue[0] - 0 >= d:
                pos = 0
                d = self.queue[0] - 0
            ### end
            if self.num_pos-1-self.queue[-1] > d:
                pos = self.num_pos-1
                d = self.num_pos-1-self.queue[-1]
                
            #self.queue.append(pos)
            #bisect.insort_right(self.queue, pos)
        bisect.insort(self.queue, pos)
        return pos

    def leave(self, p: int) -> None:
        self.queue.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
if __name__ == '__main__':
    examRoom = ExamRoom(10)
    print(examRoom.seat())
    print(examRoom.seat())
    print(examRoom.seat())
    print(examRoom.seat())
    examRoom.leave(4)
    print(examRoom.seat())
    #print(examRoom.queue)