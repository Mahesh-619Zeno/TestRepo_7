from order_service import process_orders
from thread_tasks import run_task
from resource_handler import copy_file
from thread_local_example import set_context

if __name__ == "__main__":
    items = ['apple', 'banana', 'orange']
    process_orders(items)

    run_task()

    try:
        copy_file('input.txt', 'output.txt')
    except Exception:
        pass

    set_context('user-session')
