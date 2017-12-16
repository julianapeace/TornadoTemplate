import tornado.ioloop
import tornado.web
import tornado.log

class MainHandler(tornado.web.RequestHandler):
  def get(self):
      name = "Paul" #can do backend processing
      self.set_header("Content-Type", 'text/plain')
      self.write("Hello, world") #can also be GET or POST
      self.write("<strong>Hello, world</strong>".format(name)) #can add HTML, must remove content-type header

class YouHandler(tornado.web.RequestHandler):
  def get(self, name):
    self.set_header("Content-Type", 'text/plain')
    self.write("Hello, {}".format(name))

class YouTooHandler(tornado.web.RequestHandler):
  def get(self):
    self.set_header("Content-Type", 'text/plain')
    name = self.get_query_argument('name', 'Nobody')
    self.write("Hello, {}".format(name))
    #http://localhost:8888/hello2?name=paul

class YouThreeHandler(tornado.web.RequestHandler):
  def get(self):
    self.set_header("Content-Type", 'text/plain')
    names = self.get_query_arguments('name')
    print(names) #can see this in the log
    for name in names:
      self.write("Hello, {}\n".format(name))
      #http://localhost:8888/hello3?name=paul&name=joan&name=narf
      #get_query_arguments is plural. And it generates a python list. It is printable.

def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
    (r"/hello/(.*)", YouHandler),
    (r"/hello2", YouTooHandler),
    (r"/hello3", YouThreeHandler),
  ], autoreload=True)

if __name__ == "__main__":
      tornado.log.enable_pretty_logging()

      app = make_app()
      app.listen(8888, print('Server on localhost:8888'))
      tornado.ioloop.IOLoop.current().start() #creates infinite loop for requests

#YouHandler is creating a URL with set parameters
#YouTOOHandler is creating a URL that parses through. pro: you can set defaults
