from app import app


@app.route('/helloworld', methods=['GET', 'POST'])
def helloworld():
    return '<p>Hello, World</p>'
