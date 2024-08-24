import configparser

read_content = configparser.RawConfigParser()
read_content.read(r"..\Configurations\config.ini")

# print(read_content.get("common data", "url"))
class ReadProperty:
    @staticmethod
    def GetUrl():
        return read_content.get("common data", "url")

    @staticmethod
    def GetUsername():
        return read_content.get("common data", "username")

    @staticmethod
    def GetPassword():
        return read_content.get("common data", "password")

    @staticmethod
    def GetChomeDriver():
        return read_content.get("driver path", "chrome_driver_path")
    @staticmethod
    def GetEdgeDriver():
        return read_content.get("driver path", "edge_driver_path")
    @staticmethod
    def GetFirefoxDriver():
        return read_content.get("driver path", "firefox_driver_path")