# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CMDPDialog
                                 A QGIS plugin
 QGIS plugin for importing and analyzing CAMS (Copernicus Atmosphere Monitoring Service) data. 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-10-09
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Polimi
        email                : nshwan.khairalla@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Importing necessary modules and classes at the top
import cdsapi  # For connecting to the CAMS website
import os
from datetime import datetime
import logging
import time
import threading
from pyproj import Transformer
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView
from PyQt5 import QtCore, QtGui, QtWidgets
from qgis.PyQt import uic, QtWidgets, QtCore
from qgis.PyQt.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialog
from qgis.utils import iface # This is used by QGIS
from qgis.PyQt.QtCore import QSettings  # For displaying error messages
from qgis.core import QgsGeometry, QgsPointXY, QgsCoordinateTransform, QgsProject, QgsCoordinateReferenceSystem, QgsMapLayer, QgsWkbTypes
from PyQt5.QtWidgets import QMessageBox # For showing messages to the user
from PyQt5.QtWidgets import QProgressBar  # Import QProgressBar To show a progress bar
from .ui_CMDP_dialog import Ui_CMDPDialogBase # This is the user interface file
from .populate_methods import PopulateComboBoxes #This is for the combo boxes methods
from .info_methods import InfoHandler

# Load the .ui file so that PyQt can populate the plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'CMDP_dialog_base.ui'))

