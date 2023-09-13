from flask import Flask, render_template, request
import pytube
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['url']
        video_resolution = request.form['resolution']
        try:
            youtube = pytube.YouTube(video_url)
            stream = youtube.streams.filter(res=video_resolution).first()
            stream.download()
            return "Download complete!"
        except Exception as e:
            return f"An error occurred: {str(e)}"
            return render_template('index.html')
        if __name__ == '__main__':
            app.run(debug=True)

