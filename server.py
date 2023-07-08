from flask import Flask,jsonify, request
import util
app=Flask(__name__)

@app.route('/hello')
def Hello():
    return "Heyy"

@app.route('/classify_image',methods=["GET","POST"])
def classify_image():
    image_data = request.form['image_data']
    path = "./testImg/" + image_data
    print(path)
    response = jsonify(util.classify_image(None, path))

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == "__main__":
    print("Starting Python Flask Server For Student Name Classification")
    util.load_saved_artifacts()
    app.run(port=5000)