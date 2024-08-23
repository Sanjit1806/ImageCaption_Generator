from flask import Flask, request, jsonify, render_template
# from ImageCaptioning_Transformer import generate_caption

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_caption', methods=['POST'])
def caption_image():
    if 'image_upload' in request.files:
        image = request.files['image_upload']
        caption = generate_caption(image)
    elif 'image_url' in request.form:
        image_url = request.form['image_url']
        caption = generate_caption(image_url)
    else:
        return jsonify({"error": "No image provided"}), 400

    return jsonify({"caption": caption})

if __name__ == '__main__':
    app.run(debug=True)
