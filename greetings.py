from datetime import datetime

name = input("Enter your name: ")
current_time = datetime.now().strftime("%H:%M:%S")

print(f"Hello, {name}!")
print(f"Current time: {current_time}")