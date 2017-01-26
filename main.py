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
import webapp2;import caesar
# html boilerplate for the top of every page

title = "Web Ceasar"
header = "Web Ceasar"

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

encrypt = caesar.encrypt

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header_2 = '<h2>Enter some text to encrypt</h2>'

        encrypt_form = """
               <form method="post">
                    <input type="textarea" name="text"/>

                    <input type="submit" value="Encrypt"/>
               </form>
               """

        message = 'Hello world!'


        encryted_message = encrypt(message,13)
        encryted_paragraph = '<p>' + encryted_message + '</p>'

        content = page_header + header_2 + encryted_paragraph + page_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
