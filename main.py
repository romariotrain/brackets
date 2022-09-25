from decorator import decorator


class Stack():

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        pop_result = self.stack.pop()
        return pop_result

    def peek(self):
        if self.stack != []:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


pairs = {']' : '[', '}' : '{', ')' : '('}
s = Stack()


@decorator
def check_brackets(brackets):
    brackets_list = list(brackets)
    for bracket in brackets_list:
        if bracket in pairs.values():
            s.push(bracket)
        elif not s.isEmpty():
            if bracket in pairs:
                if s.peek() == pairs[bracket]:
                    s.pop()
                else:
                    return False
            else:
                return 'Не скобка'
        else:
            return False
    return s.isEmpty()


if __name__ == '__main__':
    print(check_brackets('((([(]))))'))


