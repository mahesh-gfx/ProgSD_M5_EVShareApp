from tkinter import *


defect_report_dict={
    "can't connect bluetooth" : False,
    "wrong battery status" : False,
    "tyre problems" : False,
    "traffic accident" : False
}

def jump_page():
    print('jump')

def upload_photo():
    print('upload photo')

def add_chat():
    print('add chat')

def to_profile_page():
    print('to profile page')

def to_consult_page():
    print('to consult page')

def press_bt1():
    global buttonReportLabel1
    if defect_report_dict["can't connect bluetooth"] == False:
        defect_report_dict["can't connect bluetooth"] = True
        buttonReportLabel1.destroy()
        buttonReportLabel1 = Button(image=photoSelect_T, compound=TOP, command=press_bt1, borderwidth=0,background='#F8F8F8')
        buttonReportLabel1.place(x=420, y=170)
    else:
        defect_report_dict["can't connect bluetooth"] = False
        buttonReportLabel1.destroy()
        buttonReportLabel1 = Button(image=photoSelect_F, compound=TOP, command=press_bt1, borderwidth=0,background='#F8F8F8')
        buttonReportLabel1.place(x=420, y=170)

def press_bt2():
    global buttonReportLabel2
    if defect_report_dict["wrong battery status"] == False:
        defect_report_dict["wrong battery status"] = True
        buttonReportLabel2.destroy()
        buttonReportLabel2 = Button(image=photoSelect_T, compound=TOP, command=press_bt2, borderwidth=0,background='#F8F8F8')
        buttonReportLabel2.place(x=420, y=200)
    else:
        defect_report_dict["wrong battery status"] = False
        buttonReportLabel2.destroy()
        buttonReportLabel2 = Button(image=photoSelect_F, compound=TOP, command=press_bt2, borderwidth=0,background='#F8F8F8')
        buttonReportLabel2.place(x=420, y=200)

def press_bt3():
    global buttonReportLabel3
    if defect_report_dict["tyre problems"] == False:
        defect_report_dict["tyre problems"] = True
        buttonReportLabel3.destroy()
        buttonReportLabel3 = Button(image=photoSelect_T, compound=TOP, command=press_bt3, borderwidth=0,background='#F8F8F8')
        buttonReportLabel3.place(x=420, y=230)
    else:
        defect_report_dict["tyre problems"] = False
        buttonReportLabel3.destroy()
        buttonReportLabel3 = Button(image=photoSelect_F, compound=TOP, command=press_bt3, borderwidth=0,background='#F8F8F8')
        buttonReportLabel3.place(x=420, y=230)

def press_bt4():
    global buttonReportLabel4
    if defect_report_dict["traffic accident"] == False:
        defect_report_dict["traffic accident"] = True
        buttonReportLabel4.destroy()
        buttonReportLabel4 = Button(image=photoSelect_T, compound=TOP, command=press_bt4, borderwidth=0,background='#F8F8F8')
        buttonReportLabel4.place(x=420, y=260)
    else:
        defect_report_dict["traffic accident"] = False
        buttonReportLabel4.destroy()
        buttonReportLabel4 = Button(image=photoSelect_F, compound=TOP, command=press_bt4, borderwidth=0,background='#F8F8F8')
        buttonReportLabel4.place(x=420, y=260)




# local variable
font_name = 'Mako'


defectScreen = Tk()
defectScreen.geometry('480x800')
defectScreen.title('Report Defect')
defectScreen.configure(background='#F8F8F8')
defectScreen.resizable(False,False)
# profile button
photoProf = r"../image_components/defect-profile.png"
photoProf = PhotoImage(file=photoProf)
buttonProf= Button(image=photoProf,compound=TOP,command=to_profile_page,borderwidth=0,background='#F8F8F8')
buttonProf.place(x=10,y=20)


# consult button
photoConsult = r"../image_components/defect-consult.png"
photoConsult = PhotoImage(file=photoConsult)
buttonConsult= Button(image=photoConsult,compound=TOP,command=to_consult_page,borderwidth=0,background='#F8F8F8')
buttonConsult.place(x=440,y=20)

