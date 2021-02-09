# data = [4, 5, 6, 7, 8, 101, 223, 343, 43, 454, 345, 534, 133,
#       232, 343, 432, 113, 445, 541, 312, 434, 113, 345]
# data = [4, 5, 6, 7, 8, 101, 223, 343, 43, 454, 345, 534, 133,
#            232, 343, 432, 113, 445, 541, 312, 434, 113, 345]
# data = [ 6, 7, 8, 101, 223, 343, 43, 454, 345, 534, 133,
#              232, 343, 432, 113, 445, 541, 312, 434, ]
data = []
min_valid = 100
max_valid = 200

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)
del data[start:]
print(data)
