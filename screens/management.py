from tkinter import *
import sqlite3
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.lines import Line2D
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import ttk


class management(ttk.Frame):
    def get_incomefig(self):

        # 连接到数据库
        conn = sqlite3.connect('zevo-dev.db')
        cursor = conn.cursor()

        # 执行 SQL 查询以检索所有 income 和 startTime 数据
        cursor.execute("SELECT income, startTime FROM orders")

        # 获取所有 income 和 startTime 数据
        data = cursor.fetchall()

        # 初始化一个字典来存储每个月份的总和
        monthly_income = {}

        # 遍历数据并按月份进行求和
        for item in data:
            income = int(item[0])
            start_time = datetime.strptime(item[1], '%Y-%m-%d %H:%M:%S')
            month_key = start_time.strftime('%Y-%m')
            if month_key in monthly_income:
                monthly_income[month_key] += income
            else:
                monthly_income[month_key] = income

        # 提取月份和总和数据
        months = list(monthly_income.keys())
        total_incomes = list(monthly_income.values())

        # 转换月份字符串为日期格式
        months = [datetime.strptime(month, '%Y-%m') for month in months]
        # 绘制折线图
        plt.figure(figsize=(431 / 100, 155 / 100))  # 设置图表大小为431x155像素
        plt.plot(total_incomes, marker='o', markersize=2, linestyle='-')
        plt.xticks([])
        # 保存图表为PNG文件
        plt.savefig('image_components/income_trend.png',
                    dpi=100)  # 设置dpi以控制输出图像的分辨率
        # 关闭连接
        conn.close()

    def get_activefig(self):
        # 连接到数据库
        conn = sqlite3.connect('zevo-dev.db')
        cursor = conn.cursor()

        # 执行 SQL 查询以检索所有 startTime 列的数据
        cursor.execute("SELECT startTime FROM orders")

        # 获取所有 startTime 数据
        start_times = cursor.fetchall()

        # 初始化一个字典来存储每个月份的总和
        monthly_sum = {}

        # 遍历 startTime 数据并按月份进行求和
        for start_time in start_times:
            start_time = datetime.strptime(start_time[0], '%Y-%m-%d %H:%M:%S')
            month_key = start_time.strftime('%Y-%m')
            if month_key in monthly_sum:
                monthly_sum[month_key] += 1
            else:
                monthly_sum[month_key] = 1

        # 提取月份和总和数据
        months = list(monthly_sum.keys())
        totals = list(monthly_sum.values())

        # 绘制柱状统计图
        plt.figure(figsize=(5, 1.4))  # 设置图表大小为500x140像素
        plt.bar(months, totals)
        plt.xticks([])

        # 保存图表为PNG文件
        plt.savefig('image_components/active_month.png',
                    dpi=100)  # 设置dpi以控制输出图像的分辨率

        # 关闭连接
        conn.close()

    def create_pie_chart(self, data, filename):
        count = Counter(data)
        labels, values = zip(*count.items())
        fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
        [wedges, texts, autotexts] = ax.pie(
            values, autopct='%1.1f%%', startangle=140)
        for autotext in autotexts:
            autotext.set_fontsize(20)
        colors = plt.cm.tab20.colors
        for i, (label, color) in enumerate(zip(labels, colors)):
            wedges[i].set_facecolor(color)
        # 设置标签
        legend_elements = [Line2D([0], [0], marker='o', color='w', label=label, markersize=10, markerfacecolor=color)
                           for label, color in zip(labels, colors)]
        legend = ax.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(0.9, 1, 0.01, 0.01),
                           prop={'size': 16})
        legend.get_frame().set_alpha(0)
        ax.axis('equal')
        ax.set_position([0.15, 0.15, 0.7, 0.7])
        plt.subplots_adjust(left=0.05, right=0.6)
        plt.savefig(filename, format='png')

    def get_fleet(self):
        # 连接到数据库
        conn = sqlite3.connect('zevo-dev.db')
        c = conn.cursor()
        defect_data = c.execute("SELECT defects FROM vehicles ").fetchall()
        # 关闭数据库连接
        conn.close()
        months = []
        weeks = []
        days = []
        defect = 0
        for row in defect_data:
            try:
                parts = row[0].split(',')
                timestamp = parts[1].strip()
                info = parts[0].strip()
                # 假设时间戳的格式是'YYYY-MM-DD HH:MM:SS'
                date = timestamp.split(' ')[0]
                year, month, day = map(int, date.split('-'))
                if day <= 2:
                    days.append(info)
                if day > 2 and day <= 7:
                    weeks.append(info)
                if day > 7:
                    months.append(info)
                if info != 'fine':
                    defect = defect+1
            except:
                pass
        self.create_pie_chart(days, r'image_components/days.png')
        self.create_pie_chart(weeks, r'image_components/weeks.png')
        self.create_pie_chart(months, r'image_components/months.png')
        return len(defect_data), defect

    def get_income(self):
        conn = sqlite3.connect('zevo-dev.db')
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(income) FROM orders")
        total_income = cursor.fetchone()[0]
        return total_income

    def get_Userinfo(self):
        conn = sqlite3.connect('zevo-dev.db')
        c = conn.cursor()
        User_data = c.execute("SELECT * FROM users ").fetchall()
        return len(User_data)

    def download_as_PDF(self):
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
        from reportlab.lib.styles import getSampleStyleSheet
        pdf_filename = "Management.pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        story = []

        # 添加标题
        styles = getSampleStyleSheet()
        title = "Management Information"
        title_text = Paragraph(title, styles["Title"])
        story.append(title_text)

        story.append(Spacer(1, 12))
        text = "Fleet days :"
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)

        story.append(Spacer(1, 12))
        # 添加图像
        image_filename = r"image_components/days.png"
        image = Image(image_filename, width=400, height=300)
        story.append(image)

        story.append(Spacer(1, 12))
        text = "Fleet weeks :"
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)
        image_filename = r"image_components/weeks.png"
        image = Image(image_filename, width=400, height=300)
        story.append(image)

        story.append(Spacer(1, 12))
        text = "Fleet months :"
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)
        image_filename = r"image_components/months.png"
        image = Image(image_filename, width=400, height=300)
        story.append(image)

        story.append(Spacer(1, 12))
        # 添加文本段落
        text = "Total car : " + str(self.carNumber)
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)

        text = "Total customers : " + str(self.UserNumber)
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)

        text = "Total income : " + str(self.income) + " Pounds"
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)

        text = "Total defect : " + str(self.defect)
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)

        story.append(Spacer(1, 12))
        text = "Active customers per month months :"
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)
        image_filename =  r"image_components/active_month.png"
        image = Image(image_filename, width=400, height=300)
        story.append(image)

        story.append(Spacer(1, 12))
        text = "Income per year :"
        text_paragraph = Paragraph(text, styles["Normal"])
        story.append(text_paragraph)
        image_filename =   r"image_components/income_trend.png"
        image = Image(image_filename, width=400, height=300)
        story.append(image)

        doc.build(story)

        from tkinter import messagebox
        messagebox.showinfo("Info", "PDF has been created")

    def to_profile_page(self):
        print('to profile page')

    def show_data(self):
        print('')

        # 创建并保存饼图
    def __init__(self, container, controller):
        super().__init__(container)
        self.get_incomefig()
        self.get_activefig()
        self.carNumber, self.defect = self.get_fleet()
        self.UserNumber = self.get_Userinfo()
        self.income = self.get_income()

        # baseUI
        self.BlueBarPath = r"image_components/manager-bluebar.png"
        self.BlueBarPath = PhotoImage(file=self.BlueBarPath)
        self.BlueBarLabel = Label(self, image=self.BlueBarPath)
        self.BlueBarLabel.place(x=0, y=0)

        self.FleetStateDayPath = r"image_components/manager-Feetstate-Day.png"
        self.FleetStateDayPath = PhotoImage(file=self.FleetStateDayPath)
        self.FleetStateDayPathLabel = Label(self,
                                            image=self.FleetStateDayPath, background='#F0F0F0')
        self.FleetStateDayPathLabel.place(x=138, y=70)

        self.FleetStateWeekPath = r"image_components/manager-Fleet-Week.png"
        self.FleetStateWeekPath = PhotoImage(file=self.FleetStateWeekPath)
        self.FleetStateWeekPathLabel = Label(self,
                                             image=self.FleetStateWeekPath, background='#F0F0F0')
        self.FleetStateWeekPathLabel.place(x=625, y=70)

        self.FleetStateMonthPath = r"image_components/manager-Fleet-Month.png"
        self.FleetStateMonthPath = PhotoImage(file=self.FleetStateMonthPath)
        self.FleetStateMonthPathLabel = Label(self,
                                              image=self.FleetStateMonthPath, background='#F0F0F0')
        self.FleetStateMonthPathLabel.place(x=1096, y=70)

        self.TotalCarPath = r"image_components/manager-Total-Cars.png"
        self.TotalCarPath = PhotoImage(file=self.TotalCarPath)
        self.TotalCarPathLabel = Label(
            self, image=self.TotalCarPath, background='#F0F0F0')
        self.TotalCarPathLabel.place(x=140, y=330)

        self.TotalCustomerPath = r"image_components/manager-Total-customer.png"
        self.TotalCustomerPath = PhotoImage(file=self.TotalCustomerPath)
        self. TotalCustomerPathLabel = Label(self,
                                             image=self.TotalCustomerPath, background='#F0F0F0')
        self.TotalCustomerPathLabel.place(x=493, y=330)

        self.DailyIncomePath = r"image_components/manager-Daily-income.png"
        self.DailyIncomePath = PhotoImage(file=self.DailyIncomePath)
        self.DailyIncomePathLabel = Label(self,
                                          image=self.DailyIncomePath, background='#F0F0F0')
        self.DailyIncomePathLabel.place(x=875, y=330)

        self.RecentDefectPath = r"image_components/manager-recent-defect.png"
        self.RecentDefectPath = PhotoImage(file=self.RecentDefectPath)
        self.RecentDefectPathLabel = Label(self,
                                           image=self.RecentDefectPath, background='#F0F0F0')
        self.RecentDefectPathLabel.place(x=1257, y=330)

        self.ActiveCustomerPath = r"image_components/manager-Active-customer.png"
        self.ActiveCustomerPath = PhotoImage(file=self.ActiveCustomerPath)
        self.ActiveCustomerPathLabel = Label(self,
                                             image=self.ActiveCustomerPath, background='#F0F0F0')
        self.ActiveCustomerPathLabel.place(x=138, y=540)

        self.IncomePath = r"image_components/manager-income.png"
        self.IncomePath = PhotoImage(file=self.IncomePath)
        self.IncomePathLabel = Label(
            self, image=self.IncomePath, background='#F0F0F0')
        self.IncomePathLabel.place(x=807, y=540)

        # DownloadButton
        self.DownloadButPath = r"image_components/manager-downloadBut.png"
        self.DownloadButPath = PhotoImage(file=self.DownloadButPath)
        self.buttonDownload = Button(self, image=self.DownloadButPath, compound=TOP, command=self.download_as_PDF,
                                     borderwidth=0, background='#44AEEA', activebackground="#44AEEA")
        self.buttonDownload.place(x=30, y=3)

        # ProfileButton
        self.ProfileButPath = r"image_components/defect-profile.png"
        self.ProfileButPath = PhotoImage(file=self.ProfileButPath)
        self.buttonProfile = Button(self, image=self.ProfileButPath, compound=TOP, command=self.to_profile_page,
                                    borderwidth=0, background='#44AEEA', activebackground="#44AEEA")
        self.buttonProfile.place(x=1400, y=20)

        # Fleet day
        self.image1 = Image.open(r"image_components/days.png")
        self.image1 = self.image1.resize((240, 180))
        self.FleetdayPath = ImageTk.PhotoImage(self.image1)
        self.FleetdayPathLabel = Label(
            self, image=self.FleetdayPath, background='#FFFFFF')
        self.FleetdayPathLabel.place(x=180, y=135)
        # Fleet Week
        self.image2 = Image.open(r"image_components/weeks.png")
        self.image2 = self.image2.resize((240, 180))
        self.FleetWeekPath = ImageTk.PhotoImage(self.image2)
        self.FleetWeekPathLabel = Label(
            self, image=self.FleetWeekPath, background='#FFFFFF')
        self.FleetWeekPathLabel.place(x=667, y=135)

        # Fleet Month
        self.image3 = Image.open(r"image_components/months.png")
        self.image3 = self.image3.resize((240, 180))
        self.FleetMonthPath = ImageTk.PhotoImage(self.image3)
        self.FleetMonthPathLabel = Label(
            self, image=self.FleetMonthPath, background='#FFFFFF')
        self.FleetMonthPathLabel.place(x=1138, y=135)

        # Total car info
        self.CarNumber = Label(self, text=str(self.carNumber), font=('inter', 25, 'bold'),
                               background='#FFFFFF', foreground='#504F4F')
        self.CarNumber.place(x=191, y=460)

        # Total customers info
        self.customersNumber = Label(self, text=str(self.UserNumber), font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        self.customersNumber.place(x=541, y=460)

        # Daily income info
        self.incomeNumber = Label(self, text='￡'+str(self.income), font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        self.incomeNumber.place(x=910, y=460)

        # Defect info
        self.DefectNumber = Label(self, text=str(self.defect), font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        self.DefectNumber.place(x=1330, y=460)

        # Active customers info
        self.customersInfo = r"image_components/active_month.png"
        self.customersInfo = PhotoImage(file=self.customersInfo)
        self.customersInfoLabel = Label(
            self, image=self.customersInfo, background='#FFFFFF')
        self.customersInfoLabel.place(x=200, y=600)

        # income trend info
        self.incomeInfo = r"image_components/income_trend.png"
        self.incomeInfo = PhotoImage(file=self.incomeInfo)
        self.incomeInfoLabel = Label(
            self, image=self.incomeInfo, background='#FFFFFF')
        self.incomeInfoLabel.place(x=900, y=600)
