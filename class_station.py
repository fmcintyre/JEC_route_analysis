class station:
    """
    A class to represent a single station.

    ...

    Attributes
    ----------
    station_id : str
        unique ID for the station
    station_name : str
        name of the station
    station_description : str
        description of where the station is located
    station_latitude : float
        decimal degrees for latitude (in WGS84) of the station
    station_longitude : float
        decimal degrees for longitude (in WGS84) of the station

    Methods
    -------
    method1(argument=""):
        Description of method.
    """
    def __init__(self,station_id = None, station_name = None, station_description = None, station_latitude = None, station_longitude = None):
        """
        Constructs all the necessary attributes for the station object.

        Parameters
        ----------
            station_id : str
                unique ID for the station
            station_name : str
                name of the station
            station_description : str
                description of where the station is located
            station_latitude : float
                decimal degrees for latitude (in WGS84) of the station
            station_longitude : float
                decimal degrees for longitude (in WGS84) of the station
        """

        self.station_id = station_id
        self.station_name = station_name
        self.station_description = station_description
        self.station_latitude = station_latitude
        self.station_longitude = station_longitude
