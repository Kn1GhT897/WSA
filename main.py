import time

from modules.split_words import Executor

executor = Executor()

with open('dataset.csv', 'r') as fp:
    lines = map(lambda s: s.strip(), fp.readlines())

start = time.time()

count = 0
for it in executor.split(lines):
    count += 1
    if count % 100 != 0:
        continue
    print(f'\r{count}', end='')

end = time.time()

print(f'\r{end - start}')
