from bokeh.application import Application
from bokeh.application.handlers import FunctionHandler
from bokeh.server.server import Server


def make_doc(doc):
    return doc


app = Application(FunctionHandler(make_doc))
server = Server({'/test', app})
server.start()
server.run_until_shutdown()