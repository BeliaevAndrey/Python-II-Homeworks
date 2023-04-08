import json
import os


class JsonWorks:

    @staticmethod
    def json_writer(in_dct: [list, dict],
                    output_file_name: str,
                    output_file_path: str = os.getcwd(),
                    ) -> None:
        """
         Writes to disk json file of dictionary passed
        :param in_dct: dict -- dictionary to write
        :param output_file_path: str -- path where binary file to write
        :param output_file_name: str -- file name
        :return: None
        """
        file_path = os.path.join(output_file_path, output_file_name)
        with open(file_path, 'w', encoding='utf-8') as f_out:
            json.dump(in_dct, f_out, indent=4)

    @staticmethod
    def json_reader(output_file_name: str,
                    output_file_path: str = os.getcwd(),
                    ) -> dict[str]:
        """
        Reads json file to a dictionary
        :param output_file_name: str -- filename
        :param output_file_path: str -- path to a file to be read
        :return: dict[str] -- deserialized dictionary
        """
        file_path = os.path.join(output_file_path, output_file_name)
        with open(file_path, 'r', encoding='utf-8') as f_in:
            json_dict = json.load(f_in)
        return json_dict


if __name__ == '__main__':
    print('Not for separate use')
