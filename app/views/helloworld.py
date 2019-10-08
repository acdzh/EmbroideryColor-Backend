from app.views import view


@view.route('/helloworld', methods=['GET', 'POST'])
def helloworld():
    return '<p>Hello, World</p>'
