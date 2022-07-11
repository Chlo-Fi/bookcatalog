from app import create_app, db

if __name__ == '__main__':
    print('Attempting to run app...')
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
    flask_app.run()

