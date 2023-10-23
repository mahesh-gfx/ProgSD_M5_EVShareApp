from tkinter import *
class management:
    def __init__(self):
        def download_as_PDF():
            print('download as PDF')

        def to_profile_page():
            print('to profile page')
        def show_data():
            print('')
        managePage = Tk()
        managePage.geometry('1600x976')
        managePage.title('Management')
        #managePage.resizable(False,False)
        managePage.configure(background='#F8F8F8')

        # baseUI
        BlueBarPath = r"../image_components/manager-bluebar.png"
        BlueBarPath = PhotoImage(file=BlueBarPath)
        BlueBarLabel= Label(image=BlueBarPath)
        BlueBarLabel.place(x=0,y=0)

        FleetStateDayPath = r"../image_components/manager-Feetstate-Day.png"
        FleetStateDayPath = PhotoImage(file=FleetStateDayPath)
        FleetStateDayPathLabel= Label(image=FleetStateDayPath,background='#F8F8F8')
        FleetStateDayPathLabel.place(x=138,y=70)

        FleetStateWeekPath = r"../image_components/manager-Fleet-Week.png"
        FleetStateWeekPath = PhotoImage(file=FleetStateWeekPath)
        FleetStateWeekPathLabel= Label(image=FleetStateWeekPath,background='#F8F8F8')
        FleetStateWeekPathLabel.place(x=625,y=70)

        FleetStateMonthPath = r"../image_components/manager-Fleet-Month.png"
        FleetStateMonthPath = PhotoImage(file=FleetStateMonthPath)
        FleetStateMonthPathLabel= Label(image=FleetStateMonthPath,background='#F8F8F8')
        FleetStateMonthPathLabel.place(x=1096,y=70)

        TotalCarPath = r"../image_components/manager-Total-Cars.png"
        TotalCarPath = PhotoImage(file=TotalCarPath)
        TotalCarPathLabel= Label(image=TotalCarPath,background='#F8F8F8')
        TotalCarPathLabel.place(x=140,y=330)

        TotalCustomerPath = r"../image_components/manager-Total-customer.png"
        TotalCustomerPath = PhotoImage(file=TotalCustomerPath)
        TotalCustomerPathLabel= Label(image=TotalCustomerPath,background='#F8F8F8')
        TotalCustomerPathLabel.place(x=493,y=330)

        DailyIncomePath = r"../image_components/manager-Daily-income.png"
        DailyIncomePath = PhotoImage(file=DailyIncomePath)
        DailyIncomePathLabel= Label(image=DailyIncomePath,background='#F8F8F8')
        DailyIncomePathLabel.place(x=875,y=330)

        RecentDefectPath = r"../image_components/manager-recent-defect.png"
        RecentDefectPath = PhotoImage(file=RecentDefectPath)
        RecentDefectPathLabel= Label(image=RecentDefectPath,background='#F8F8F8')
        RecentDefectPathLabel.place(x=1257,y=330)

        ActiveCustomerPath = r"../image_components/manager-Active-customer.png"
        ActiveCustomerPath = PhotoImage(file=ActiveCustomerPath)
        ActiveCustomerPathLabel= Label(image=ActiveCustomerPath,background='#F8F8F8')
        ActiveCustomerPathLabel.place(x=138,y=540)

        IncomePath = r"../image_components/manager-income.png"
        IncomePath = PhotoImage(file=IncomePath)
        IncomePathLabel= Label(image=IncomePath,background='#F8F8F8')
        IncomePathLabel.place(x=807,y=540)

        # DownloadButton
        DownloadButPath = r"../image_components/manager-downloadBut.png"
        DownloadButPath = PhotoImage(file=DownloadButPath)
        buttonDownload= Button(image=DownloadButPath,compound=TOP,command=download_as_PDF,borderwidth=0,background='#44AEEA',activebackground="#44AEEA")
        buttonDownload.place(x=30,y=3)

        # ProfileButton
        ProfileButPath = r"../image_components/defect-profile.png"
        ProfileButPath = PhotoImage(file=ProfileButPath)
        buttonProfile= Button(image=ProfileButPath,compound=TOP,command=to_profile_page,borderwidth=0,background='#44AEEA',activebackground="#44AEEA")
        buttonProfile.place(x=1400,y=20)


        # Fleet day
        FleetdayPath = r"../image_components/manager-test-piechart.png"
        FleetdayPath = PhotoImage(file=FleetdayPath)
        FleetdayPathLabel = Label(image=FleetdayPath, background='#FFFFFF')
        FleetdayPathLabel.place(x=224, y=140)

        # Fleet Week
        FleetWeekPath = r"../image_components/manager-test-piechart.png"
        FleetWeekPath = PhotoImage(file=FleetWeekPath)
        FleetWeekPathLabel = Label(image=FleetWeekPath, background='#FFFFFF')
        FleetWeekPathLabel.place(x=711, y=140)

        # Fleet Month
        FleetMonthPath = r"../image_components/manager-test-piechart.png"
        FleetMonthPath = PhotoImage(file=FleetMonthPath)
        FleetMonthPathLabel = Label(image=FleetMonthPath, background='#FFFFFF')
        FleetMonthPathLabel.place(x=1193, y=140)

        # Total car info
        CarNumber = Label(text='30,200',font=('inter',25,'bold'),background='#FFFFFF',foreground='#504F4F' )
        CarNumber.place(x=191,y=460)

        # Total customers info
        customersNumber = Label(text='50,270',font=('inter',25,'bold'),background='#FFFFFF' ,foreground='#504F4F')
        customersNumber.place(x=541,y=460)

        # Daily income info
        incomeNumber = Label(text='￡7,270',font=('inter',25,'bold'),background='#FFFFFF' ,foreground='#504F4F')
        incomeNumber.place(x=910,y=460)

        # Daily income info
        incomeNumber = Label(text='￡7,270',font=('inter',25,'bold'),background='#FFFFFF' ,foreground='#504F4F')
        incomeNumber.place(x=910,y=460)

        # Defect info
        DefectNumber = Label(text='100',font=('inter',25,'bold'),background='#FFFFFF' ,foreground='#504F4F')
        DefectNumber.place(x=1330,y=460)

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