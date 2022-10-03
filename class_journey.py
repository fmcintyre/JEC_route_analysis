class journey:
    """
    A class to represent a single journey.

    ...

    Attributes
    ----------
    start_time : naive time object
        local time of day at beginning of the journey
    end_time : naive time object
        local time of day at end of the journey
    start_date : date object
        date at beginning of the journey
    end_date : date object
        date at end of the journey
    duration : int
        duration of the journey in seconds
    start_station : station object
        station at which the journey began
    end_station : station object
        station at which the journey ended

    Methods
    -------
    method1(argument=""):
        Description of method.
    """
    def __init__(self,start_time = None, start_date = None, end_time = None, end_date = None, duration = None, start_station = None, end_station = None):
        """
        Constructs all the necessary attributes for the journey object.

        Parameters
        ----------
            start_time : naive time object
                local time of day at beginning of journey
            end_time : naive time object
                local time of day at end of journey
            start_date : date object
                date at beginning of journey
            end_date : date object
                date at end of journey
            duration : int
                duration of journey in seconds
            start_station : station object
                station at which journey began
            end_station : station object
                station at which journey ended
        """

        self.start_time = start_time
        self.start_date = start_date
        self.end_time = end_time
        self.end_date = end_date
        self.duration = duration
        self.start_station = start_station
        self.end_station = end_station

    # Example of method/function and typical docstring
    #
    # def info(self, additional=""):
    #     """
    #     Prints the person's name and age.
    #
    #     If the argument 'additional' is passed, then it is appended after the main info.
    #
    #     Parameters
    #     ----------
    #     additional : str, optional
    #         More info to be displayed (default is None)
    #
    #     Returns
    #     -------
    #     None
    #     """
