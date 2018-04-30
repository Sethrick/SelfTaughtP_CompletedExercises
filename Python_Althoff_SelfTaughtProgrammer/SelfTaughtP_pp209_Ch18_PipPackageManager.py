# First in install the Python package manager Pip:
# seth@Anglachel:~$ sudo apt install python3-pip

# Then install the Flask web framework for Ubuntu/Unix:
# seth@Anglachel:~$ pip3 install flask

# Finally, you can import and run Flask in a Python program:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

app.run(port=8000)

# Screen output:
#        * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
#       127.0.0.1 - - [20/Apr/2018 12:52:20] "GET / HTTP/1.1" 200 -
