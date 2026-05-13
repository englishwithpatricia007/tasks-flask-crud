from flask import Flask

# __name__=__main__ 
# means that the code is being run directly, rather than imported as a module. 
# This is a common pattern in Python to allow code to be run as a script or imported as a module without executing the script code.
app = Flask(__name__)

@app.route('/') # This is a decorator that tells Flask to execute the hello_world function when the root URL (/) is accessed.
def hello_world():
    return 'Hello, World!'

@app.route("/about")
def about():
    return "This is the about page."

if __name__ == '__main__':
    app.run(debug=True) 
# This starts the Flask development server. The debug=True argument enables debug mode, 
# which provides helpful error messages and automatically reloads the server when code changes are detected.
