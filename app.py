import beyangs_special_package.m
from beyangs_special_package import m
from werkzeug.utils import import_string

def run():
    beyangs_special_package.m.helloWorld()
    m.helloWorld()

def useWerkzeug():
    import_string('', silent=True)

run()
