# [MS-Teams-Auto-Joiner](https://github.com/atharva-lipare/MS-Teams-Auto-Joiner)

## Misc

if 
`config['dev'] == true`
```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/ekim/Library/Application Support/Google/Chrome/Profile 2" https://teams.microsoft.com/_#/calendarv2\n

```
## Troubleshooting Chromedriver & Chrome Browser version incompatibility

Due to driver restructuring by the Chromium Team for the new [Chrome-for-Testing](https://googlechromelabs.github.io/chrome-for-testing/), this prevents the use of [LATEST_RELEASE](https://chromedriver.storage.googleapis.com/LATEST_RELEASE) after v114 for auto-downloads with `selenium` v4.10.0 which includes `Selenium-Manager` that auto-downloads latest driver via that URL. 

Workaround solution #1: Get `chromedriver-autoinstall` library
    This seems to be a Mac issue. Did not bother to look into it further.

```
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
``` 
this used to work (solution #0?), but iirc it became redundant thanks to selenium version 4's `Service` class: 

```
from selenium.webdriver.chrome.service import Service

web_driver = webdriver.Chrome(
    service=Service(executable_path=chromedriver_exec_path),
    options=opts
)

```
But this doesn't work with a homebrew installed chromedriver executable path. This also requires manually updating chromedriver via homebrew which is very cumbersome and time-consuming:

Terminal
```
> which chromedriver
/opt/homebrew/bin/chromedriver

> chromedriver --version
ChromeDriver <someOldVersion>

> rm /opt/homebrew/bin/chromedriver
> chromedriver --version

> brew install --cask chromedriver
```
Program
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class DriverClass:

    def __init__(self):
        pass
  
    @staticmethod
    def _get_chromedriver_executable_path():
        return '/opt/homebrew/bin/chromedriver'
        
    def setup_driver(self):
        opts = webdriver.ChromeOptions()
        
        web_driver = webdriver.Chrome(
        service=Service(executable_path=self._get_chromedriver_executable_path()),
        options=opts
    )
```

Currently implemented working solution:

```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


        web_driver = webdriver.Chrome(
            service=Service(executable_path=ChromeDriverManager().install()),
            options=opts
        )
```

Console output
```
/Users/ekim/opt/anaconda3/envs/bots/bin/python -m src.app.__main__ 
2024-02-21 12:13:14,064 - INFO - Initializing ChromeDriver...
2024-02-21 12:13:14,064 - INFO - ====== WebDriver manager ======
2024-02-21 12:13:14,380 - INFO - Get LATEST chromedriver version for google-chrome
2024-02-21 12:13:14,384 - INFO - Get LATEST chromedriver version for google-chrome
2024-02-21 12:13:14,384 - INFO - There is no [mac64] chromedriver "122.0.6261.57" for browser google-chrome "122.0.6261.57" in cache
2024-02-21 12:13:14,395 - INFO - Get LATEST chromedriver version for google-chrome
2024-02-21 12:13:14,609 - INFO - WebDriver version 122.0.6261.57 selected
2024-02-21 12:13:14,610 - INFO - Modern chrome version https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.57/mac-x64/chromedriver-mac-x64.zip
2024-02-21 12:13:14,610 - INFO - About to download new driver from https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.57/mac-x64/chromedriver-mac-x64.zip
2024-02-21 12:13:14,836 - INFO - Driver downloading response is 200
2024-02-21 12:13:15,305 - INFO - Get LATEST chromedriver version for google-chrome
2024-02-21 12:13:15,430 - INFO - Driver has been saved in cache [/Users/ekim/.wdm/drivers/chromedriver/mac64/122.0.6261.57]

Process finished with exit code 0
```
