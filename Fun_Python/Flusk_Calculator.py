from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        try:
            expression = request.form["expression"]
            result = eval(expression)  # Evaluate the user input expression
        except:
            result = "Error"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
# Save this file as "Flusk_Calculator.py" in the "Python" directory.
# Create a new directory called "templates" inside the "Python" directory.
# Create a new file called "index.html" inside the "templates" directory.
# Add the following HTML code to the "index.html" file: