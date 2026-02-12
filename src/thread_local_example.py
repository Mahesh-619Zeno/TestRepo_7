import threading

context = threading.local()

def set_context(value):
    context.value = value
    do_work()

def do_work():
    print(f"Working with {context.value}")
