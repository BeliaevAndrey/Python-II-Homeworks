import pickle
import os


class PickleWorks:

    @staticmethod
    def pickle_writer(in_dct: [list[dict], dict],
                      output_file_path: str,
                      output_file_name: str,
                      ) -> None:
        """
         Writes to disk binary file of dictionary passed
        :param output_file_path:  str -- path where binary file to write
        :param output_file_name:  -- file name
        :param in_dct: dict -- dictionary to write
        :return: None
        """
        file_path = os.path.join(output_file_path, output_file_name)
        with open(file_path, 'wb') as f_out:
            pickle.dump(in_dct, f_out)

    @staticmethod
    def pickle_reader(input_file_path: str,
                      input_file_name: str,
                      ) -> list[dict[str]]:
        """
        Reads binary file to a list of dictionaries
        :param input_file_path: str    -- path to a file to be read
        :param input_file_name: str
        :return: list[dict[str]]
        """
        file_path = os.path.join(input_file_path, input_file_name)
        with open(file_path, 'rb') as f_in:
            out_lst = pickle.load(f_in, encoding='utf-8')
        return out_lst


if __name__ == '__main__':
    print('Not for separate use')
