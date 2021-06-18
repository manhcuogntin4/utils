import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join


def getFilesInDir(dir_path):
    file_list = []
    for filename in glob.glob(dir_path + '/*.txt'):
        file_list.append(filename)

    return file_list

DIR_PATH = "test"
list_file = getFilesInDir(DIR_PATH)
for filename in list_file:
    with open(filename, "r") as fp:
        lines = fp.readlines()
        fp.close()
    new_file = open(filename, "w")
    for line in lines:
        if line.split()[0]!="0":
            new_file.write(line)

    new_file.close()