class CMDPDialog(QDialog):
    def __init__(self, iface, cmdp_instance, parent=None):
        self.iface = iface
        super(CMDPDialog, self).__init__(parent)
        self.ui = Ui_CMDPDialogBase()
        self.ui.setupUi(self)  # Setup UI using the generated class
        logging.debug("UI components are set up")
        self.setWindowTitle("CMDP - CAMS Managing Data Plugin")
        self.cmdp_instance = cmdp_instance
        # Setup UI and other initializations
        logging.debug("Initializing CMDPDialog UI")
        # Further configurations
        self.setupConnections()
        logging.debug("UI connections are set up")
        self.cams_client = None  # Initialize cams_client attribute
        logging.debug(f"CAMS Client Initialized: {self.cams_client is not None}")
        # Initialize user_id and api_key as empty strings or None
        self.user_id = ""
        self.api_key = ""
        self.loadSavedCredentials()  # Load saved credentials
        self.displayHelpText()  # To display the help text
        self.populate_combo_boxes = PopulateComboBoxes()
        self.ui.pBCancel.clicked.connect(self.closePlugin)
        # Connect the folder choose button to the method
        self.ui.tBChooseFolder.clicked.connect(self.chooseFolder)
        self.initGui()
        # Populate combo boxes immediately
        self.populate_combo_boxes.populate_variable_combo_box(self.ui.cBVariable)
        self.populate_combo_boxes.populate_model_combo_box(self.ui.cBModel)
        self.populate_combo_boxes.populate_level_combo_box(self.ui.cBLevel)
        self.populate_combo_boxes.populate_type_combo_box(self.ui.cBType)
        self.populate_combo_boxes.populate_format_combo_box(self.ui.cBFormat)
        self.populate_combo_boxes.populate_time_list_widget(self.ui.lWTime)
        self.populate_combo_boxes.populate_leadtime_hour_list_widget(self.ui.lWLeadTime)
        # Checking if pBDownloadDataProgress exists in the UI
        if hasattr(self.ui, "pBDownloadDataProgress"):
            # Creating a QProgressBar widget
            self.progress_bar = QProgressBar(self.ui.pBDownloadDataProgress)
            self.progress_bar.setMinimum(0)
            self.progress_bar.setMaximum(100)
            self.progress_bar.setValue(0)
        else:
            # Handling the case where pBDownloadDataProgress is missing
            print("Warning: pBDownloadDataProgress is missing from the UI")
            self.progress_bar = None

    def initGui(self):
        #tAOI
        # Connects the radio buttons to the handleRadioClick function
        self.ui.rBFullModelArea.toggled.connect(self.handleRadioClick)
        self.ui.rBRestrictedArea.toggled.connect(self.handleRadioClick)
        #tDataImport
        self.ui.cBTermsAndConditions.stateChanged.connect(self.handleTermsAndConditions)
        # Connects the "Import" button to the handleDownload function
        self.ui.pBDownloadData.clicked.connect(self.handleDownload)
        # Populates the shape file combo box with available layers
        self.populateShapeFileComboBox()
        # Info connections
        self.ui.pBCAMSInfo.clicked.connect(InfoHandler.openCAMSInfo)
        self.ui.pBVariableInfo.clicked.connect(InfoHandler.showVariableInfo)
        self.ui.pBModelInfo.clicked.connect(InfoHandler.showModelInfo)
        self.ui.pBLevelInfo.clicked.connect(InfoHandler.showLevelInfo)
        self.ui.pBTimeInfo.clicked.connect(InfoHandler.showTimeInfo)
        self.ui.pBLeadTimeInfo.clicked.connect(InfoHandler.showLeadTimeInfo)
        self.ui.pBFormatInfo.clicked.connect(InfoHandler.showFormatInfo)

    def PopulateComboBoxes(self):
        # Use the class methods to populate combo boxes
        if self.cams_client:
            self.populate_combo_boxes.populate_variable_combo_box(self.ui.cBVariable)
            self.populate_combo_boxes.populate_model_combo_box(self.ui.cBModel)
            self.populate_combo_boxes.populate_level_combo_box(self.ui.cBLevel)
            self.populate_combo_boxes.populate_type_combo_box(self.ui.cBType)
            self.populate_combo_boxes.populate_format_combo_box(self.ui.cBFormat)

            # Populate list widgets and set selection mode for multi-selection
            self.populate_combo_boxes.populate_time_list_widget(self.ui.lWTime)
            self.populate_combo_boxes.populate_leadtime_hour_list_widget(self.ui.lWLeadTime)
            self.ui.lWTime.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
            self.ui.lWLeadTime.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        else:
            QMessageBox.warning(self, "Warning", "CAMS client not initialized. Please connect first.")

    def saveCredentials(self):
        """Saves user credentials to QSettings."""
        try:
            # Fetch credentials from the UI elements
            user_id = self.ui.lEUserId.text().strip()  # Assuming lEUserId is the line edit for the user ID
            api_key = self.ui.lEApiKey.text().strip()  # Assuming lEApiKey is the line edit for the API key

            # Check if credentials are not empty
            if not user_id or not api_key:
                QMessageBox.warning(self, "Warning", "User ID and API Key cannot be empty.")
                return False

            # Create QSettings object for persistent storage
            settings = QSettings()
            settings.beginGroup("CMDP")

            # Save credentials in settings
            settings.setValue("user_id", user_id)
            settings.setValue("api_key", api_key)
            settings.endGroup()

            logging.debug(f"Credentials saved: User ID - {user_id}, API Key - {api_key}")
            return True

        except Exception as e:
            logging.error(f"Error saving credentials: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred while saving credentials: {str(e)}")
            return False

    def loadSavedCredentials(self):
        # Create QSettings object
        settings = QSettings()

        # Load saved credentials if they exist
        saved_user_id = settings.value("CMDP/user_id", "")
        saved_api_key = settings.value("CMDP/api_key", "")

        logging.debug(f"Loaded credentials: User ID - {saved_user_id}, API Key - {saved_api_key}")

        if saved_user_id and saved_api_key:
            self.ui.lEUserId.setText(saved_user_id)
            self.ui.lEApiKey.setText(saved_api_key)

    def populateShapeFileComboBox(self):
        # Clear any existing items in the combo box
        self.ui.cBShapeFile.clear()

        # Iterate over layers and add shapefile layers to the combo box
        for layer in QgsProject.instance().mapLayers().values():
            if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == QgsWkbTypes.PolygonGeometry:
                self.ui.cBShapeFile.addItem(layer.name(), layer)

        # Handle the state of coordinate input fields based on the selected radio button
        if self.ui.rBRestrictedArea.isChecked():
            # Enable the input fields for North, South, East, and West coordinates
            self.ui.lENorth.setEnabled(True)   # North
            self.ui.lEWest.setEnabled(True) # West
            self.ui.lESouth.setEnabled(True) # South
            self.ui.lEEast.setEnabled(True) # East
        else:
            # Disable the input fields for coordinates
            self.ui.lENorth.setDisabled(True)
            self.ui.lEWest.setDisabled(True)
            self.ui.lESouth.setDisabled(True)
            self.ui.lEEast.setDisabled(True)

            self.ui.lENorth.clear()
            self.ui.lEWest.clear()
            self.ui.lESouth.clear()
            self.ui.lEEast.clear()

    def handleRadioClick(self):
        # Checks which radio button is selected
        if self.ui.rBFullModelArea.isChecked():
            # If "Full Model Area" is selected, disable the input fields for the restricted area
            self.ui.lENorth.setEnabled(False)
            self.ui.lEWest.setEnabled(False)
            self.ui.lESouth.setEnabled(False)
            self.ui.lEEast.setEnabled(False)
            self.ui.cBShapeFile.setDisabled(True)

        elif self.ui.rBRestrictedArea.isChecked():
            # If "Restricted Area" is selected, enable the input fields
            self.ui.lENorth.setEnabled(True)
            self.ui.lEWest.setEnabled(True)
            self.ui.lESouth.setEnabled(True)
            self.ui.lEEast.setEnabled(True)
            self.ui.cBShapeFile.setDisabled(True)

        elif self.ui.rBAddShapeFile.isChecked():
            # If "Add Shape File" is selected, disable the coordinate input fields and enable the shapefile combo box
            self.ui.lENorth.setDisabled(True)
            self.ui.lEWest.setDisabled(True)
            self.ui.lESouth.setDisabled(True)
            self.ui.lEEast.setDisabled(True)
            self.ui.cBShapeFile.setEnabled(True)
            self.populateShapeFileComboBox()

    def handleTermsAndConditions(self):
        # Gets the state of the "Terms and Conditions" checkbox
        terms_checked = self.ui.cBTermsAndConditions.isChecked()

        # Log the state of the checkbox or handle other UI changes as necessary
        if terms_checked:
            logging.debug("Terms and Conditions have been agreed to.")
        else:
            logging.debug("Terms and Conditions have not been agreed to.")

    def constructRequestParameters(self, variable, model, level, type, format, time_choices, leadtime_hour_choices, start_date, end_date):
        logging.debug("Entering constructRequestParameters method")
        try:
            # Basic input validation
            if not all([variable, model, level, type, format, start_date, end_date]):
                raise ValueError("Please ensure all required fields are filled.")

            # Validate and format dates
            start_date, end_date = self.validateAndFormatDates(start_date, end_date)

            # Extract time and leadtime hour choices from list widgets
            time_choices = self.getSelectedItems(self.ui.lWTime)
            leadtime_hour_choices = self.getSelectedItems(self.ui.lWLeadTime)

            # Construct parameters dictionary
            parameters = {
            'variable': variable,
            'model': model,
            'level': level,
            'type': type,
            'format': format,
            'time': time_choices, 
            'leadtime_hour': leadtime_hour_choices,
            'date': f"{start_date}/{end_date}",
            }

            # Handle area parameter
            if self.ui.rBRestrictedArea.isChecked():
                parameters['area'] = self.getRestrictedAreaCoordinates()
            elif self.ui.rBAddShapeFile.isChecked():
                parameters['area'] = self.getShapefileArea()

            logging.info(f"Request parameters constructed: {parameters}")
            return parameters

        except ValueError as e:
            logging.error(f"Input validation error in constructRequestParameters: {e}")
            QMessageBox.warning(self, "Input Validation Error", str(e))
            raise

    def validateAndFormatDates(self, start_date_str, end_date_str):
        # Convert and validate date strings
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
    def getSelectedItems(self, list_widget):
        # Extract selected items from a list widget
        selected_items = [item.text() for item in list_widget.selectedItems()]
        return selected_items

    def getRestrictedAreaCoordinates(self):
        # Validate and return restricted area coordinates
        north = self.ui.lENorth.text().strip()
        west = self.ui.lEWest.text().strip()
        south = self.ui.lESouth.text().strip()
        east = self.ui.lEEast.text().strip()
        if not all([north, west, south, east]):
            raise ValueError("All coordinates (North, West, South, East) are required for restricted area.")
        return [north, west, south, east]

    def getShapefileArea(self):
        # Extract bounding box from selected shapefile
        selected_shapefile = self.ui.cBShapeFile.currentData()
        if not selected_shapefile:
            raise ValueError("No shapefile selected.")
        return self.extractBoundingBoxFromShapefile(selected_shapefile)

    def extractBoundingBoxFromShapefile(self, shapefile_layer):
        if not shapefile_layer or not shapefile_layer.isValid():
            logging.error("Invalid or non-existent shapefile layer.")
            return None

        try:
            # Initialize the bounding box variables
            min_x, min_y, max_x, max_y = None, None, None, None

            # Iterate over each feature (polygon) in the shapefile
            for feature in shapefile_layer.getFeatures():
                geom = feature.geometry()
                if geom:
                    bbox = geom.boundingBox()
                    # Update the bounding box variables
                    if min_x is None or bbox.xMinimum() < min_x:
                        min_x = bbox.xMinimum()
                    if min_y is None or bbox.yMinimum() < min_y:
                        min_y = bbox.yMinimum()
                    if max_x is None or bbox.xMaximum() > max_x:
                        max_x = bbox.xMaximum()
                    if max_y is None or bbox.yMaximum() > max_y:
                        max_y = bbox.yMaximum()

            # Transform the coordinates if the CRS is different from WGS 84
            source_crs = shapefile_layer.crs()
            dest_crs = QgsCoordinateReferenceSystem(4326)  # WGS 84
            transform = QgsCoordinateTransform(source_crs, dest_crs, QgsProject.instance())

            # Transform the points to the destination CRS
            lower_left = transform.transform(QgsPointXY(min_x, min_y))
            upper_right = transform.transform(QgsPointXY(max_x, max_y))

            # Ensure north is greater than south
            north = max(lower_left.y(), upper_right.y())
            south = min(lower_left.y(), upper_right.y())

            return [north, lower_left.x(), south, upper_right.x()]

        except Exception as e:
            logging.error(f"Error extracting bounding box: {e}")
            return None

    #Downloads the data
    def handleDownload(self):
        logging.debug("handleDownload method called")

        # Validate Terms and Conditions
        if not self.ui.cBTermsAndConditions.isChecked():
            logging.warning("Terms and Conditions not checked")
            QMessageBox.warning(self, "Warning", "You must agree to the terms and conditions to import data.")
            return

        # Fetch user inputs from UI elements
        logging.debug("Fetching user inputs from UI elements")
        selected_product = "cams-europe-air-quality-forecasts"  # Replace with actual product selection logic
        selected_variable = self.ui.cBVariable.currentText()
        selected_model = self.ui.cBModel.currentText()
        selected_level = self.ui.cBLevel.currentText()
        selected_type = self.ui.cBType.currentText()
        selected_format = self.ui.cBFormat.currentText()

        # Get selections for Time and Leadtime Hour
        time_choices = [item.text() for item in self.ui.lWTime.selectedItems()]
        leadtime_hour_choices = [item.text() for item in self.ui.lWLeadTime.selectedItems()]

        start_date = self.ui.dTEStartDate.date().toString("yyyy-MM-dd")
        end_date = self.ui.dTEEndDate.date().toString("yyyy-MM-dd")
        logging.debug(f"Selected parameters: Variable - {selected_variable}, Model - {selected_model}, Level - {selected_level}, Type - {selected_type}, Format - {selected_format}, Time - {time_choices}, Leadtime Hour - {leadtime_hour_choices}, Date Range - {start_date} to {end_date}")

        try:
            # Construct request parameters
            request_parameters = self.constructRequestParameters(
                selected_variable, selected_model, selected_level, selected_type, selected_format,
                time_choices, leadtime_hour_choices, start_date, end_date
            )

            # Use the folder path from the QLineEdit where the user selected the folder
            folder_path = self.ui.tBChooseFolder.text()
            if not folder_path:
                logging.info("No folder selected for saving data.")
                QMessageBox.warning(self, "Warning", "Please select a folder to save the data.")
                return

            # File path for saving downloaded data
            output_file = os.path.join(folder_path, f"CAMS_{selected_variable}_{selected_model}_{selected_type}_{start_date}_{end_date}.nc")

            # Initiate the download process
            if self.downloadCAMSData(selected_product, request_parameters, output_file):
                # Check if the downloaded data is available/valid
                if self.isDataAvailable(output_file):
                    QMessageBox.information(self, "Success", f"Data downloaded and saved to {output_file}")
                else:
                    QMessageBox.warning(self, "Warning", "Data is not available for the selected parameters.")
            else:
                QMessageBox.warning(self, "Warning", "Data download failed. Please check the logs for details.")

        except Exception as e:
            logging.error(f"Error in handleDownload: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def validateUserInputs(self, selected_variable, selected_model, selected_level, selected_type, selected_format, selected_time, selected_leadtime_hour, start_date, end_date):
        # Check if any parameter is empty or invalid
        if not all([selected_variable, selected_model, selected_level, selected_type, selected_format, selected_time, selected_leadtime_hour, start_date, end_date]):
            QMessageBox.warning(self, "Warning", "All fields must be filled.")
            return False

        return True  # Return True if all validations pass
    
    def downloadCAMSData(self, product, request_parameters, output_file):
        logging.debug("downloadCAMSData method called")
        logging.debug(f"Product: {product}, Output file: {output_file}")
        logging.debug(f"Request parameters: {request_parameters}")

        try:
            # Initialize the cdsapi client
            logging.info("Initiating connection to CAMS API")
            cds_client = cdsapi.Client()
            cds_client.verify = True  # Enabling SSL certificate verification

            # Start a background thread for downloading
            download_thread = threading.Thread(target=self.runDownload, args=(cds_client, product, request_parameters, output_file))
            download_thread.start()

            # Update the progress bar in the main thread
            for i in range(101):
                time.sleep(0.1)  # Update every 0.1 seconds
                self.ui.pBDownloadDataProgress.setValue(i)

            download_thread.join()  # Wait for the download thread to finish
            logging.info(f"Data successfully downloaded to {output_file}")
            return True

        except Exception as e:
            logging.error(f"Error during data download: {e}")
            return False
 
    def isDataAvailable(self, output_file):
        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
            return True
        return False

    def runDownload(self, cds_client, product, request_parameters, output_file):
        # This method runs in a separate thread to perform the download
        try:
            cds_client.retrieve(product, request_parameters, output_file)
        except Exception as e:
            logging.error(f"Error in downloading data: {e}")

    def displayHelpText(self):
        # Define the help content here
        help_text = (
        "Welcome to the CMDP - CAMS Managing Data Plugin!\n\n"
        "This plugin enables you to connect to the Copernicus Atmosphere Monitoring Service (CAMS) "
        "and import atmospheric data for analysis and visualization within QGIS.\n\n"

        "Installation and Setup Instructions:\n"
        "1. Prerequisites:\n"
        "   - Ensure QGIS is installed on your system.\n"
        "   - Python must be installed and accessible within QGIS.\n"
        "   - The 'cdsapi' Python package is required. Install it via pip:\n"
        "       pip install cdsapi\n"
        "   - The 'pyproj' Python package is required. Install it via pip:\n"
        "       pip install pyproj\n"
        "2. Setting Up CAMS API Access:\n"
        "   - Register and obtain your User ID and API Key from the CAMS account at https://cds.climate.copernicus.eu/.\n"
        "   - Create a '.cdsapirc' file in your home directory with your CAMS credentials. Place this file in:\n"
        "       - Windows: C:\\Users\\<YourUsername>\\.cdsapirc\n"
        "       - macOS/Linux: /home/<YourUsername>/.cdsapirc\n"
        "       Content format:\n"
        "           url:https://ads.atmosphere.copernicus.eu/api/v2\n"
        "           key:[Your-UID]:[Your-API-Key]\n"
        "       Replace [Your-UID] and [Your-API-Key] with your actual details.\n"
        "3. Plugin Installation:\n"
        "   - Download and install the CMDP plugin through the QGIS plugin repository or provided source.\n\n"

        "Usage Instructions:\n"
        "1. Plugin Setup:\n"
        "   - After opening the CMDP plugin, ensure your User ID and API Key are entered in the Login tab if not saved from a previous session.\n"
        "   - Credentials can be saved for future sessions.\n"
        "2. Configuring Data Import:\n"
        "   - In the 'Area Of Interest' tab, select your area of interest:\n"
        "       - 'Full Model Area' for the complete available data range.\n"
        "       - 'Restricted Area': Specify the geographical coordinates for a custom area. Enter the North, South, East, and West boundaries using decimal degrees in the World Geodetic System 1984 (WGS 84) coordinate system. For example, North: 45.00, South: 40.00, East: 10.00, West: 5.00. This will define a rectangular area for data extraction.\n"
        "       - 'Add Shape File' to choose a shapefile from QGIS layers to define the area.\n"
        "   - In the 'Import Data' tab, choose the desired variables, model, level, type, format, time, and lead time for the data.\n"
        "       - Note: When selecting 'Analysis' as Type, the Lead Time should be set to 0.\n"
        "       - For 'Forecast' Type, the Time should be set to 00:00.\n"
        "       - Some variables like 'pollen' do not have 'Analysis' data available.\n"
        "   - Set the start and end dates for the data range.\n"
        "   - Read the file licence to use copernicus products, and agree to the terms and conditions before importing data.\n"
        "3. Data Import:\n"
        "   - Click 'Import Data' to begin the data download process. Monitor progress via the progress bar.\n"
        "   - On successful download, the data will be saved to the home directory location and ready for use in QGIS.\n"
        "   - Incase the data is not available , the data will not be downloaded or saved to the home directory location and you must check the log for details.\n\n"

        "Logging and Troubleshooting:\n"
        "   - The plugin generates a log file to help with troubleshooting. You can find the log file at:\n"
        "       - Windows: C:\\Users\\<YourUsername>\\cmdp_plugin.log\n"
        "       - macOS/Linux: /home/<YourUsername>/cmdp_plugin.log\n"
        "For assistance, troubleshooting, or to provide feedback, refer to the detailed documentation "
        "or contact us at nshwan.khairalla@gmail.com. We appreciate your feedback for improving this plugin.\n\n"

        "Thank you for using the CMDP - CAMS Managing Data Plugin!"
    )


        # Sets the help text in the QTextEdit (or QLabel) within the tHelp tab
        self.ui.tEHelp.setText(help_text)

    def hideHelpText(self):
        # Clears the help text in the QTextEdit (or QLabel) within the tHelp tab
        self.ui.tEHelp.clear()

    def run(self):
        self.dlg = CMDPDialog(self.iface)  # Passes iface as an argument
        self.dlg.show()
    
    def unload(self):
        """
        Perform any cleanup tasks specific to the dialog when unloading the plugin.
        """
        # Close the dialog if it's open
        if self.isVisible():
            self.close()

        # Additional dialog-specific cleanup code can go here
        # ...

    def setupConnections(self):
        logging.debug("Connecting signals and slots")
        # Radio button connections
        self.ui.rBFullModelArea.toggled.connect(self.handleRadioClick)
        logging.debug("Connected: rBFullModelArea toggled to handleRadioClick")
        # Update the connection to use the correct radio button name
        self.ui.rBRestrictedArea.toggled.connect(self.handleRadioClick)
        logging.debug("Connected: rBRestrictedArea toggled to handleRadioClick")
        self.ui.rBAddShapeFile.toggled.connect(self.handleRadioClick)
        # Checkbox connection
        self.ui.cBTermsAndConditions.stateChanged.connect(self.handleTermsAndConditions)
        logging.debug("Connected: cBTermsAndConditions state changed to handleTermsAndConditions")

    def populate_combo_box(self, combo_box, items):
        self.updating_combobox = True  # Set the flag
        combo_box.clear()
        for item in items:
            combo_box.addItem(item)
        self.updating_combobox = False  # Reset the flag
    
    def closePlugin(self):
        self.close()

    def chooseFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            # Set the selected folder path to the QLineEdit
            self.ui.tBChooseFolder.setText(folder_path)



# Imports, class definition, and methods go here

# The existing code for running the plugin within QGIS
if __name__ == "__main__":
    try:
        import sys
        from qgis.PyQt.QtWidgets import QApplication
        from qgis.core import QgsApplication
        #Initializing the QGIS application
        qgs = QgsApplication([], False)
        qgs.initQgis()
        # Starting the application
        app = QApplication(sys.argv)
        dialog = CMDPDialog(iface)
        dialog.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
