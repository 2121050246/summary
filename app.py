from flask import Flask, render_template, request
from handles import handle

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route cho trang chủ
@app.route('/home')
def index():
    return render_template('index.html')

# Định nghĩa route để xử lý form
@app.route('/submit', methods=['POST'])
def submit():
    summaries = []
    # Stop words list
    stop_words_vi = [
        "và", "một", "có", "không", "được", "của", "trong", "cho", "cái", "là", 
        "đã", "được", "của", "các", "với", "vào", "để", "này", "khi", "nó", 
        "ở", "ra", "làm", "nên", "được", "để", "qua", "trên", "từ", "là", 
        "theo", "của", "các", "nhiều", "vào", "nhưng", "đây", "được", "từ", 
        "đó", "những", "cũng", "nhiều", "các", "là", "đã", "khi", "cũng", 
        "và", "của", "các", "đã", "nên", "được", "và", "nên", "và", "không", 
        "có", "là", "được", "nên", "là", "của", "được", "từ", "này", "có", 
        "nhiều", "không", "và", "có", "là", "của", "đã", "được", "và", "nên", 
        "của", "đã", "và", "có", "là", "này", "là", "của", "đã", "của", 
        "có", "của", "đã", "và", "không", "là", "nên", "của", "có", "và", 
        "của", "đã", "là", "của", "có", "và", "không", "được", "và", "nên", 
        "và", "có", "của", "và", "này", "này", "của", "có", "được", "đã", 
        "có", "và", "và", "của", "này", "này", "này", "này", "này", "này"
    ]

    if request.method == 'POST':
        files = request.files.getlist('file')

        if files and all(file.filename.endswith('.txt') for file in files):
            for file in files:
                content = file.read().decode('utf-8')
       

                result = handle(content, stop_words_vi)
                summaries.append({"filename": file.filename, "summary": result})

        elif request.form.get('name'):
            content = request.form['name'].strip()
            

            result = handle(content, stop_words_vi)
            summaries.append({"filename": "Text", "summary": result})

        return render_template('render.html', summaries=summaries)

if __name__ == '__main__':
    app.run(debug=True)
