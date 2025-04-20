from flask import Flask, render_template 

app = Flask(__name__)


app_name = "My Application name is: anak ke empat "

#1 App Route di flask "hello word"
@app.route("/")
def hello_world():
    return f"<p>Hello, semuanya, apa kabar! anak ke empat </p>"


#2 App Route di flask
@app.route("/aplikasi/")
def aplikasi():
    return "<p>Selamat Datanag di Aplikasi Flask</p>"


#3 App Route di HTML
@app.route("/about/")
def about():
    return render_template('about_without_bostrapp.html')

#4 App Route dengan HTML with bostrapp
@app.route("/about-bostrapp/")
def about_bostrapp():
    return render_template('about.html')


#5 App Route Dinamis
@app.route("/nama/<string:nama_mahasiswa>/")
def getnama(hilma_raihanah):
    return "nama anda adalah {}".format(hilma_raihanah)

#6 App Route ID
@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

#7 App Route Variabel Global
@app.route('/variabel-global/')
def variabel_global():
    return f"Welcome anak ke empat"

#8 App Route Dictionary Variabel
@app.route('/data')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('data.html', user=user)

if __name__ == "__main__":
    app.run()



<<<<<<< HEAD
=======

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Ini halaman utama
@app.route("/", methods=["GET", "POST"])
def kalkulator():
    ratecard = None
    if request.method == "POST":
        followers = int(request.form["followers"])
        # Logika rate card endorse berdasarkan jumlah followers
        if followers < 1000:
            ratecard = "Rp50.000"
        elif followers < 10000:
            ratecard = "Rp150.000"
        elif followers < 100000:
            ratecard = "Rp500.000"
        else:
            ratecard = "Rp1.000.000+"

    # Template HTML langsung di Python (biar sederhana dulu)
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kalkulator Rate Card Endorse</title>
    </head>
    <body>
        <h1>Kalkulator Rate Card Endorse</h1>
        <form method="POST">
            <label>Jumlah Followers:</label><br>
            <input type="number" name="followers" required><br><br>
            <button type="submit">Hitung Rate Card</button>
        </form>
        {% if ratecard %}
            <h2>Rate Card: {{ ratecard }}</h2>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, ratecard=ratecard)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> bbb0401915608e706e43e3be9d22711af479adad
