from flask import Flask 
  
app = Flask(__name__) 
  
# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
    
    return "From extension - Hello world! again !!"
    
@app.route("/") 
def index(): 
    return "Hello World"
  
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)