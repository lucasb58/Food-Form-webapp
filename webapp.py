from flask import Flask, url_for, render_template, request 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/input")
def render_main_input():
    Q1 = request.args['Q1']
    if Q1 == "Meal":
        answer = "Teriyaki Chicken"
        
    if Q1 == "Snack":
        answer = "Onigiri"
        
    if Q1 == "Dessert":
        answer = "Mochi"    
        
    return render_template('input.html', response1 = answer)

if __name__=="__main__":
    app.run(debug=True)
