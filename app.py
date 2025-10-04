from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email == "admin@example.com" and password == "admin123":
            return redirect("/dashboard")
        return "Invalid credentials", 401
    return render_template_string("""
        <h2>Login Page</h2>
        <form method="post">
            <input name="email" placeholder="Email" />
            <input name="password" type="password" placeholder="Password" />
            <button type="submit" id="login-button">Login</button>
        </form>
    """)


@app.route("/dashboard")
def dashboard():
    return """
        <html>
            <head><title>Dashboard</title></head>
            <body><h1>Dashboard</h1></body>
        </html>
    """



