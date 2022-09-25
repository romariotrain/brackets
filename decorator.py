def decorator(function):
    def wrapper(*args, **qwargs):
        if function(*args, **qwargs) == True:
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'
    return wrapper

