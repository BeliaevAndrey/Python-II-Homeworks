# 3. В большой текстовой строке подсчитать количество встречаемых слов и
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re

source = dir.__doc__

pattern = re.compile("[\\[\\]()<>_\",.?!;:-]")

string = source.replace('\n', ' ').replace("'s", '').lower()
string = ''.join(ch if ch not in pattern.findall(string) else ' ' for ch in string).split()

frequency_sort = set(string)

frequency_sort = sorted(frequency_sort, key=lambda w: string.count(w), reverse=True)

print('\n'.join(frequency_sort[:10]))
