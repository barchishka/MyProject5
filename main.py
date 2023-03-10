file_list = ['1.txt', '2.txt', '3.txt']
new_txt = ['1_1.txt', '2_1.txt', '3_1.txt']
new_dictionary = []
step = 0
while step < len(file_list):
    with open(file_list[step], encoding='UTF-8') as f:
        data = f.readlines()
        file_str = len(data)
    with open(file_list[step], encoding='UTF-8') as f:
        data_text = f.read()

    with open(new_txt[step], 'w', encoding='UTF-8') as f:
        f.write(f'{file_list[step]}\n')
        f.write(f'{file_str}\n')
        f.write(f'{data_text}\n')
    step += 1
for some_file in new_txt:
    with open(some_file, encoding='UTF-8') as f:
        new_data = f.read()
        new_dictionary.append(new_data)
new_dictionary.sort(key=len)
sorted(new_dictionary, key=len)
print(new_dictionary)

with open('book.txt', 'a', encoding='UTF-8') as f:
    for some_pat in new_dictionary:
        f.write(f'{some_pat}')
