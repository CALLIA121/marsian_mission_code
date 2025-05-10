from flask import Flask, render_template, request

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
