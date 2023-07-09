# Напишите функцию группового переименования файлов. Она должна:
#   принимать параметр желаемое конечное имя файлов. При переименовании
#       в конце имени добавляется порядковый номер.
#   принимать параметр количество цифр в порядковом номере.
#   принимать параметр расширение исходного файла. Переименование должно
#       работать только для этих файлов внутри каталога.
#   принимать параметр расширение конечного файла.
#   принимать диапазон сохраняемого оригинального имени. Например для
#       диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#       К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os


def grp_rename(number_digits_amt: int,
               src_extension: str,
               origin_range: tuple[int, int],
               dst_extension: str = '',
               dst_file_name: str = '',
               ) -> list[tuple[str, str]]:
    counter = 0
    files_processed = []
    for file in os.listdir():
        if os.path.isfile(file) and len(curr_file := file.rsplit('.')) == 2:
            if not dst_extension:
                dst_extension = src_extension
            if file.endswith('.' + src_extension):
                counter += 1
                number = f'{counter:0>{number_digits_amt}}'
                new_name = curr_file[0].replace('.', '')[origin_range[0]: origin_range[1]]
                new_name = f'{new_name}{dst_file_name}{number}.{dst_extension}'
                os.replace(file, new_name)
                files_processed.append((file, new_name))
    return files_processed


def main():
    os.chdir('/home/andrew/Documents/geekbrains/Python2023/Homeworks/homework_07/out_dir_task02')
    result = grp_rename(number_digits_amt=4,
                        src_extension='ext2',
                        origin_range=(3, 6),
                        dst_extension='ext3',
                        )
    print(''.join([f'File: {item[0]} moved to: {item[1]}\n' for item in result]))

    result = grp_rename(number_digits_amt=4,
                        src_extension='other',
                        origin_range=(6, 16),
                        dst_extension='ext001',
                        )
    print(''.join([f'File: {item[0]} moved to: {item[1]}\n' for item in result]))


if __name__ == '__main__':
    main()
