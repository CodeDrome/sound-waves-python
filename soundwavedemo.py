import soundwave as sw


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Sound Wave    |")
    print("-----------------\n")

    # set speed and frequency
    # SoundWave class calculates wavelength
    air = sw.SoundWave(speed_ms=sw.SPEED_AIR_MS, frequency_hz=500.0)
    water = sw.SoundWave(speed_ms=sw.SPEED_WATER_MS, frequency_hz=500.0)

    print(air)
    print()
    print(water)

    # set speed and wavelength
    # SoundWave class calculates frequency
    air = sw.SoundWave(speed_ms=sw.SPEED_AIR_MS, wavelength_m=0.66)
    water = sw.SoundWave(speed_ms=sw.SPEED_WATER_MS, wavelength_m=3.0)

    print("-"*32)

    print(air)
    print()
    print(water)

    # set frequency and wavelength
    # SoundWave class calculates speed
    air = sw.SoundWave(frequency_hz=500.0, wavelength_m=0.66)
    water = sw.SoundWave(frequency_hz=500.0, wavelength_m=3.0)

    print("-"*32)

    print(air)
    print()
    print(water)

    #--------------------------------------------------------------

    print("-"*32)

    middle_c_air = sw.SoundWave(speed_ms=sw.SPEED_AIR_MS, frequency_hz=sw.MIDDLE_C_FREQUENCY)
    print(middle_c_air)

    print("-"*32)

    middle_c_air = sw.SoundWave(speed_ms=sw.SPEED_AIR_MS, frequency_hz=sw.MIN_HUMAN_FREQUENCY)
    print(middle_c_air)

    print("-"*32)

    middle_c_air = sw.SoundWave(speed_ms=sw.SPEED_AIR_MS, frequency_hz=sw.MAX_HUMAN_FREQUENCY)
    print(middle_c_air)

    print("-"*32)


if __name__ == "__main__":

    main()
