def read_weather_data(r):
    '''Read weather data from reader r in fixed-width format. The field widths are:
        4,2,2    YYYYMMDD    (date)
        2,2,2    DDMMSS      (latitude 纬度)
        2,2,2    DDMMSS      (longitude 经度)
        6,6,6    FF.FFF      (temp temperature温度, deg degree度数, C; humidity湿度, %; pressure压力, kPa)
        The result is a list of values (not tuples) '''

    fields = ((4,int) , (2,int) , (2,int),
              (2,int) , (2,int) , (2,int) ,
              (2,int) , (2,int) , (2,int) ,
              (6,float) , (6,float) , (6,float))
    result = []
    # For each record
    for line in r:
        start = 0
        record = []
        for (width , target_type) in fields:
            # convert the text
            text = line[start:start + width]
            field = target_type(text)
            # add it to the recorc
            record.append(field)
            # move on
            start += width
        # add the completed record to the result
        result.append(record)
    return result
