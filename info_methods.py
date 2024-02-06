import webbrowser
from PyQt5.QtWidgets import QMessageBox

class InfoHandler:
    @staticmethod
    def openCAMSInfo():
        url = "https://confluence.ecmwf.int/display/CKB/CAMS+Regional:+European+air+quality+analysis+and+forecast+data+documentation"
        webbrowser.open(url)

    @staticmethod
    def showVariableInfo():
        message = "Variables in CAMS data represent different atmospheric components and conditions, such as concentrations of gases, aerosols, and various pollutants. Each variable provides insights into specific aspects of air quality and atmospheric composition."
        QMessageBox.information(None, "Variable Information", message)

    @staticmethod
    def showModelInfo():
        message = "CAMS employs various atmospheric models to predict and analyze air quality. These models simulate the behavior of atmospheric pollutants and help in forecasting air quality, assessing pollution sources, and understanding atmospheric processes."
        QMessageBox.information(None, "Model Information", message)

    @staticmethod
    def showLevelInfo():
        message = "Levels in CAMS data refer to the atmospheric layers at different altitudes. Data is available for multiple levels, providing a vertical profile of atmospheric conditions. This is crucial for understanding phenomena like vertical distribution of pollutants."
        QMessageBox.information(None, "Level Information", message)

    @staticmethod
    def showTimeInfo():
        message = "Time information in CAMS data includes historical, near-real-time, and forecast data. The time selection allows users to focus on specific periods for analysis, ranging from past trends to future predictions."
        QMessageBox.information(None, "Time Information", message)

    @staticmethod
    def showLeadTimeInfo():
        message = "Lead time in CAMS forecasts refers to the time span between the forecast issuance and the actual period for which the forecast is made. It is vital for planning and decision-making, especially in response to air quality emergencies."
        QMessageBox.information(None, "Lead Time Information", message)

    @staticmethod
    def showFormatInfo():
        message = "CAMS data is available in various formats suitable for different applications and analyses. Common formats include GRIB, and NetCDF, each offering unique advantages in terms of compatibility, detail, and ease of use."
        QMessageBox.information(None, "Format Information", message)

