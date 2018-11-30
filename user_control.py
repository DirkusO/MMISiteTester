from browser_controller import browser_control as control
from mmi_data import credentials as cred
from mmi_data import friendly_urls as page

###
# Page Portlet And Service Test
###
control.login(username=cred.pvt_username, password=cred.pvt_password)

# Initiate
control.test_service()
control.test_portlet()


def test_kit(url):
    control.nav_to(url)
    control.test_service()
    control.test_portlet()
    control.test_wcm()


for i in page.friendly_urls:
    test_kit(i)

control.end()
