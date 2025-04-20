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



