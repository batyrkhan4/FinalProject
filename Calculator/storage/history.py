from storage.database import save, load, clear

def add_history(expression,result):
    save(expression,result)

def get_history():
    return load()

def clear_history():
    clear()