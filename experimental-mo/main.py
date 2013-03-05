import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/html'
      html = '<p>Experimental for automatic deployment by Jenkins.</p>'
      html += 'This application is experimental pages.'

      self.response.write(html)

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
