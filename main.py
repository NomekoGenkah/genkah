from flask import Flask, request, send_file
from flask_cors import CORS
import os
from download import getAudio
from search import getUrl

#main
#for now let's assume the url only
app = Flask("app")
CORS(app, resources={r"/download_query": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "<h1>hello compaire</h1>"


@app.route("/search", methods=['POST'])
def searchQuery():
    data = request.get_json()
    if "query" in data:
        query = data["query"]
        results = getUrl(query)
        return results


@app.route("/download_query", methods=['POST'])
def downloadQuery():
    data = request.get_json()
    
    if "query" in data:
        query = data["query"]
        results = getUrl(query)
        url = results[0]["url"]
        
        file_name = getAudio(url)
        response = send_file(file_name, mimetype='audio/mpeg')

        try:
            os.remove(file_name)
        except OSError as e:
            print(f"Eror: {e}")

        return response



@app.route("/download", methods=['POST'])
def download():
    data = request.get_json()
    print(data)

    if "link" in data:
        print(data['link'])
        songTitle = getAudio(data['link'])
        
        return send_file(songTitle, mimetype='audio/mpeg')

    return "hola"

    #song = getAudio()

#url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)