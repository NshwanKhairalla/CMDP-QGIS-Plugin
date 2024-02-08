---
__CMDP-QGIS-Plugin __

- __[QGIS-CMDP (QGIS Copernicus Managing Data Plugin)](https://github.com/NshwanKhairalla/CMDP-QGIS-Plugin.git/)__ - Download data from Copernicus Atmosphere Monitoring Service (CAMS).
- __[Politecnico di Milano](https://www.polimi.it/)__ - Polimi website.


---

# QGIS-CMDP (QGIS Copernicus Managing Data Plugin)
The plugin's purpose is to download data from Copernicus Atmosphere Monitoring Service (CAMS).
The CMDP plugin enables users to download atmospheric data directly within the ǪGIS environment.
Users can specify various parameters for the data they wish to download.
The plugin seamlessly connects to the Copernicus Atmosphere Monitoring Service (CAMS) database, allowing users to access and download a wide range of atmospheric datasets.

---

## How to install it:
### The CMDP plugin is designed for ease of installation and setup, ensuring users can quickly start utilizing its features:
Users can download the code from the Github repository in ZIP file.
Through the ǪGIS Plugin Manager install the plugin from the choice install from ZIP. 
Located within the ǪGIS toolbar or menu after installation.
The 'cdsapi' Python package is required.
Install it via pip:
pip install cdsapi
Setting Up CAMS API Access:
Register and obtain your User ID and API Key from the CAMS account at https://cds.climate.copernicus.eu/.
Create a '.cdsapirc' file in your home directory with your CAMS credentials. Place this file in:
Windows: C:\Users\<YourUsername>\.cdsapirc
macOS/Linux: /home/<YourUsername>/.cdsapirc
Content format:
url:https://ads.atmosphere.copernicus.eu/api/v2
key:[Your-UID]:[Your-API-Key]
Replace [Your-UID] and [Your-API-Key] with your actual details.

---

## How it works:
### The plugin consists of 4 tabs:
login tab, area of interest tab, data download tab, and help tab.
In the login tab users enter their user ID and API key, with the possibility of saving the credentials.
In the area of interest tab users can specify their area of interest using coordinates or shapefiles.
In the download data tab selection of variables, models, levels, and types from dropdown menus, choice of time frame and data format for the download.
Click ‘Download Data’ to start the retrieval process. Progress is displayed via a progress bar. 
Once downloaded, data can be visualized and analyzed within ǪGIS.
In the help tab the user is introduced to clear and simple instructions on how to use the plugin.

---

## Developed by:
The CMDP plugin was developed as part of the course Geoinformatics Project at the university of Politecnico di Milano (Polimi).
#### Name of the project:
A QGIS plugin for managing Copernicus Atmosphere Monitoring Service (CAMS) data.
#### The instructor of the course is:
Prof. Mariagrazia Fugini 
Politecnico di Milano.
Department of Electronics, Information and Bioengineering.
#### Supervision of the project:
Prof. Maria Antonia Brovelli, Lorenzo Amici.
Politecnico di Milano.
Professor of GIS and Digital Mapping.
#### Student:
Nshwan Ali Abdalla Khairalla.
Politecnico di Milano.
MSc student of Geoinformatics.
