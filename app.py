import mypkg
from werkzeug.utils import import_string

def run():
    mypkg.helloWorld()

def useWerkzeug():
    import_string('', silent=True)

run()
