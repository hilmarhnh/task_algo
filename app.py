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

