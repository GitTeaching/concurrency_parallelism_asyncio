from tasks import add


# Calling a task - asyncronously
# Calling a task returns an AsyncResult instance. 
result = add.delay(4, 9)

print("Continue")

print(result.ready())

print(result.get())
