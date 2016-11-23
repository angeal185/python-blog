# -*- coding: utf-8 -*-

db.define_table('blog',Field('title',requires=IS_NOT_EMPTY()),
               Field('body','text',notnull=True,represent=lambda text,row:XML(text.replace('n','<br/>'),sanitize=True,permitted_tags=['br/'])),
               Field('images','upload'),
               auth.signature)
db.define_table('blog_comments',Field('blog','reference blog',readable=False,writable=False),
               Field('body','text',requires=IS_NOT_EMPTY()),
               auth.signature)
