System.setProperty("webdriver.chrome.driver","E:\\Roma\\prog\\Java\\project\\yandex\\driver\\chromedriver.exe")
opt = new ChromeOptions()
opt.setBinary("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
opt.addArguments("--user-data-dir=C:\\Users\\Roma\\AppData\\Local\\Google\\Chrome\\User Data")
ChromeDriver driver=new ChromeDriver(opt)

driver.get("https://site.ru/checkout")
