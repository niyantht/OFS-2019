import MySQLdb

connection = MySQLdb.connect (host = "iotplatform.c66jtrv2jovs.us-east-1.rds.amazonaws.com",
                              user = "iotplatformusr",
                              passwd = "iotplatformpwd",
                              db = "temperature_data_logger")

cursor = connection.cursor()


def selectTable (columns, tablename):
    cursor0bj.execute(
        "select" + columns + " from " + tablename
    )
    records = cursor0bj.fetchall()

#print(records)


#find the min value
def my_min_function(list):
    min_value = None
    for value in list:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value


