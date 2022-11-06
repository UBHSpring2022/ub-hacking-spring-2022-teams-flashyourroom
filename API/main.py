from flask import Flask,request,Response

app = Flask(__name__)
data = {
    "1": {"brightness": 0,
        "red": 0,
        "green": 0,
        "blue": 0,
        "frequency": 0,
        "area": 0},
     "2": {"brightness": 0,
        "red": 0,
        "green": 0,
        "blue": 0,
        "frequency": 0,
        "area": 0},
     "3": {"brightness": 0,
        "red": 0,
        "green": 0,
        "blue": 0,
        "frequency": 0,
        "area": 0},
     "4": {"brightness": 0,
        "red": 0,
        "green": 0,
        "blue": 0,
        "frequency": 0,
        "area": 0}
}

@app.route("/", methods=['GET', 'POST','OPTIONS'])
def hello_world():
    if request.method == 'OPTIONS':
        resp = Response({})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'POST'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        print("OPTIONS")
        return resp
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            jsonData = request.json
            resp = Response(data)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            print(jsonData)
            data["1"]=jsonData["1"]
            data["2"]=jsonData["2"]
            data["3"]=jsonData["3"]
            data["4"]=jsonData["4"]
            # data["brightness"] = jsonData["brightness"]
            # data["red"] = jsonData["red"]
            # data["green"] = jsonData["green"]
            # data["blue"] = jsonData["blue"]
            # data["frequency"] = jsonData["frequency"]
            # data["area"] = jsonData["area"]
            return data

    if request.method == 'GET':
        
        return data

if __name__ == "__main__":
    app.run(debug=True)