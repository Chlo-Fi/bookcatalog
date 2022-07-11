from app import create_app

if __name__ == '__main__':
    print('Attempting to run app...')
    flask_app = create_app('dev')
    flask_app.run()
