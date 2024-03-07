from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# กำหนดเส้นทางสำหรับโฟลเดอร์รูปภาพ
IMAGE_FOLDER_ROOM = 'hotel'

# เส้นทางสำหรับแสดงรูปภาพ
@app.route('/images/<path:image_name>')
def get_image(image_name):
    return send_from_directory(IMAGE_FOLDER_ROOM, image_name)

# หน้าเว็บที่ใช้สำหรับแสดงรูปภาพ
@app.route('/')
def index():
    # ดึงรายการของรูปภาพจากโฟลเดอร์
    images = os.listdir(IMAGE_FOLDER_ROOM)
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)


# ตัวอย่างการใช้ในหน้า html
