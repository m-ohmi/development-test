# -*- coding:utf-8 -*-

import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/html'
      self.response.write('<p>Experimental for DEV@Cloud Jenkins.</p>')
      self.response.write('This application is depolied to Google App Engine by Jenkins on DEV@Cloud')


app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
