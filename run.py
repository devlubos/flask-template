from waitress import serve
from app import create_app

application = create_app()

mode = 'dev'

if __name__ == '__main__':
    if mode == 'dev':
        application.run(port=5000, debug=True)
    else:
        serve(application, host='0.0.0.0', port=5000, threads=2)
