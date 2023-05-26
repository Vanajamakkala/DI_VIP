from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello I am  Makkala Vanaja,\n')
        self.response.out.write('I am an intern at Digirise Infolabs \n')
        self.response.out.write('and I am pursuing my B.Tech in the stream of Computer Science and Engineering in Ravindra College of Engineering for Women in Kurnool.')


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
