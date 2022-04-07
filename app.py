from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__) 
@app.route('/')
def index():
    return render_template("Home.html")

@app.route('/about')
def about():
    return  render_template("about.html")

@app.route('/req')
def req():
    return render_template("sol.html")
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
    if request.method == 'POST':  
        result = request.form 
    print(result)
    name=request.form.get('Name')
    return render_template("result.html",result = result,name=name)
if __name__ == '__main__':
    app.run()