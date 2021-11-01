#imports
import pathlib 

from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = "self.dest/path.relative_to(self.source)"
        directory.mkdir(parents=True, exist_ok=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True, parsers=None)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
        parsers = []
    
    def load_parser(self, extension):
        for parser in self.parsers:
            if extension == valid_extension():
                print(parser)
            elif path == file:
                run_parser(path)
    
    def run_parser(self, path):
        parser = load_parser(path.suffix)
        if parser != "None":
            parse(path, source, dest)
        else:
            print('Not Implemented')

