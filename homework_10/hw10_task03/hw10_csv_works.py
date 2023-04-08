import csv
import os


class CsvWorks:

    @classmethod
    def csv_reader(cls,
                   input_file_path: str,
                   input_file_name: str,
                   ) -> list[dict[str]]:
        """
        Reads a csv-file with headers to list of dicts
        :return: list[dict[str]]
        """
        out_dict_list = []
        input_file = os.path.join(input_file_path, input_file_name)
        with open(input_file, 'r', encoding='utf-8') as f_in:
            print(f'Are these ones headers:\n {f_in.readline()}')
            f_in.seek(0)
            while True:
                answer = input('[Y/N]: ').lower()
                if answer in ['y', 'n']:
                    break
                else:
                    print("'Y' or 'N' Only, please.")
            if answer == 'y':
                read_csv = csv.DictReader(f_in, dialect='excel', delimiter=';')
                keys = read_csv.fieldnames
                for row in read_csv.reader:
                    out_dict_list.append({key: item for key, item in zip(keys, row)})
            else:
                read_csv = csv.reader(f_in, dialect='excel', delimiter=';')
                for row in read_csv:
                    if len(row) == 2:
                        out_dict_list.append({row[0]: row[1]})
                    else:
                        out_dict_list.append({row[0]: {row[1]: row[2:]}})
        return out_dict_list

    # @classmethod
    # def csv_reader(cls,
    #                input_file_path: str,
    #                input_file_name: str,
    #                ) -> list[dict[str]]:
    #     """
    #     Reads a csv-file with headers to list of dicts
    #     :return: list[dict[str]]
    #     """
    #     out_dict_list = []
    #     input_file = os.path.join(input_file_path, input_file_name)
    #     with open(input_file, 'r', encoding='utf-8') as f_in:
    #         read_csv = csv.reader(f_in, dialect='excel', delimiter=';')
    #         keys = (next(read_csv))
    #         print('Keys:', keys)
    #         for row in read_csv:
    #             out_dict_list.append({key: item for key, item in zip(keys, row)})
    #     return out_dict_list
    #
    @classmethod
    def csv_writer(cls, in_dct: [list[dict], dict],
                   output_file_path: str,
                   output_file_name: str,
                   ) -> None:
        """
         Writes to disk a csv-file of dictionary passed, ";" used as delimiter
        :param output_file_name: str    -- a file to write to
        :param output_file_path: str    -- working dir, current by default
        :param in_dct: dict -- dictionary to write
        :return: None
        """
        output_file = os.path.join(output_file_path, output_file_name)
        if isinstance(in_dct, list):
            data = cls._form_lst_values_to_cols(in_dct)
        else:
            data = cls._form_lst_values_to_rows(in_dct)
        with open(output_file, 'w', encoding='utf-8') as f_out:
            write_csv = csv.writer(f_out, dialect='excel', delimiter=';')
            write_csv.writerows(data)

    @staticmethod
    def _form_lst_values_to_cols(data_lst: list[dict]) -> list[list[str, int]]:
        """
        Converts a list of dicts to a table (list of lists)
        :param data_lst: list[dict]  -- list of dicts of a same structure
        :return: list[str, int]
        """
        out_lst = [[i_key for i_key in data_lst[0].keys()]]
        for dct in data_lst:
            out_lst.append([*dct.values()])
        return out_lst

    @staticmethod
    def _form_lst_values_to_rows(in_dct: dict[dict]) -> list[list[str, int]]:
        """
        Converts a dict of dicts to a table (list of lists)
        values are placed in rows:
        { key0: {keyA: b, keyC: d} } -> [[key0, keyA, b], [key0, keyC, d]]
        :param in_dct: dict[dict]  -- list of dicts of a same structure
        :return: list[str, int]
        """
        out_lst = []
        for i_key, i_val in in_dct.items():
            if isinstance(i_val, dict):
                for j_key, j_val in i_val.items():
                    out_lst.append([i_key, j_key, j_val])
            else:
                out_lst.append([i_key, i_val])

        return out_lst


if __name__ == '__main__':
    print('Not for separate use')
