# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# предусмотреть условие его завершения.

from itertools import count, accumulate
import copy

for i in count(1):
    if i > 1:
        break
    else:
        result = list(accumulate(range(10)))
        print(result)

copy_result = copy.deepcopy(result)
print(copy_result)