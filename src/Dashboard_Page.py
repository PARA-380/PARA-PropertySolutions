"""
File: Dashboard_Page.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 03/20/2024
Description: Setting page user interface
Purposes: To provide the main dashboard for the entire application
"""
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
from System import Cont_UserProfile, Cont_Tenant, Cont_Contractor


class Dashboard(QMainWindow, Ui_DashBoard):
    """Represents the dashboard interface for the application.

    provides functionalities to navigate to different pages in the application.

    Args:
        QMainWindow (QMainWindow): The base class for the main window of the application.
        Ui_DashBoard (Ui_DashBoard): The user interface class for the dashboard with the assist of QtDesigner.
    """
    def __init__(self, Cont_UserProfile : Cont_UserProfile, Cont_TenantPage : Cont_Tenant):
        """Initialize the Dashboard instance.

        Args:
            Cont_UserProfile (Cont_UserProfile): An instance of Cont_UserProfile, 
                which handles user profile-related functionalities.
            Cont_TenantPage (Cont_Tenant): An instance of Cont_Tenant, which handles
                the Tenant page-related functionalities.
        """
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
        """Navigate to the property page.

        Args:
            checked (bool): Indicates whether the button is checked or not.
        """
        self.property_page = Property_Page()
        self.property_page.show()

    def goto_user_profile_page(self, checked):
        """Navigate to the user profile page.

        Args:
            checked (bool): Indicates whether the button is checked or not.
        """
        print(f"going to user profile page")
        self.user_profile = Userprofile(self.Cont_UserProfile)
        self.user_profile.show()

    def goto_setting_page(self, checked):
        """Navigate to the setting page.

        Args:
            checked (bool): Indicates whether the button is checked or not.
        """
        self.setting_page = Setting_Page()
        self.setting_page.show()

    def goto_notification_page(self, checked):
        """Navigate to the notification page.

        Args:
            checked (bool): Indicates whether the button is checked or not.
        """
        self.notification_page = Notification_Page()
        self.notification_page.show()

    def goto_contractor_page(self, checked):
        """Navigate to the contractor page.

        Args:
            checked (bool): Indicates whether the button is checked or not.
        """
        self.contractor_page = Contractor_Page(Cont_Contractor)
        self.contractor_page.show()

    def goto_tenant_page(self, checked):
        """Navigate to the tenant page.

        Args:
            checked (bool): Indicates whether the button is checked or not.
        """
        self.tenant_page = tenantsui(self.Cont_TenantPage)
        self.tenant_page.show()

    def sign_out(self, checked):
        """Navigate to the sign out page.

        Args:
            checked (bool): Indicates whether the button is checked or not.
        """
        self.close()
        self.is_signout = True
        