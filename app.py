from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "secret123"
app.config["SESSION_PERMANENT"] = False

# ---------------- USERS (dynamic) ----------------
users = {}

# ---------------- PRODUCTS ----------------
products = [
    {"id": 1, "name": "Laptop", "price": 50000, "category": "Laptops", "rating": 4, "stock": 5, "img": "images/laptop.jpg"},
    {"id": 2, "name": "Phone", "price": 20000, "category": "Mobiles", "rating": 5, "stock": 10, "img": "images/phone.jpg"},
    {"id": 3, "name": "Headphones", "price": 2000, "category": "Accessories", "rating": 4, "stock": 8, "img": "images/headphones.jpg"},
    {"id": 4, "name": "Watch", "price": 3000, "category": "Accessories", "rating": 3, "stock": 6, "img": "images/watch.jpg"},
    {"id": 5, "name": "Keyboard", "price": 1500, "category": "Accessories", "rating": 4, "stock": 7, "img": "images/keyboard.jpg"},
    {"id": 6, "name": "Mouse", "price": 800, "category": "Accessories", "rating": 4, "stock": 9, "img": "images/mouse.jpg"},
    {"id": 7, "name": "Tablet", "price": 15000, "category": "Mobiles", "rating": 4, "stock": 4, "img": "images/tablet.jpg"},
    {"id": 8, "name": "Camera", "price": 40000, "category": "Electronics", "rating": 5, "stock": 3, "img": "images/camera.jpg"},
    {"id": 9, "name": "Speaker", "price": 3000, "category": "Electronics", "rating": 4, "stock": 6, "img": "images/speaker.jpg"},
    {"id": 10, "name": "Charger", "price": 500, "category": "Accessories", "rating": 3, "stock": 15, "img": "images/charger.jpg"},
    {"id": 11, "name": "Power Bank", "price": 1200, "category": "Accessories", "rating": 4, "stock": 10, "img": "images/powerbank.jpg"},
    {"id": 12, "name": "Monitor", "price": 10000, "category": "Electronics", "rating": 4, "stock": 5, "img": "images/monitor.jpg"},
]

# ---------------- HOME + SEARCH + FILTER ----------------
@app.route("/")
def index():
    query = request.args.get("q", "")
    category = request.args.get("category", "")
    price = request.args.get("price", "")

    filtered = products

    if query:
        filtered = [p for p in filtered if query.lower() in p["name"].lower()]

    if category:
        filtered = [p for p in filtered if p["category"] == category]

    if price:
        filtered = [p for p in filtered if p["price"] <= int(price)]

    visits = session.get("visits", 0)

    # First open = BLUE
    if visits == 0:
        session["visits"] = 1
        return render_template(
            "blue.html",
            products=filtered,
            cart_count=len(session.get("cart", [])),
            version="BLUE"
        )

    # Refresh / next load = GREEN
    return render_template(
        "index.html",
        products=filtered,
        cart=session.get("cart", []),
        user=session.get("user")
    )


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


# ---------------- SIGNUP ----------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        if email in users:
            return "User already exists"

        users[email] = {"name": name, "password": password}
        return redirect("/login")

    return render_template("signup.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in users and users[email]["password"] == password:
            session["user"] = users[email]["name"]
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

# ---------------- ADD TO CART ----------------
@app.route("/add/<int:id>", methods=["POST"])
def add(id):
    cart = session.get("cart", [])
    item = next(p for p in products if p["id"] == id)
    cart.append(item)
    session["cart"] = cart
    return redirect("/")

# ---------------- CART ----------------
@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    total = sum(i["price"] for i in cart)
    return render_template("cart.html", cart=cart, total=total)

# ---------------- REMOVE ----------------
@app.route("/remove/<int:index>")
def remove(index):
    cart = session.get("cart", [])
    if index < len(cart):
        cart.pop(index)
    session["cart"] = cart
    return redirect("/cart")

# ---------------- CHECKOUT ----------------
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        order = {
            "name": request.form["name"],
            "address": request.form["address"],
            "items": session.get("cart", [])
        }

        orders = session.get("orders", [])
        orders.append(order)
        session["orders"] = orders

        session["cart"] = []
        return redirect("/success")

    return render_template("checkout.html")

# ---------------- SUCCESS ----------------
@app.route("/success")
def success():
    return render_template("success.html")

# ---------------- ORDERS ----------------
@app.route("/orders")
def orders():
    return render_template("orders.html", orders=session.get("orders", []))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)