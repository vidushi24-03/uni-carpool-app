from flask import Flask, render_template, request, redirect
from database import init_db, add_trip, get_all_trips, book_seat

app = Flask(__name__)


@app.route("/")
def home():
    trips = get_all_trips()
    return render_template("home.html", trips=trips)


@app.route("/post_trip", methods=["POST"])
def post_trip():
    driver = request.form["driver"]
    from_location = request.form["from_location"]
    to_location = request.form["to_location"]
    date = request.form["date"]
    seats_available = int(request.form["seats_available"])
    price_per_seat = float(request.form["price_per_seat"])

    add_trip(driver, from_location, to_location, date, seats_available, price_per_seat)
    return redirect("/")


@app.route("/book_trip/<int:trip_id>", methods=["POST"])
def book_trip(trip_id):
    book_seat(trip_id)
    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)