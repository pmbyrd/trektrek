from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    print('Hello, world! This is the main blueprint.')