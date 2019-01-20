from flask import Flask, jsonify, redirect, url_for, escape, request, render_template
import requests

app = Flask(__name__,static_url_path='/static')

@app.route('/', methods=['GET','POST'])
def main():
    if request.method=="POST":
        ilac=request.form["ilac"]
        tckn=request.form["tckn"]
        return redirect("/sorgu/{0}/{1}".format(ilac,tckn))
    return render_template("girdi.html")

@app.route('/sorgu/<ilac>/<tckn>',methods=["GET"])
def result(ilac,tckn):
    return render_template("sonuc.html",ilac=ilac,tckn=tckn)

@app.route('/ilac/<ilac>',methods=['GET'])
def ilacgoster(ilac):
    return render_template("ilac.html",ilac=ilac)

@app.route('/hasta/<hasta>',methods=['GET'])
def hastagoster(hasta):
    return render_template("hasta.html",hasta=hasta)

if __name__ == '__main__':
    app.run(debug=True)
