
def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', 'Soumyadip Majumder'))



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'Soumyadip', 'age': 20}

student_info(*courses, **info)