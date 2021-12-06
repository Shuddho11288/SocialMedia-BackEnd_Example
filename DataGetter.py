from DataEnter import DataEnterProcess, JSONEditor

x = DataEnterProcess({"name": "Shuddho", "text": "Hello This is a test"})
x.save()
engine = JSONEditor("database.json")

print(engine.read())

import random

n = random.randint(1, len(engine.read()))
print(n)
print(engine.read()[str(n)])

#engine.remove_items(['1'])
#print(engine.read())

time = "Your Time"
is_deleted = False
delete_index = None
for x,y in engine.read().items():
    if y["time"] == time:
        delete_index = x
        engine.remove_items([str(delete_index)])
        is_deleted = True
        break
if not is_deleted:
    print("Not Found")
