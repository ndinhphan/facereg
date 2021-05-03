import cv2
import sqlite3

camera = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# cap nhat ten va ID vao csdl
def InsertOrUpdate(id,name):
    connect = sqlite3.connect("FaceBaseNew.db")
    cursor = connect.execute('SELECT * FROM People WHERE ID= '+ str(id))
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
        break;
    if isRecordExist==1:
        cmd = "UPDATE people SET Name=' "+str(name)+" ' WHERE ID="+str(id)
    else:
        cmd = "INSERT INTO people(ID,Name) Values("+str(id)+",' "+str(name)+" ' )"
    connect.execute(cmd)
    connect.commit()
    connect.close()

ID = input('Ma nhan vien : ')
name = input('Nhap ten nhan vien : ')
print('Bắt đầu chụp ảnh hồ sơ, nhấn Q để thoát...')

InsertOrUpdate(ID,name)
sampleNum = 0

while(True):

    ret, img = camera.read()

    # Lật ảnh cho đỡ bị ngược
    img = cv2.flip(img,1)

    # Kẻ khung giữa màn hình để người dùng đưa mặt vào khu vực này
    centerH = img.shape[0] // 2;
    centerW = img.shape[1] // 2;
    sizeboxW = 300;
    sizeboxH = 400;
    cv2.rectangle(img, (centerW - sizeboxW // 2, centerH - sizeboxH // 2),
                  (centerW + sizeboxW // 2, centerH + sizeboxH // 2), (255, 255, 255), 5)

    # Đưa ảnh về ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Nhận diện khuôn mặt
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # Vẽ hình chữ nhật quanh mặt nhận được
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        sampleNum = sampleNum + 1
        # Ghi dữ liệu khuôn mặt vào thư mục dataSet
        cv2.imwrite("dataSet/"+name+'.' + ID + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

    cv2.imshow('frame', img)
    # Check xem có bấm q hoặc trên 5 ảnh sample thì thoát
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum>5:
        break

camera.release()
cv2.destroyAllWindows()