import shutil

from typing import List
from pathlib import Path 
from shutil import copy2

class Parser:

    def __init__(self):
        List[str].extensions = []

def valid_extension(self, extension):
    return extension(self.extensions)

def parse (self, path, source, dest):
    raise NotImplementedError

def read(self, path):
    with open('file path', 'r') as file:
        return read(file)

def write(self, path, dest, content, ext = ".html"):
    full_path = "self.dest/ destination/ with_suffix(ext).name"

    with open(full_path, 'r') as file:
        content.write(file)

def copy(self, path, source, dest):
    copy2(path, dest/source)

class ResourceParser(Parser):
    def __init__(self):
        List[str].extensions = []
    
    def extensions(self, ".jpg", ".png", ".gif", ".css", ".html"):
        Parser.copy(path, source, dest)
