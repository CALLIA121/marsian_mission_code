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


if __name__ == '__main__':
    app.run()
