import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


from gui.Dashboard.pyqt_dashboard import Ui_DashBoard
from gui.UserProfile.UserProfile import Userprofile
from gui.Property_GUI.Property_main import Property_Page
from gui.Setting_GUI.Setting_Page_GUI import Setting_Page
from gui.Notification_GUI.Noti_Page_GUI import Notification_Page
from gui.Contractor_Page_GUI.Contractor_Page import Contractor_Page
from gui.TenantPage_GUI.tenantsUI_main import tenantsui

#controllers
from System import Cont_UserProfile, Cont_Tenant


class Dashboard(QMainWindow, Ui_DashBoard):
    def __init__(self, Cont_UserProfile : Cont_UserProfile, Cont_TenantPage : Cont_Tenant):
        super().__init__()
        self.setupUi(self)
        #edits by Ali
        self.Cont_UserProfile = Cont_UserProfile
        self.Cont_TenantPage = Cont_TenantPage
        #
        self.show()

        self.is_signout = False

        self.Properties_btn.clicked.connect(self.goto_property_page)
        # pushButton = userprofile page
        self.pushButton_3.clicked.connect(self.goto_user_profile_page)
        # pushButton_2 = setting page
        self.pushButton_2.clicked.connect(self.goto_setting_page)
        # pushButton_4 = notification page
        self.pushButton_4.clicked.connect(self.goto_notification_page)
        # pushButton_5 = contractor page
        self.pushButton_5.clicked.connect(self.goto_contractor_page)
        # Tenants_btn = Tenant page
        self.Tenants_btn.clicked.connect(self.goto_tenant_page)
        # signout_btn = signout button
        self.signout_btn.clicked.connect(self.sign_out)

    def goto_property_page(self, checked):
        self.property_page = Property_Page()
        self.property_page.show()

    def goto_user_profile_page(self, checked):
        print(f"going to user profile page")
        self.user_profile = Userprofile(self.Cont_UserProfile)
        self.user_profile.show()

    def goto_setting_page(self, checked):
        self.setting_page = Setting_Page()
        self.setting_page.show()

    def goto_notification_page(self, checked):
        self.notification_page = Notification_Page()
        self.notification_page.show()

    def goto_contractor_page(self, checked):
        self.contractor_page = Contractor_Page()
        self.contractor_page.show()

    def goto_tenant_page(self, checked):
        self.tenant_page = tenantsui(self.Cont_TenantPage)
        self.tenant_page.show()

    def sign_out(self, checked):
        self.close()
        self.is_signout = True
        