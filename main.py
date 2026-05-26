from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        n1 = int(request.form.get("num1", 0))
        n2 = int(request.form.get("num2", 0))
        op = request.form.get("operation")

        if op=="add":
            result = f"The sum is {n1+n2}"
        elif op=="multiply":
            result = f"The product is {n1*n2}"
        elif op=="divide":
            if n2!=0:
                result = f"The quotient is {n1/n2}"
            else: 
                result = "Error: Can't divide by zero!"
        elif op=="subtract":
            result = f"The difference is {n1-n2}"
        else:
            result = "Error: the answer could not be calculated. Please try again."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)