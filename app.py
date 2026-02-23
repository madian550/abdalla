from flask import Flask, render_template, request, jsonify
# استورد هنا الدوال الأساسية من كودك (con, create_websocket)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_tokens():
    tokens = request.json.get('tokens', [])
    results = []
    for token in tokens:
        # هنا هتنادي دالة الفحص (con) وترجع النتيجة في list
        # مثال: res = con(token, mask_token(token))
        results.append({"token": token, "status": "Valid"}) 
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)