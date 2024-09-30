from flask import Flask, url_for, render_template, request 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/input")
def render_main_q1():
    Q1 = request.args['Q1']
    if Q1 == "Meal":
        answer1 = "Teriyaki Chicken"
        
    if Q1 == "Snack":
        answer1 = "Onigiri"
        
    if Q1 == "Dessert":
        answer1 = "Mochi"    #q1
        
    Q2 = request.args['Q2']
    if Q2 == "Hot":
        answer2 = "Ramen"
        
    if Q2 == "Cold":
        answer2 = "Soba"    #q2
        
    Q3 = request.args['Q3']
    if Q3 == "Sweet":
        answer3 = "Dango"
        
    if Q3 == "Sour":
        answer3 = "Umeboshi" 
        
    if Q3 == "Spicy":
        answer3 = "Chicken Curry Katsu"
        
    if Q3 == "Bitter":
        answer3 = "Natto"
        
    if Q3 == "Salty":
        answer3 = "Uni Sushi" #q3 
    
    return render_template('input.html', response1 = answer1, response2 = answer2, response3 = answer3, )
    
    

if __name__=="__main__":
    app.run(debug=True)
