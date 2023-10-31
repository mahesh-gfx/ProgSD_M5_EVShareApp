from tkinter import *
import sqlite3
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.lines import Line2D
import datetime
from PIL import Image, ImageTk

class management:

    def create_pie_chart(self, data, filename):
        count = Counter(data)
        labels, values = zip(*count.items())

        # 创建饼图
        fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
        [wedges, texts, autotexts] = ax.pie(values, autopct='%1.1f%%', startangle=140)
        for autotext in autotexts:
            autotext.set_fontsize(20)

        # 设置饼图部分的颜色
        colors = plt.cm.tab20.colors
        for i, (label, color) in enumerate(zip(labels, colors)):
            wedges[i].set_facecolor(color)
        # 设置标签
        legend_elements = [Line2D([0], [0], marker='o', color='w', label=label, markersize=10, markerfacecolor=color)
                        for label, color in zip(labels, colors)]
        legend = ax.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(0.9, 1, 0.01, 0.01),prop={'size': 16})
        #legend.set_title("String Types", prop={'size': 20})
        legend.get_frame().set_alpha(0)
        ax.axis('equal')
        ax.set_position([0.15, 0.15, 0.7, 0.7])
        plt.subplots_adjust(left=0.05, right=0.6)
        plt.savefig(filename, format='png')

    def get_fleet(self):
        # 连接到数据库
        conn = sqlite3.connect(r'../zevo-dev.db')
        c = conn.cursor()

        # 查询数据库以获取符合条件的数据
        defect_data = c.execute("SELECT defects FROM vehicles ").fetchall()
        # 关闭数据库连接
        conn.close()
        months = []
        weeks = []
        days = []

        for row in defect_data:
            parts = row[0].split(',')
            timestamp = parts[1].strip()
            info = parts[0].strip()
            # 假设时间戳的格式是'YYYY-MM-DD HH:MM:SS'
            date = timestamp.split(' ')[0]
            year, month, day = map(int, date.split('-'))
            if day <=2:
                days.append(info)
            if day>2 and day<=7:
                weeks.append(info)
            if day >7:
                months.append(info)
        self.create_pie_chart(days,'days.png')
        self.create_pie_chart(weeks, 'weeks.png')
        self.create_pie_chart(months,'months.png')


        # 创建并保存饼图
    def __init__(self):
        self.get_fleet()
        def download_as_PDF():
            print('download as PDF')

        def to_profile_page():
            print('to profile page')

        def show_data():
            print('')
        managePage = Tk()
        managePage.geometry('1600x976')
        managePage.title('Management')
        # managePage.resizable(False,False)
        managePage.configure(background='#F8F8F8')

        # baseUI
        BlueBarPath = r"../image_components/manager-bluebar.png"
        BlueBarPath = PhotoImage(file=BlueBarPath)
        BlueBarLabel = Label(image=BlueBarPath)
        BlueBarLabel.place(x=0, y=0)

        FleetStateDayPath = r"../image_components/manager-Feetstate-Day.png"
        FleetStateDayPath = PhotoImage(file=FleetStateDayPath)
        FleetStateDayPathLabel = Label(
            image=FleetStateDayPath, background='#F8F8F8')
        FleetStateDayPathLabel.place(x=138, y=70)

        FleetStateWeekPath = r"../image_components/manager-Fleet-Week.png"
        FleetStateWeekPath = PhotoImage(file=FleetStateWeekPath)
        FleetStateWeekPathLabel = Label(
            image=FleetStateWeekPath, background='#F8F8F8')
        FleetStateWeekPathLabel.place(x=625, y=70)

        FleetStateMonthPath = r"../image_components/manager-Fleet-Month.png"
        FleetStateMonthPath = PhotoImage(file=FleetStateMonthPath)
        FleetStateMonthPathLabel = Label(
            image=FleetStateMonthPath, background='#F8F8F8')
        FleetStateMonthPathLabel.place(x=1096, y=70)

        TotalCarPath = r"../image_components/manager-Total-Cars.png"
        TotalCarPath = PhotoImage(file=TotalCarPath)
        TotalCarPathLabel = Label(image=TotalCarPath, background='#F8F8F8')
        TotalCarPathLabel.place(x=140, y=330)

        TotalCustomerPath = r"../image_components/manager-Total-customer.png"
        TotalCustomerPath = PhotoImage(file=TotalCustomerPath)
        TotalCustomerPathLabel = Label(
            image=TotalCustomerPath, background='#F8F8F8')
        TotalCustomerPathLabel.place(x=493, y=330)

        DailyIncomePath = r"../image_components/manager-Daily-income.png"
        DailyIncomePath = PhotoImage(file=DailyIncomePath)
        DailyIncomePathLabel = Label(
            image=DailyIncomePath, background='#F8F8F8')
        DailyIncomePathLabel.place(x=875, y=330)

        RecentDefectPath = r"../image_components/manager-recent-defect.png"
        RecentDefectPath = PhotoImage(file=RecentDefectPath)
        RecentDefectPathLabel = Label(
            image=RecentDefectPath, background='#F8F8F8')
        RecentDefectPathLabel.place(x=1257, y=330)

        ActiveCustomerPath = r"../image_components/manager-Active-customer.png"
        ActiveCustomerPath = PhotoImage(file=ActiveCustomerPath)
        ActiveCustomerPathLabel = Label(
            image=ActiveCustomerPath, background='#F8F8F8')
        ActiveCustomerPathLabel.place(x=138, y=540)

        IncomePath = r"../image_components/manager-income.png"
        IncomePath = PhotoImage(file=IncomePath)
        IncomePathLabel = Label(image=IncomePath, background='#F8F8F8')
        IncomePathLabel.place(x=807, y=540)

        # DownloadButton
        DownloadButPath = r"../image_components/manager-downloadBut.png"
        DownloadButPath = PhotoImage(file=DownloadButPath)
        buttonDownload = Button(image=DownloadButPath, compound=TOP, command=download_as_PDF,
                                borderwidth=0, background='#44AEEA', activebackground="#44AEEA")
        buttonDownload.place(x=30, y=3)

        # ProfileButton
        ProfileButPath = r"../image_components/defect-profile.png"
        ProfileButPath = PhotoImage(file=ProfileButPath)
        buttonProfile = Button(image=ProfileButPath, compound=TOP, command=to_profile_page,
                               borderwidth=0, background='#44AEEA', activebackground="#44AEEA")
        buttonProfile.place(x=1400, y=20)

        # Fleet day
        image1 = Image.open("days.png")
        image1 = image1.resize((240, 180), Image.ANTIALIAS)
        FleetdayPath = ImageTk.PhotoImage(image1)
        FleetdayPathLabel = Label(image=FleetdayPath, background='#FFFFFF')
        FleetdayPathLabel.place(x=180, y=135)
        # Fleet Week
        image2 = Image.open("weeks.png")
        image2 = image2.resize((240, 180), Image.ANTIALIAS)
        FleetWeekPath = ImageTk.PhotoImage(image2)
        FleetWeekPathLabel = Label(image=FleetWeekPath, background='#FFFFFF')
        FleetWeekPathLabel.place(x=667, y=135)

        # Fleet Month
        image3 = Image.open("months.png")
        image3 = image3.resize((240, 180), Image.ANTIALIAS)
        FleetMonthPath = ImageTk.PhotoImage(image3)
        FleetMonthPathLabel = Label(image=FleetMonthPath, background='#FFFFFF')
        FleetMonthPathLabel.place(x=1138, y=135)
      
    

        # Total car info
        CarNumber = Label(text='30,200', font=('inter', 25, 'bold'),
                          background='#FFFFFF', foreground='#504F4F')
        CarNumber.place(x=191, y=460)

        # Total customers info
        customersNumber = Label(text='50,270', font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        customersNumber.place(x=541, y=460)

        # Daily income info
        incomeNumber = Label(text='￡7,270', font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        incomeNumber.place(x=910, y=460)

        # Daily income info
        incomeNumber = Label(text='￡7,270', font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        incomeNumber.place(x=910, y=460)

        # Defect info
        DefectNumber = Label(text='100', font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        DefectNumber.place(x=1330, y=460)

        # Active customers info
        customersInfo = r"../image_components/manager-customer-test.png"
        customersInfo = PhotoImage(file=customersInfo)
        customersInfoLabel = Label(image=customersInfo, background='#FFFFFF')
        customersInfoLabel.place(x=200, y=600)

        # income trend info
        incomeInfo = r"../image_components/manager-customer-income-test.png"
        incomeInfo = PhotoImage(file=incomeInfo)
        incomeInfoLabel = Label(image=incomeInfo, background='#FFFFFF')
        incomeInfoLabel.place(x=900, y=600)

        managePage.mainloop()


if __name__ == '__main__':
    management()
