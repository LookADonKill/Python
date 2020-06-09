import time

titik = "."
for x in range(4):
    for y in range(1,4):
        print(f'Loading{titik * y}')
        time.sleep(0.5)