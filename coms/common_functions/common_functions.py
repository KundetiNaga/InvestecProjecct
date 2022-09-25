from pathlib import Path

parentDir = Path(__file__).parent.parent.parent # get parent directory

def readJsonFile(JSONFilePath):
    try:
        with open(JSONFilePath, 'r') as file:
            filedata = file.read()
        return filedata
    except FileNotFoundError as f:
        print('ERROR-----',str(f))

def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for result in find(key, d):
                        yield result
