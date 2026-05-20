from storage.database import save_operation, get_history, clear_history, delete_operation

def add_to_history(expression, result):
    save_operation(expression, result)

def add_operation_object(operation):
    save_operation(
        operation.get_expression(),
        operation.get_result()
    )

def load_history():
    return get_history()


def delete_history():
    clear_history()

def history_generator(records):
    for record in records:
        yield record

def delete_one_operation(operation_id):
    delete_operation(operation_id)