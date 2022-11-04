from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

proxy = f"{'p.webshare.io'}:9999"

class Browser:
    def __init__(self) -> None:
        pass

    
    def get_browser():
       
        chrome_options = Options()
        preferences = {
                "webrtc.ip_handling_policy": "disable_non_proxied_udp",
                "webrtc.multiple_routes_enabled": False,
                "webrtc.nonproxied_udp_enabled": False,
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            }

        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--proxy-server={proxy}")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-bundled-ppapi-flash")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("prefs", preferences)

        # chrome_options.add_extension(fr"./proxy_auth_plugin.zip")

        browser = webdriver.Chrome(ChromeDriverManager().install(),
            options=chrome_options,
        )
        return browser