# Report defect text
photoReportDefect = r"../image_components/defect-reportDefect.png"
photoReportDefect = PhotoImage(file=photoReportDefect)
ReportDefectLabel = Label(image=photoReportDefect,background='#F8F8F8')
ReportDefectLabel.place(x=89,y=64)


photoSelect_T = r"../image_components/defect-choise-T.png"
photoSelect_T = PhotoImage(file=photoSelect_T)
photoSelect_F = r"../image_components/defect-choise-F.png"
photoSelect_F = PhotoImage(file=photoSelect_F)

# Quick report text
QuickReportLabel = Label(text='Quick report:',font=(font_name,20),background='#F8F8F8')
QuickReportLabel.place(x=20,y=131)

global buttonReportLabel1
QuickReportLabel1 = Label(text="can't connect bluetooth",font=(font_name,16),background='#F8F8F8')
QuickReportLabel1.place(x=50,y=170)
buttonReportLabel1 = Button(image=photoSelect_F,compound=TOP,command=press_bt1,borderwidth=0,background='#F8F8F8')
buttonReportLabel1.place(x=420,y=170)

global buttonReportLabel2
QuickReportLabel2 = Label(text='wrong battery status',font=(font_name,16),background='#F8F8F8')
QuickReportLabel2.place(x=50,y=200)
buttonReportLabel2 = Button(image=photoSelect_F,compound=TOP,command=press_bt2,borderwidth=0,background='#F8F8F8')
buttonReportLabel2.place(x=420,y=200)

global buttonReportLabel3
QuickReportLabel3 = Label(text='tyre problems',font=(font_name,16),background='#F8F8F8')
QuickReportLabel3.place(x=50,y=230)
buttonReportLabel3 = Button(image=photoSelect_F,compound=TOP,command=press_bt3,borderwidth=0,background='#F8F8F8')
buttonReportLabel3.place(x=420,y=230)

global buttonReportLabel4
QuickReportLabel4 = Label(text='traffic accident',font=(font_name,16),background='#F8F8F8')
QuickReportLabel4.place(x=50,y=260)
buttonReportLabel4 = Button(image=photoSelect_F,compound=TOP,command=press_bt4,borderwidth=0,background='#F8F8F8')
buttonReportLabel4.place(x=420,y=260)

# description box
photoRectangle = r"../image_components/defect-rectangle.png"
photoRectangle = PhotoImage(file=photoRectangle)
photoRectangleImg=Label(image=photoRectangle,background='#F8F8F8')
photoRectangleImg.place(x=30,y=307)

description_box = Entry(background='#FFFFFF',borderwidth=0)
description_box.place(x=45,y=360,width=395)
description_box.focus()

descriptionLabel = Label(text='Describe the details...',font=(font_name,16),background='#FFFFFF')
descriptionLabel.place(x=40,y=330)

# add image
photoaddImage = r"../image_components/defect-addImage-rectangle.png"
photoaddImage = PhotoImage(file=photoaddImage)
imageLabel1 = Label(image=photoaddImage,background='#F8F8F8')
imageLabel1.place(x=30,y=529)
imageLabel2 = Label(image=photoaddImage,background='#F8F8F8')
imageLabel2.place(x=180,y=529)
imageLabel3 = Label(image=photoaddImage,background='#F8F8F8')
imageLabel3.place(x=331,y=529)

photoaddPhoto = r"../image_components/defect-addPhoto.png"
photoaddPhoto = PhotoImage(file=photoaddPhoto)
upload_but = Button(image=photoaddPhoto,background='#F8F8F8',borderwidth=0,compound=TOP,command=upload_photo)
upload_but.place(x=200,y=549)

photoaddChat = r"../image_components/defect-addChat.png"
photoaddChat = PhotoImage(file=photoaddChat)
addChat_but = Button(image=photoaddChat,background='#F8F8F8',borderwidth=0,compound=TOP,command=add_chat)
addChat_but.place(x=351,y=549)


# submit button
photoSubmit=r"../image_components/defect-submit.png"
photoSubmit = PhotoImage(file=photoSubmit)
submit_but = Button(image=photoSubmit,background='#F8F8F8',borderwidth=0,compound=TOP,command=jump_page)
submit_but.place(x=21,y=672)


defectScreen.mainloop()