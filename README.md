# MMISiteTester- By Dirk
Python Automated Site Testing Tool

dependencies: splinter, six & gecko

### user control commands

`screen_shot()`   - takes a single screen shot at browsers current position

`page_shot()`     - takes a set of shots of an entire page 

`refresh()`       - refreshes page and scrolls to top

`desktop() `      - sets browser to standard desktop resolution for screenshot testing

`tablet() `       - sets browser to standard tablet resolution for screenshot testing

`mobile() `       - sets browser to standard mobile resolution for screenshot testing

`login()`         - login currently set up for *PRE MMI* environment
                - logs current browser load speed
                
`end()`           - closes browser and logs results

`btn_with_text()` - navigate to new page via a button with specific text 

`nav_to()`        - add extended friendly url to navigate on the *PRE MMI* environment

`scroll_to_class()` - scroll to specific element via its class name

`scroll_to_id()`  - scroll to specific element via its id name

**To make use of the private credentials either add your own registered user and password 
or add mmi_data in the credentials.py include:**

`pvt_username = '#######'`

`pvt_password = '#######'`


