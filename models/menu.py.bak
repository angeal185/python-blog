# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################


response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'ben eaves <angeal185@github.com>'
response.meta.description = 'python personal blog'
response.meta.keywords = 'blog, python'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
]

if auth.user:
    response.menu.append((T('Creat Post'), False, URL('default', 'create_post')))
if "auth" in locals(): auth.wikimenu()
