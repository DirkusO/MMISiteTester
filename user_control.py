from browser_controller import browser_control as control
from mmi_data import credentials as cred
from mmi_data import friendly_urls as page

###
# Page Portlet And Service Test
###
control.login(username=cred.pvt_username, password=cred.pvt_password)

# Initiate
control.test_service()


def test_kit(url):
    control.nav_to(url)
    control.test_service()


def snapshot_kit(url):
    control.nav_to(url)
    control.desktop()
    control.page_shot(url)
    control.mobile()
    control.page_shot(url)


for i in page.friendly_urls:
    test_kit(i)

for i in page.friendly_urls:
    snapshot_kit(i)

control.end()
