import re


def read():
    f = open("dictionary.csv", "rb")
    csv = f.read()
    return csv


if __name__ == '__main__':
    # csv = read()
    #
    # name = []
    #
    # for s in csv.split(b'\r\n'):
    #     arr = re.split(",", s.decode('utf-8'))
    #     if len(arr) > 1:
    #         name.append(arr[1])
    #     print(arr)
    # print(name)
    
    colName = "[Nid, Original ID, Name, Project acronym, Visual, Project description, Results, Coordinators, Partners, Project address(es), Project postal code(s), Project town(s), Project country(ies), Project location latitude, Project location longitude, Link to a video, Timeframe start, Timeframe end, Project webpage, Related links, EU Budget MFF heading, Programme name, Funding area, EC’s priorities, EU Budget contribution, Total project budget, Author, Language]"
    dataType = """java.lang.Integer
java.lang.String
java.lang.String
java.lang.String
java.lang.String
java.lang.String
java.lang.String
java.lang.String
com.example.progetto.StringArray
com.example.progetto.StringArray
com.example.progetto.StringArray
com.example.progetto.StringArray
com.example.progetto.StringArray
com.example.progetto.FloatArray
com.example.progetto.FloatArray
java.lang.String
java.lang.String
java.lang.String
java.lang.String
com.example.progetto.StringArray
java.lang.String
java.lang.String
com.example.progetto.StringArray
com.example.progetto.StringArray
java.lang.Integer
java.lang.Integer
java.lang.String
java.lang.String"""
    
    colName = colName.replace("[", '')
    colName = colName.replace("]", '')
    arr = colName.split(", ")
    s = []
    for a in arr:
        s.append(a.replace("(", "").replace(")", "").replace("’", "").title().replace(" ", ""))
    colName = []
    for a in s:
        colName.append(a[:1].lower() + a[1:])
    
    dataType = dataType.split('\n')
    
    for d, c in zip(dataType, colName):
        print("private " + d + " " + c + ";")

    print("{", end="")
    for c in dataType:
        print('"' + c + '"' + ", ", end="")
    print("}", end="")
