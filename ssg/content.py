import re

from yaml import load
from yaml.loader import FullLoader 

from collections.abc import Mapping

class Content:
    def __init__(self, Mapping):
        __delimiter = "^(?:-|\+){3}\s*$"
        __regex = re.compile(__delimiter, re.MULTILINE)

        @classmethod
        def load(cls, string):
            __regex.split(string, 2) = (_, fm, Loader=FullLoader)
            return cls(metadata, content)
        

