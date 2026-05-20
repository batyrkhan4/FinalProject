from storage.database import get_history

records = get_history()

for record in records:
    print(record)