from collections import deque
import configparser

CONFIG_FILE_NAME = '/home/pkgone/py_exercises/config/project_env.cfg'

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    
    file_name = input("Enter config file path: ")
    if file_name is None or not file_name:
        config.read(CONFIG_FILE_NAME)
    else:
        config.read(filenames=file_name)

    with open(config['DEFAULT']['PROJECT_PATH']+'files/techcrunch.csv', "r") as f:
        for line, prevlines in search(f, 'web', 5):
            for pline in prevlines:
                print(pline, end=' ')
            print(line, end=' ')
            print('-'*20)
