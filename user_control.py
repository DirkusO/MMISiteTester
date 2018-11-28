from browser_controller import browser_control as control
from mmi_data import credentials as cred

# user control here

control.login(username=cred.pvt_username, password=cred.pvt_password)

control.mobile()
control.page_shot('mobile_dashboard')

control.nav_to('/my-engaged/safety/safe-dayz/safe-dayz-dashboard')



control.end()
