from storage.database import save, load, clear

def add_history(expression,result):
    save(expression,result)

def get_history():
    return load()

def clear_history():
    clear()

def history_generator(records):
    for record in records:
        yield record