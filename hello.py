from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#   return render_template('base.html')

# @app.route('/gardening')
# def gardening_info():
#   return render_template('gardening.html')

# @app.route('/cooking')
# def cooking_details():
#   return render_template('cooking.html')

# @app.route('/sci-fi')
# def sci_fi_world():
#   return render_template('sci_fi.html')


# if __name__ == '__main__':
#   app.run(debug=True)
