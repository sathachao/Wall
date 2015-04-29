__author__ = 'Faaiz'
from PIL import Image
from PySide.QtGui import *
import sys
import psycopg2 

class Test(QWidget):
    def __init__(self,im):
        QWidget.__init__(self)
        image = QImage.fromData(im)
        image = image.scaled(100,200)
        display = QLabel()
        display.setPixmap(QPixmap(image))
        layout = QVBoxLayout(self)
        layout.addWidget(display)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = psycopg2.connect(database="Wall",user="postgres",password="pP3819269")
    cur = db.cursor()
    db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur.execute("SELECT image FROM images")
    im = cur.fetchone()[0]
    t = Test(im.tobytes())
    t.show()
    sys.exit(app.exec_())




'''
f = open("bg1.png",'rb')
binary = f.read()
b = psycopg2.Binary(binary)
cur.execute("SELECT count(*) FROM images")
index = cur.fetchone()[0]
cur.execute("INSERT INTO images(id,image) VALUES(%s,%s)" ,[index,b])
print(len(binary))
'''
