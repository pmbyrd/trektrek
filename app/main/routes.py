from app.main import bp as main



@main.route('/')
def index():
    return 'Hello, world! This is the main blueprint.'

@main.route('/test/')
def test_page():
   return '<h1>Testing the Flask Application Factory Pattern</h1>'
    
    
