from CH07L05_stack import Stack


def is_balanced(input_str: str) -> bool:
    s = Stack()
    for i in input_str:
        if i == ")":
            if s.size() == 0:
                return False
            s.pop()
        else:
            s.push(i)
    return s.size() == 0

