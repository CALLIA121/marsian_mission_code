from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/img'


@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', 'Колонизация Марса')
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    prof_lower = prof.lower()
    print(prof_lower)

    if 'инженер' in prof_lower or 'строитель' in prof_lower:
        header = "Инженерные тренажеры"
        image = "img/engineering_scheme.png"
    else:
        header = "Научные симуляторы"
        image = "img/science_scheme.png"

    return render_template(
        'training.html',
        header_text=header,
        image_path=image
    )


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = [
        "Инженер-робототехник",
        "Пилот марсохода",
        "Космический биолог",
        "Строитель куполов",
        "Специалист по системам жизнеобеспечения",
        "Геолог-исследователь",
        "Метеоролог",
        "Врач-космонавт"
    ]

    list_type = list.lower()
    valid_types = {'ol', 'ul'}

    return render_template(
        'list_prof.html',
        list_type=list_type,
        professions=professions,
        valid_types=valid_types
    )


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    form_data = {
        'title': 'Анкета кандидата',
        'surname': 'Иванов',
        'name': 'Марсианин',
        'education': 'высшее космическое',
        'profession': 'пилот марсохода',
        'sex': 'male',
        'motivation': 'Хочу стать первым колонизатором Марса!',
        'ready': 'yes'
    }
    return render_template('auto_answer.html', data=form_data)


@app.route('/upload_photo')
def upload_photo():
    return render_template('upload_photo.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'photo' not in request.files:
        return redirect(url_for('upload_photo'))

    file = request.files['photo']
    if file.filename == '':
        return redirect(url_for('upload_photo'))

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return render_template('upload_photo.html', photo_url=file_path)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)
