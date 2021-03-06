def index():
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*5
    end = page*5
    rows = db(db.blog).select(orderby =~ db.blog.created_on,limitby=(start,end))
    return locals()

@auth.requires_login()
#You can add membership to create post by only selected person
def create_post():
    form= SQLFORM(db.blog).process()
    if form.accepted:
        redirect(URL('index'))
        session.flash="Your Post was created"
    return locals()

def view_post():
    post = db.blog(request.args(0,cast=int))
    db.blog_comments.blog.default = post.id
    imgs = db(db.blog.images).select() or None
    form = SQLFORM(db.blog_comments,deletable=True).process()
    if form.accepted:
        if auth.user:
            response.flash="Your comment has been posted"
        else:
            redirect(URL('user'))
    comments = db(db.blog_comments.blog ==post.id).select(orderby=~ db.blog_comments.created_on)
    return locals()

def search():
    var = request.vars
    search = db(db.blog.title.belongs(var)).select()
    return locals()
@auth.requires_login()
def delete_comment():
    #return db(db.blog_comments.id == request.vars.id).delete()
    if (db.blog_comments.id == request.vars.id):
        db(db.blog_comments.id == request.vars.id).delete()
        response.flash="Comment deleted"
    return locals()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
