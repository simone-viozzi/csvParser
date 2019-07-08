import re


def read():
    f = open("eu_results.csv", "rb")
    csv = f.read()
    return csv


if __name__ == '__main__':
    csv = read()
    
    for s in csv.split(b'\r\n'):
        arr = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", s.decode('utf-8'))
        print(arr)
