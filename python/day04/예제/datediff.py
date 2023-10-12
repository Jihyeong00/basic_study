import datetime

x = datetime.datetime(2022, 9, 1)
y = datetime.datetime.now()

delta = y - x

print(f"만난 일: {str(x)}")
print(f"현재: {str(y)}")
print(f"만난 일: {str(delta.days)}")
