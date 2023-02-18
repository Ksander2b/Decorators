import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        log_data = f''' 
        Дата и время вызова функции - {datetime.datetime.now()}\n 
        Имя функции - {old_function.__name__}\n 
        Аргументы - {args}, {kwargs}\n 
        Результат функции - {result}\n'''
        with open('task_3/main.log', 'a') as f:
            f.writelines(log_data)
        return result

    return new_function