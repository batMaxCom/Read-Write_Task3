import os

BASE_PATH = os.getcwd()
dirname = 'text_file'
dirfiles = os.listdir(dirname)

sorted_dict = {}

def file_sorted (file_list):
    file_dict = {}
    for files in file_list:
        fullpaths: str = os.path.join(BASE_PATH, dirname, files)
        with open(fullpaths, encoding='utf-8') as file:
            date = file.readlines()
            file_dict.update({fullpaths: len(date)})
    sorted_values = sorted(file_dict.values())
    for i in sorted_values:
        for key in file_dict.keys():
            if file_dict[key] == i:
                sorted_dict[key] = file_dict[key]
                break
    s_file = open('sort.txt', 'w', encoding='utf-8')
    for sort in sorted_dict.items():
        file_name = os.path.basename(sort[0])
        s_file.write(f'{file_name}\n{sort[1]}\n')
        for i in range(sort[1]):
            i = i+1
            s_file.write(f'Строка номер {i} файла номер {os.path.splitext(file_name)[0]}\n')


file_sorted(dirfiles)
