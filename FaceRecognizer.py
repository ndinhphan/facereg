# import cv2
# import numpy as np
# from PIL import Image
# import pickle
# import sqlite3
#
# # khoi tao phat hien khuon mat
# faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # khoi tao nhan dien khuon mat
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('recognizer/trainner.yml')
#
# # ham lay thong tin nguoi dung
# id = 0
# def getProfile(id):
#     connect =sqlite3.connect('FaceBaseNew.db')
#     cursor = connect.execute("SELECT * FROM People WHERE ID= "+str(id))
#     profile = None
#     for row in cursor:
#         profile = row
#     connect.close()
#     return profile
#
# # tao camera
# camera = cv2.VideoCapture(0)
#
# while(True):
#     ret,img =camera.read()
#     img = cv2.flip(img,1)
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     # phat hien khuon mat trong anh camera
#     faces = faceDetect.detectMultiScale(gray,1.3,5)
#     # lap qua tat ca khuon mat
#     for(x,y,w,h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         id, dist = recognizer.predict(gray[y:y + h, x:x + w])
#         profile = None
#
#         if (dist<=25):
#             profile=getProfile(id)
#         if (profile != None):
#             cv2.putText(img, "Name: " + str(profile[1]), (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
#         else:
#             cv2.putText(img, "Name: Unknown", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
#
#     cv2.imshow('Face', img)
#     if cv2.waitKey(1) == ord('q'):
#         break;
# # camera.release()
# # cv2.destroyAllWindows()
#
#

import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3
import tkinter
from tkinter import *
from PIL import Image,ImageTk
import cv2
import PIL.Image # cài đặt pillow
import PIL.ImageTk

# khoi tao phat hien khuon mat
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# khoi tao nhan dien khuon mat
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/trainner.yml')

# ham lay thong tin nguoi dung
id = 0
def getProfile(id):
    connect =sqlite3.connect('FaceBaseNew.db')
    cursor = connect.execute("SELECT * FROM People WHERE ID= "+str(id))
    profile = None
    for row in cursor:
        profile = row
    connect.close()
    return profile
window = Tk()
window.title("Phần mềm điểm danh")
window.resizable(False,False)
window.geometry("500x600")
window.iconbitmap("Image/UET-logo.ico")

bg_loading = Image.open("Image/background.jpg")
bg_render = ImageTk.PhotoImage(bg_loading)
bg = Label(window,image=bg_render)
bg.place(x=00,y=00)

video =cv2.VideoCapture(0)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)//2.5
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)//2.5
canvas = Canvas(window,width = canvas_w,height = canvas_h, bg ="#EEDD2F")
canvas.pack(pady = 10)

photo = None

note_lbl = Label(window,text="Please look directly at the camera ",font=("Goudy old style",15,"italic"),fg="#d77337")
note_lbl.place(x=125,y=206.5)

frame_info = Frame(window,bg="white")
frame_info.place(x=80,y=250,height=300,width=350)
frame_title = Label(frame_info,text="Information",font=("Impact",30,"bold"),fg="#d77337",bg="white").place(x=30,y=30)
desc = Label(frame_info,text="Time deals gently only with those who take it gently")
desc.config(font=("Goudy old style",10,"bold"),fg="#d77337",bg="white")
desc.place(x=30,y=80)

lbl_username = Label(frame_info,text="Name",font=("Goudy old style",13,"bold"),bg ="white",fg="gray").place(x=30,y=110)
txt_username = Entry(frame_info,font=("times new roman",15),bg="light gray")
txt_username.place(x=30,y=135,width=250,height=30)

lbl_id = Label(frame_info,text="ID",font=("Goudy old style",13,"bold"),bg ="white",fg="gray").place(x=30,y=165)
txt_id = Entry(frame_info,font=("times new roman",15),bg="light gray")
txt_id.place(x=30,y=190,width=250,height=30)

lbl_attendanceTime = Label(frame_info,text="Attendance Time",font=("Goudy old style",13,"bold"),bg ="white",fg="gray").place(x=30,y=220)
txt_attendanceTime = Text(frame_info,font=("times new roman",15),bg="light gray")
txt_attendanceTime.place(x=30,y=245,width=250,height=30)

export_btn = Button(window,text="Export",font=("times new roman",13),fg="white",bg="#d77337").place(x=225,y=538)

# while(True):
#     ret,img =video.read()
#     img = cv2.flip(img,1)
#     img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     # phat hien khuon mat trong anh camera
#     faces = faceDetect.detectMultiScale(gray,1.3,5)
#     # lap qua tat ca khuon mat
#     for(x,y,w,h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         id, dist = recognizer.predict(gray[y:y + h, x:x + w])
#         profile = None
#
#         if (dist<=25):
#             profile=getProfile(id)
#         if (profile != None):
#             cv2.putText(img, "Name: " + str(profile[1]), (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
#         else:
#             cv2.putText(img, "Name: Unknown", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
#     photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
#     canvas.create_image(0,0, image = photo,anchor = tkinter.NW)
#     if cv2.waitKey(1) == ord('q'):
#         break;

def updateFrame():
    global canvas,photo
    ret, img = video.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # phat hien khuon mat trong anh camera
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    # lap qua tat ca khuon mat
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id, dist = recognizer.predict(gray[y:y + h, x:x + w])
        profile = None
        if (dist <= 25):
            profile = getProfile(id)
        if (profile != None):
            # cv2.putText(img, "Name: " + str(profile[1]), (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            print(str(profile[1]))
        else:
            # cv2.putText(img, "Name: Unknown", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            print("unknown")
            # cái này Q đang thử xem nếu ko nhận diện đc khuôn mặt thì nó có chuyển sang màu đen ko =)) vì ko tìm đc cái chỗ đổi text
            txt_username.insert(END,"UNK")
            txt_attendanceTime.config(bg="black")
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(gray))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    window.after(15, updateFrame)

updateFrame()

window.mainloop()


