from flask import Flask,  render_template, request,url_for,json


app=Flask(__name__)
usuario=None
contraseña=None


@app.route("/", methods=['GET','POST'])

def home():
    if request.method=='POST':
        #
        #usuario=request.args.get('usuario')
        #password=request.args.get('usuario2')
        #request_data=request.get_json()
        #usuario=request_data["usuario"]
        usuario=request.form["usuario"]
        contraseña=request.form["password"]
        print(usuario)
        print(contraseña)

               
        #password=request_data["usuario2"]
         
        
    
        

    
    
    return render_template('index.html')




app.run(debug=True)