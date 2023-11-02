from tkinter import *
import tkinter as tk

class defect_page(tk.Frame):
    def __init__(self, container, controller):
            tk.Frame.__init__(self, container)
            self.defect_report_dict = {
                "can't connect bluetooth": False,
                "wrong battery status": False,
                "tyre problems": False,
                "traffic accident": False
            }

            # local variable
            font_name = 'Mako'
            # profile button
            self.photoProf = r"./image_components/arrow_alt_left.png"
            self.photoProf = PhotoImage(file=self.photoProf)
            self.buttonProf = Button(self,image=self.photoProf, compound=TOP,
                                command=lambda:controller.change_frame('paymentBill'), borderwidth=0, background='#F0F0F0')
            self.buttonProf.place(x=10, y=20)


            # Report defect text
            self.photoReportDefect = r"./image_components/defect-reportDefect.png"
            self.photoReportDefect = PhotoImage(file=self.photoReportDefect)
            self.ReportDefectLabel = Label(self,
                image=self.photoReportDefect, background='#F0F0F0')
            self.ReportDefectLabel.place(x=89, y=64)

            self.photoSelect_T = r"./image_components/defect-choise-T.png"
            self.photoSelect_T = PhotoImage(file=self.photoSelect_T)
            self.photoSelect_F = r"./image_components/defect-choise-F.png"
            self.photoSelect_F = PhotoImage(file=self.photoSelect_F)

            # Quick report text
            self.QuickReportLabel = Label(self,text='Quick report:', font=(
                font_name, 20), background='#F0F0F0')
            self.QuickReportLabel.place(x=20, y=131)

            global buttonReportLabel1
            self.QuickReportLabel1 = Label(self,text="can't connect bluetooth", font=(
                font_name, 16), background='#F0F0F0')
            self.QuickReportLabel1.place(x=50, y=170)
            self.buttonReportLabel1 = Button(self,
                image=self.photoSelect_F, compound=TOP, command=self.press_bt1, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel1.place(x=420, y=170)

            global buttonReportLabel2
            self.QuickReportLabel2 = Label(self,text='wrong battery status', font=(
                font_name, 16), background='#F0F0F0')
            self.QuickReportLabel2.place(x=50, y=200)
            self.buttonReportLabel2 = Button(self,
                image=self.photoSelect_F, compound=TOP, command=self.press_bt2, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel2.place(x=420, y=200)

            global buttonReportLabel3
            self.QuickReportLabel3 = Label(self,text='tyre problems', font=(
                font_name, 16), background='#F0F0F0')
            self.QuickReportLabel3.place(x=50, y=230)
            self.buttonReportLabel3 = Button(self,
                image=self.photoSelect_F, compound=TOP, command=self.press_bt3, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel3.place(x=420, y=230)

            global buttonReportLabel4
            self.QuickReportLabel4 = Label(self,text='traffic accident', font=(
                font_name, 16), background='#F0F0F0')
            self.QuickReportLabel4.place(x=50, y=260)
            self.buttonReportLabel4 = Button(self,
                image=self.photoSelect_F, compound=TOP, command=self.press_bt4, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel4.place(x=420, y=260)

            # description box
            self.photoRectangle = r"./image_components/defect-rectangle.png"
            self.photoRectangle = PhotoImage(file=self.photoRectangle)
            self.photoRectangleImg = Label(self,image=self.photoRectangle, background='#F0F0F0')
            self.photoRectangleImg.place(x=30, y=307)

            self.description_box = Entry(self,background='#FFFFFF', borderwidth=0)
            self.description_box.place(x=45, y=360, width=395)
            self.description_box.focus()

            self.descriptionLabel = Label(self,text='Describe the details...', font=(
                font_name, 16), background='#FFFFFF')
            self.descriptionLabel.place(x=40, y=330)

            # add image
            self.photoaddImage = r"./image_components/defect-addImage-rectangle.png"
            self.photoaddImage = PhotoImage(file=self.photoaddImage)
            self.imageLabel1 = Label(self,image=self.photoaddImage, background='#F0F0F0')
            self.imageLabel1.place(x=30, y=529)
            self.imageLabel2 = Label(self,image=self.photoaddImage, background='#F0F0F0')
            self.imageLabel2.place(x=180, y=529)
            self.imageLabel3 = Label(self,image=self.photoaddImage, background='#F0F0F0')
            self.imageLabel3.place(x=331, y=529)

            self.photoaddPhoto = r"./image_components/defect-addPhoto.png"
            self.photoaddPhoto = PhotoImage(file=self.photoaddPhoto)
            self.upload_but = Button(self,image=self.photoaddPhoto, background='#F0F0F0',
                                borderwidth=0, compound=TOP, command=self.upload_photo)
            self.upload_but.place(x=200, y=549)

            self.photoaddChat = r"./image_components/defect-addChat.png"
            self.photoaddChat = PhotoImage(file=self.photoaddChat)
            self.addChat_but = Button(self,image=self.photoaddChat, background='#F0F0F0',
                                 borderwidth=0, compound=TOP, command=self.add_chat)
            self.addChat_but.place(x=351, y=549)

            # submit button
            self.photoSubmit = r"./image_components/defect-submit.png"
            self.photoSubmit = PhotoImage(file=self.photoSubmit)
            self.submit_but = Button(self,image=self.photoSubmit, background='#F0F0F0',
                                borderwidth=0, compound=TOP, command=lambda:controller.change_frame('vehiclesView'))
            self.submit_but.place(x=21, y=672)

    def jump_page(self):
        import datetime
        data = self.defect_report_dict
        info = ''
        for key in data:
            if data[key] == True:
                info = info + " and " + key

        info = info + ',' + datetime.datetime.now()


    def upload_photo(self):
        print('upload photo')

    def add_chat(self):
        print('add chat')

    def to_profile_page(self):
        print('to profile page')

    def to_consult_page(self):
        print('to consult page')

    def press_bt1(self):
        global buttonReportLabel1
        if self.defect_report_dict["can't connect bluetooth"] == False:
            self.defect_report_dict["can't connect bluetooth"] = True
            self.buttonReportLabel1.destroy()
            self.buttonReportLabel1 = Button(self,
                image=self.photoSelect_T, compound=TOP, command=self.press_bt1, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel1.place(x=420, y=170)
        else:
            self.defect_report_dict["can't connect bluetooth"] = False
            self.buttonReportLabel1.destroy()
            self.buttonReportLabel1 = Button(self,
                image=self.photoSelect_F, compound=TOP, command=self.press_bt1, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel1.place(x=420, y=170)

    def press_bt2(self):
        global buttonReportLabel2
        if self.defect_report_dict["wrong battery status"] == False:
            self.defect_report_dict["wrong battery status"] = True
            self.buttonReportLabel2.destroy()
            self.buttonReportLabel2 = Button(self,
                image=self.photoSelect_T, compound=TOP, command=self.press_bt2, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel2.place(x=420, y=200)
        else:
            self.defect_report_dict["wrong battery status"] = False
            self.buttonReportLabel2.destroy()
            self.buttonReportLabel2 = Button(self,
                image=self.photoSelect_F, compound=TOP, command=self.press_bt2, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel2.place(x=420, y=200)

    def press_bt3(self):
        global buttonReportLabel3
        if self.defect_report_dict["tyre problems"] == False:
            self.defect_report_dict["tyre problems"] = True
            self.buttonReportLabel3.destroy()
            self.buttonReportLabel3 = Button(self,
                image=self.photoSelect_T, compound=TOP, command=self.press_bt3, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel3.place(x=420, y=230)
        else:
            self.defect_report_dict["tyre problems"] = False
            self.buttonReportLabel3.destroy()
            self.buttonReportLabel3 = Button(self,
                image=self.photoSelect_F, compound=TOP, command=self.press_bt3, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel3.place(x=420, y=230)

    def press_bt4(self):
        global buttonReportLabel4
        if self.defect_report_dict["traffic accident"] == False:
            self.defect_report_dict["traffic accident"] = True
            self.buttonReportLabel4.destroy()
            self.buttonReportLabel4 = Button(self,
                image=self.photoSelect_T, compound=TOP, command=self.press_bt4, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel4.place(x=420, y=260)
        else:
            self.defect_report_dict["traffic accident"] = False
            self.buttonReportLabel4.destroy()
            self.buttonReportLabel4 = Button(self,
                image=self.photoSelect_F, compound=TOP, command=self.press_bt4, borderwidth=0, background='#F0F0F0')
            self.buttonReportLabel4.place(x=420, y=260)

