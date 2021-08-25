def getInfo(pkgName):
    with open("D:\\PythonProject\\PyPkgAnalysis\\bupt\\resources\\malware\\"+ pkgName + "\\setup.py", 'r') as f:
    # with open("D:\\PythonProject\\PyPkgAnalysis\\bupt\\resources\\malware\\Clase-0.1.0\\setup.py", 'r') as f:
        # print(f.read())
        lines = f.readlines()
        tag = False
        dict = {}
        for line in lines:
            if line.__contains__("setup(") and tag == False:
                # print(line)
                tag = True
            elif tag == True and line.__contains__("="):
                line = line.strip()  # 去除字符串开头和结尾的空格
                line = line.rstrip(",")  # 去除字符串右边的逗号
                # print(line)
                list = line.split("=")
                dict[list[0]] = list[1]
                # print(dict[list[0]])
        # print(dict.keys().__sizeof__())
        return dict

def getPkgName(pkgName):
    dict = getInfo(pkgName)
    pkgName = dict["name"]
    return pkgName

def getVersion(pkgName):
    dict = getInfo(pkgName)
    version = dict["version"]
    return version

def getAuthorName(pkgName):
    dict = getInfo(pkgName)
    authorName = dict["author"]
    return authorName

def getAuthorEmail(pkgName):
    dict = getInfo(pkgName)
    authorEmail = dict["author_email"]
    return authorEmail

def getUrl(pkgName):
    dict = getInfo(pkgName)
    url = dict["url"]
    return url