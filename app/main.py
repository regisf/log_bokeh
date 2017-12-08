import logging

from bokeh.application import Application
from bokeh.application.handlers import FunctionHandler
from bokeh.server.server import Server
from bokeh.util import logconfig

logconfig.basicConfig(level=logging.INFO, filename='the_log_file.log')
logger = logging.getLogger('THE_LOGGER')


def make_doc(doc):
    logger.info('This is a logging comment')
    doc.title = "Hello world"
    return doc


app = Application(FunctionHandler(make_doc))
server = Server({'/test': app}, port=5000)
server.start()
server.run_until_shutdown()
