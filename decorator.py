### decorator ###
def function(func):
    def wrapper(*args, **kwargs):
        print('dec wrapper start')
        func(*args, **kwargs)
        print('dec wrapper end')
    return wrapper

@function
def print_function(a, b="print_function"):
    print(a)
    print(b)


### function wrapping ###
def function_wrap(func):
    def wrapper(*args, **kwargs):
        print('wrapper start')
        func(*args, **kwargs)
        print('wrapper end')
    return wrapper


def print_me(a, b="print_me_function"):
    print(a)
    print(b)

### function object ###
def function_object():
    print('Called function object')

def function_aufruf(call_function):
    call_function()


if __name__ == '__main__':
    # zeigt, dass function objekte sind
    # print(function_object())

    # zeigt, dass functionen diese function objekte als parameter haben können
    # function_aufrug(function_object)

    # zeigt, dass funktionen in funktionen gepackt werden können
    function_wrap(print_me) # nichts passiert, denn ist wie function ohne ()-Call
    function_wrap(print_me)('print meeeeee') # die zweite () startet den call

    print_function('zuerst wird function und wrapper aufgerufen')


