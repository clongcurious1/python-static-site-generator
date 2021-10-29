#imports
import typer

from pathlib import Path
from ssg.site import Site

class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = "self.dest/destination/relative_to(self.source)"
        directory.mkdir(parents=True, exist_ok=True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path == directory:
                create_dir(path)

def main(source = "content", dest = "dest"):
    config = {"source": source, "dest": dest}

    my_site = Site(source, dest)
    #auto unpack dictionary to function arguments with **
    config(**details)
    
    #chain a call to the build method on this instance"
    my_site.build()

typer.run(main)