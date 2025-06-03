import math

SPEED_AIR_MS = 330.0
SPEED_WATER_MS = 1500.0

MIDDLE_C_FREQUENCY = 261.63
MIN_HUMAN_FREQUENCY = 20.0
MAX_HUMAN_FREQUENCY = 20_000.0


class SoundWave(object):

    '''
    An immutable class representing the three 
    key characteristics of a sound wave:
    speed in metres/second (varies according to medium)
    wavelength in metres (varies according to medium)
    frequency  (constant across mediums)
    '''

    def __init__(self, 
                 speed_ms:float=math.nan, 
                 wavelength_m:float=math.nan, 
                 frequency_hz:float=math.nan):

        self._speed_ms = speed_ms
        self._wavelength_m = wavelength_m
        self._frequency_hz = frequency_hz

        self._calc_speed()
        self._calc_wavelength()
        self._calc_frequency()
    

    def __str__(self) -> str:

        str = []

        str.append(f"speed      {self._speed_ms}m/s\n")
        str.append(f"wavelength {self._wavelength_m}m\n")
        str.append(f"frequency  {self._frequency_hz}Hz")

        return "".join(str)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # pseudo-private functions #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~#

    def _calc_wavelength(self) -> None:

        # λ = V/f

        if math.isnan(self._wavelength_m) and \
           not math.isnan(self._frequency_hz) and \
           not math.isnan(self._speed_ms):

            self._wavelength_m = self._speed_ms / self._frequency_hz


    def _calc_frequency(self) -> None:

        # f = V/λ

        if math.isnan(self._frequency_hz) and \
           not math.isnan(self._wavelength_m) and \
           not math.isnan(self._speed_ms):

            self._frequency_hz = self._speed_ms / self._wavelength_m
        

    def _calc_speed(self) -> None:

        # V = fλ

        if math.isnan(self._speed_ms) and \
           not math.isnan(self._wavelength_m) and \
           not math.isnan(self._frequency_hz):

            self._speed_ms = self._frequency_hz * self._wavelength_m
        
