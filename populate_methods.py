import logging

class PopulateComboBoxes:
    def __init__(self):
        # Static data for each category
        self.variables = [
            'alder_pollen', 'carbon_monoxide', 'glyoxal', 'nitrogen_dioxide', 
            'olive_pollen', 'particulate_matter_10um', 'pm10_sea_salt_dry',
            'residential_elementary_carbon', 'total_elementary_carbon', 
            'ammonia', 'dust', 'grass_pollen', 'nitrogen_monoxide', 'ozone',
            'peroxyacyl_nitrates', 'pm10_wildfires', 'secondary_inorganic_aerosol',
            'birch_pollen', 'formaldehyde', 'mugwort_pollen', 'non_methane_vocs',
            'particulate_matter_2.5um', 'pm2.5_total_organic_matter', 'ragweed_pollen', 
            'sulphur_dioxide'
        ]
        self.models = [
            'chimere', 'dehm', 'emep', 'ensemble', 'euradim', 'gemaq', 'lotos', 
            'match', 'minni', 'mocage', 'monarch', 'silam'
        ]
        self.levels = ['0', '50', '100', '250', '500', '750', '1000', '2000', '3000', '5000']
        self.types = ['analysis', 'forecast']
        self.times = [
            '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', 
            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', 
            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', 
            '21:00', '22:00', '23:00'
        ]
        self.formats = ['netcdf', 'grib']
        self.leadtime_hours = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
            '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
            '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
            '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
            '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
            '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
            '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
            '91', '92', '93', '94', '95', '96'
        ]

    def populate_combo_box(self, combo_box, items):
        """Generic method to populate a combo box with given items."""
        logging.debug("Populating combo box with items: %s", items)
        combo_box.clear()
        for item in items:
            combo_box.addItem(item)
        logging.debug("Finished populating combo box.")

    def populate_variable_combo_box(self, combo_box):
        self.populate_combo_box(combo_box, self.variables)

    def populate_model_combo_box(self, combo_box):
        self.populate_combo_box(combo_box, self.models)

    def populate_level_combo_box(self, combo_box):
        self.populate_combo_box(combo_box, self.levels)

    def populate_type_combo_box(self, combo_box):
        self.populate_combo_box(combo_box, self.types)

    def populate_format_combo_box(self, combo_box):
        self.populate_combo_box(combo_box, self.formats)

    def populate_list_widget(self, list_widget, items):
        """Generic method to populate a list widget with given items."""
        logging.debug("Populating list widget with items: %s", items)
        list_widget.clear()
        for item in items:
            list_widget.addItem(item)
        logging.debug("Finished populating list widget.")

    def populate_time_list_widget(self, list_widget):
        """Populate the time list widget."""
        self.populate_list_widget(list_widget, self.times)

    def populate_leadtime_hour_list_widget(self, list_widget):
        """Populate the leadtime hour list widget."""
        self.populate_list_widget(list_widget, self.leadtime_hours)

