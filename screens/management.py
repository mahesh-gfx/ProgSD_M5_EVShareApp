from tkinter import *
import sqlite3
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.lines import Line2D
from datetime import datetime

class management:
    def get_incomefig(self):

        # 连接到数据库
        conn = sqlite3.connect(r'../zevo-dev.db')
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
        plt.savefig('income_trend.png', dpi=100)  # 设置dpi以控制输出图像的分辨率

        # 关闭连接
        conn.close()

    def get_activefig(self):
        # 连接到数据库
        conn = sqlite3.connect(r'../zevo-dev.db')
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
        plt.savefig('active_month.png', dpi=100)  # 设置dpi以控制输出图像的分辨率

        # 关闭连接
        conn.close()

    def create_pie_chart(self, data, filename):
        count = Counter(data)
        # 获取字符串类型和它们的数量
        labels, values = zip(*count.items())
        plt.figure(figsize=(3, 2.25), dpi=80)  # 180像素对应dpi为80
        plt.pie(values, labels=None, autopct='%1.1f%%', startangle=140)
        plt.axis('off')
        plt.axis('equal')
        legend_elements = [Line2D([0], [0], marker='o', color='w', label=label, markersize=10, markerfacecolor=color)
                           for label, color in zip(labels, plt.cm.tab20.colors)]

        legend = plt.gca().add_artist(plt.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(1, 1)))
        legend.set_title("String Types", prop={'size': 0.00000001})  # 调整字体大小
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
        defect = 0
        for row in defect_data:
            parts = row[0].split(',')
            timestamp = parts[1].strip()
            info = parts[0].strip()
            # 假设时间戳的格式是'YYYY-MM-DD HH:MM:SS'
            date = timestamp.split(' ')[0]
            year, month, day = map(int, date.split('-'))
            if day == 1:
                days.append(info)
            if day>1 and day<=7:
                weeks.append(info)
            if day >7:
                months.append(info)
            if info!='fine':
                defect = defect+1
        self.create_pie_chart(days,'days.png')
        self.create_pie_chart(weeks, 'weeks.png')
        self.create_pie_chart(months,'months.png')
        return len(defect_data), defect
    def get_income(self):
        # 连接到数据库
        conn = sqlite3.connect(r'../zevo-dev.db')
        cursor = conn.cursor()

        # 使用 SQL 查询来计算 income 列的总和
        cursor.execute("SELECT SUM(income) FROM orders")

        # 获取总和值
        total_income = cursor.fetchone()[0]
        return total_income

    def get_Userinfo(self):
        conn = sqlite3.connect(r'../zevo-dev.db')
        c = conn.cursor()
        # 查询数据库以获取符合条件的数据
        User_data = c.execute("SELECT * FROM users ").fetchall()
        return len(User_data)

        # 创建并保存饼图
    def __init__(self):
        self.get_incomefig()
        self.get_activefig()
        carNumber , defect = self.get_fleet()
        UserNumber = self.get_Userinfo()
        income = self.get_income()
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
        FleetdayPath = r"days.png"
        FleetdayPath = PhotoImage(file=FleetdayPath)
        FleetdayPathLabel = Label(image=FleetdayPath, background='#FFFFFF')
        FleetdayPathLabel.place(x=224, y=135)

        # Fleet Week
        FleetWeekPath = r"weeks.png"
        FleetWeekPath = PhotoImage(file=FleetWeekPath)
        FleetWeekPathLabel = Label(image=FleetWeekPath, background='#FFFFFF')
        FleetWeekPathLabel.place(x=711, y=135)

        # Fleet Month
        FleetMonthPath = r"months.png"
        FleetMonthPath = PhotoImage(file=FleetMonthPath)
        FleetMonthPathLabel = Label(image=FleetMonthPath, background='#FFFFFF')
        FleetMonthPathLabel.place(x=1193, y=135)

        # Total car info
        CarNumber = Label(text=str(carNumber), font=('inter', 25, 'bold'),
                          background='#FFFFFF', foreground='#504F4F')
        CarNumber.place(x=191, y=460)

        # Total customers info
        customersNumber = Label(text=str(UserNumber), font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        customersNumber.place(x=541, y=460)

        # Daily income info
        incomeNumber = Label(text='￡'+str(income), font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        incomeNumber.place(x=910, y=460)

        # Defect info
        DefectNumber = Label(text=str(defect), font=(
            'inter', 25, 'bold'), background='#FFFFFF', foreground='#504F4F')
        DefectNumber.place(x=1330, y=460)

        # Active customers info
        customersInfo = r"active_month.png"
        customersInfo = PhotoImage(file=customersInfo)
        customersInfoLabel = Label(image=customersInfo, background='#FFFFFF')
        customersInfoLabel.place(x=200, y=600)

        # income trend info
        incomeInfo = r"income_trend.png"
        incomeInfo = PhotoImage(file=incomeInfo)
        incomeInfoLabel = Label(image=incomeInfo, background='#FFFFFF')
        incomeInfoLabel.place(x=900, y=600)

        managePage.mainloop()


if __name__ == '__main__':
    management()
