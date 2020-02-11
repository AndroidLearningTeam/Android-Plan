# --** coding="UTF-8" **--

import os
import re
import sys
import shutil
import zipfile

currentpath = os.getcwd()
previouspath = os.path.abspath(os.path.dirname(os.getcwd()))
pos_unzip = os.getcwd()
Type = "AndroidManifest.xml"

file_list = []
for file in os.listdir(currentpath):
    file_list.append(file)

bat_name = "temp.bat"
bat_path = previouspath + "\\" + bat_name
## /r 后接目录 app
s1 = """for %%a in (*.xml) do @java -jar AXMLPrinter2.jar "%%a" >>"%%a".txt """


def change_zip():
    for fileName in file_list:
        print(fileName)
        pat = ".+\.(apk)"
        pattern = re.findall(pat, fileName)
        if pattern == []:
            continue
        os.rename(fileName, fileName.replace(".apk", ".zip"))
        os.chdir(currentpath)
        sys.stdin.flush()

def unzip(filename):

    if (filename.find(".zip")) == -1:
        return
    zip_file = zipfile.ZipFile(filename)
    a_name = zip_file.namelist()
    for names in a_name:
        if (names.find(Type)) > -1:
            try:
                zip_file.extract(names, pos_unzip)
                os.rename(names, filename.replace(".zip", "") + names)
            except:
                print(filename + " wrong")
                return
    print (filename + "解压完成! ")

if __name__ == '__main__':
    change_zip()
    for file_name in file_list:
        if (file_name.find(".zip") != -1):
            unzip(file_name)

   

    with open(bat_path, "w+") as ft:
        print(bat_path)
        
        ft.write(s1)
    os.system(bat_path)
    