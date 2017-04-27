from customersupport import app

app.secret_key = "TESTING SECRET KEY"
if __name__ == "__main__":
    app.run(debug=True)
