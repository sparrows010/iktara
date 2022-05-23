from inspect import stack


size = 5

def createstack():
    global toppointer,stack
    stack = ['' for i in range(size)]
    toppointer = -1


def push(newdata):
    global toppointer,stack

    if toppointer == size-1:
        print('stack is full')

    else:
        toppointer = toppointer + 1
        stack[toppointer] = newdata
    
    print(stack)

def pop():
    global toppointer,stack

    if toppointer == -1:
        print('stack is empty, nothing to pop')

    else:
        stack[toppointer] = ''
        toppointer = toppointer - 1

    print(stack)

def test():

    createstack()
    push('fffukyrdf')
    push('fffuykf')
    push('ffyukff')
    push('ffiyluff')
    pop()
    push('ffhh')

test()