from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Chạy Flask bằng python app.py!"

if __name__ == '__main__':
    # Lấy port từ biến môi trường (Render sẽ set), mặc định là 5000 nếu chạy local
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' để Flask lắng nghe mọi IP (bắt buộc với Render)
    app.run(host='0.0.0.0', port=port, debug=True)
