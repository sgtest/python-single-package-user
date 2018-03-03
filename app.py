import mypkg.m
from mypkg import m
from werkzeug.utils import import_string

def run():
    mypkg.m.helloWorld()
    m.helloWorld()

def useWerkzeug():
    import_string('', silent=True)

run()
