from flask import Flask,redirect,url_for,render_template,request

#this app instance will be WSGI application which will be interacting with the server...here we are intialising the flask
app=Flask(__name__)

#Jinja2 template engine
'''
{%...%}  statements
{{...}} expressions to print output
{#...#} this is for comments
'''



#decorator with two parameters rule and options here rule is str parameter refer to the url
@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/members")
def greet():
    return "Welcome to my flask application members."

#dynamically building the url where we get the score from the url itself
@app.route("/success/<int:score>")
def success(score):
    # return "Congratulations! You passed the exam with a score of "+str(score)
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    # return render_template('result.html',result=res)
    exp={'score': score,'res':res}
    return render_template('result.html',result=exp)

@app.route("/fail/<int:score>")
def fail(score):
    return "Oops! You failed the exam with a score of "+str(score)

##Result checker route
@app.route("/result/<int:score>")
def result_checker(score):
    result = ""
    if score>=50:
        result = "success"
    else:
        result = "fail"
    return redirect(url_for(result,score=score))

#Result checker html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    return redirect(url_for('success',score=total_score))   

#Entry point : __name__ is the first thing which will start when flask app is intialised
if __name__=="__main__":
    app.run(debug=True)