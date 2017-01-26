#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2;import caesar;import cgi
# html boilerplate for the top of every page

title = "Web Caesar"
header = "Web Caesar"

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>{}</title>
</head>
<body>
    <h1>{}</h1>
    """.format(title,header)

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
header_2 = '<h2>Enter some text to encrypt</h2>'
encrypt = caesar.encrypt

def build_page(textarea_content):
    rot_label = "<label> Rotate by: </label>"
    rotation_input = "<input type='number' name='rotation'>"

    message_label = "<label> Enter some text to encrypt: </label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>" + (2 * ("</br>"))
    submit = "<input type='submit' value='Encrypt'/>"
    form = "<form method='post'>" + rot_label + rotation_input + (
    2 * ("</br>")) + message_label + textarea + submit + "</form>"

    return page_header + form + page_footer


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))

        encryted_message = encrypt(message, rotation)
        escaped_message = cgi.escape(encryted_message)
        content = build_page(escaped_message)

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
