import webapp2
import os
import jinja2
import random
import logging

jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

# ================== HANDLERS ====================
""" HANDLER INFORMATION
    url: /
    handler: IndexHandler
    frontend: /templates/index.html,            /stylesheets/index.css     """
class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index_v2.html')

        temp = {
            "username": nick,
            "log_url": log,
            "log_text": log_text,
            "dash_text": dash_text
        }
        self.response.write(template.render(temp))
# ================== OBJECTS ====================
""" OBJECT INFORMATION
"""

# ============== LINKS ===============
app = webapp2.WSGIApplication([
    ('/', IndexHandler)
], debug=True)
