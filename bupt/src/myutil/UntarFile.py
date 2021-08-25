import tarfile

def untarFile(filename,dirs):
    """filename 被解压文件的路径
       dirs 文件解压后存放的路径"""
    t = tarfile.open(filename)
    t.extractall(path=dirs)
    # t.extract(member=filename,path=dirs)


filename = "D:\\PythonProject\\PyPkgAnalysis\\bupt\\resources\\nonmalware\\czgbyer_example_pkg-0.0.1.tar.gz"
dirs = "D:\\PythonProject\\PyPkgAnalysis\\bupt\\resources\\nonmalware"

untarFile(filename,dirs)