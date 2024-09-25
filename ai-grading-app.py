from flask import Flask, request, jsonify
from text_grading_model import grade_text
from image_grading_model import grade_image
from code_grading_model import grade_code

app = Flask(__name__)

@app.route('/grade', methods=['POST'])
def grade():
    text_input = request.form.get('textInput')
    image_input = request.files.get('imageInput')
    code_input = request.form.get('codeInput')

    text_grade = grade_text(text_input) if text_input else None
    image_grade = grade_image(image_input) if image_input else None
    code_grade = grade_code(code_input) if code_input else None

    result = {
        'text_grade': text_grade,
        'image_grade': image_grade,
        'code_grade': code_grade
    }

    return jsonify(result)

if __name__ == '_main_':
    app.run(debug=True)
