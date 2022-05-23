size = 10
queue = [None for i  in range(size)]
startpointer = 0
endpointer = 0


def enqueue(newdata):
    global endpointer
    if startpointer == endpointer and queue[startpointer] is not None:
        print('queue is full')

    else:
        queue[endpointer] = newdata
        endpointer = endpointer + 1
        if endpointer == size:
            endpointer == 0

    print(queue)

def dequeue():
    if startpointer == endpointer and queue[startpointer] is None:
        print('nothing to dequeue, queue is empty')

    else:
        remove = queue[endpointer]
        queue[startpointer] = None

        startpointer = startpointer + 1
        if startpointer == size:
            startpointer = 0

    print(queue)


