from flask import Flask
from flask import render_template
from flask import request
import prepods as p
import os 
from flask import send_from_directory

class App():
    def __init__(self):
        self.app = Flask(__name__)

        from werkzeug.utils import secure_filename

        # папка для сохранения загруженных файлов
        UPLOAD_FOLDER = '/home/ccat/prog/sites/codzen/codzen/codzen/files/files/works'
        # расширения файлов, которые разрешено загружать
        ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

        self.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


        @self.app.route('/upload/', methods=['POST', 'GET'])
        def upload():
            if request.method == 'POST':
                c = request.form.get('filee')
                return send_from_directory(self.app.config['UPLOAD_FOLDER'], c)
            elif request.method == 'GET':
                return 'ok'
                

        @self.app.route('/')
        def Home():
            return render_template('other/Home.html') , 200

        @self.app.route('/add')
        def Add():
            return render_template('other/Add.html', context=p.f) , 200

        @self.app.route('/regedit')
        def Registration():
            return render_template('other/Reg.html') ,200

        @self.app.errorhandler(404)
        def not_found(error):
            return render_template('other/error.html', context='404 | Страница не найдена'), 404

        @self.app.route('/search', methods=['GET', 'POST'])
        def Search():
                if request.method == 'POST':
                    s = request.form.get('f')
                    return render_template('other/Search.html', context=s)
                elif request.method == 'GET':
                    return render_template('other/error.html', context='Ошибка запроса'), 403

        self.app.run(port=80, host='0.0.0.0')

App()
