def sec_2_human_readable(seconds: int) -> str:
    if seconds < 1:
        return "No"

    time_units = {
        'year': 31536000,
        'day': 86400,
        'hour': 3600,
        'minute': 60,
        'second': 1
    }

    human_readable = []

    for unit, seconds_in_unit in time_units.items():
        calcd_time = seconds // seconds_in_unit

        if calcd_time == 0:
            continue

        human_readable.append(f"{calcd_time} {unit}{'s' if calcd_time != 1 else ''}")
        seconds = seconds % seconds_in_unit

    if len(human_readable) == 1:
        return human_readable[0]
    return ' and '.join([', '.join(human_readable[:-1]), human_readable[-1]])


if __name__ == '__main__':
    print(sec_2_human_readable(-50))
    print(sec_2_human_readable(0))
    print(sec_2_human_readable(60))
    print(sec_2_human_readable(62))
    print(sec_2_human_readable(3600))
    print(sec_2_human_readable(3602))
    print(sec_2_human_readable(3662))
    print(sec_2_human_readable(31536005))
    print(sec_2_human_readable(100000000))