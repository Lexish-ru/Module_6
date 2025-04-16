from flask import Flask, request, send_from_directory, render_template_string

app = Flask(__name__)

pages = {
    "": "index.html",
    "index": "index.html",
    "catalog": "catalog.html",
    "category": "category.html",
    "contacts": "contacts.html"
}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def serve_page(path):
    filename = pages.get(path)
    if filename:
        return send_from_directory('.', filename)
    return "<h1>404 — Страница не найдена</h1>", 404

@app.route('/submit', methods=['POST'])
def handle_submit():
    name = request.form.get('name', 'Без имени')
    email = request.form.get('email', 'Без почты')
    message = request.form.get('message', 'Без сообщения')

    print("Новое сообщение с формы:")
    print(f"Имя: {name}")
    print(f"Email: {email}")
    print(f"Сообщение: {message}")

    return render_template_string(f"""
        <h2>Спасибо, {name}!</h2>
        <p>Мы получили ваше сообщение.</p>
        <a href="/contacts">Вернуться</a>
    """)

if __name__ == '__main__':
    app.run(debug=True)
