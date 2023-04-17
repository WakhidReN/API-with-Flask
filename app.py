from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from datetime import *
import requests

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'car_rent'
mysql = MySQL(app)


def showData(cursor, msg):

    column_name = [i[0] for i in cursor.description]

    data = []
    for i in cursor.fetchall():
        data.append(dict(zip(column_name, i)))

    cursor.close()

    statuscode = 200
    messege = {
        "statuscode": statuscode,
        "messege": msg,
        "timestamp": datetime.now()
    }

    return jsonify(data, messege)


@app.route('/')
def root():
    return "Showroom Cars"


@app.route('/car', methods=['GET',])
def car():
    cursor = mysql.connection.cursor()

    if 'id' in request.args:
        id = request.args['id']

        cursor.execute(f"SELECT * FROM car WHERE car_id = {id}")

    elif 'name' in request.args:
        name = request.args['name']

        cursor.execute(f"SELECT * FROM car WHERE car_name LIKE \'%{name}%\'")

    elif 'maxprice' in request.args:
        price = request.args['maxprice']

        cursor.execute(f"SELECT * FROM car WHERE price <= {price}")

    elif 'transmision' in request.args:
        trans = request.args['transmision']

        cursor.execute(f"SELECT * FROM car WHERE transmision LIKE '%{trans}%'")

    else:
        cursor.execute(f"SELECT * FROM car")

    messege = "Data Fetched Successfully"

    return showData(cursor, messege)


@app.route('/customer', methods=['GET'])
def cust():
    cursor = mysql.connection.cursor()

    if 'id' in request.args:
        id = request.args['id']

        cursor.execute(f'SELECT * FROM customer WHERE cust_id = {id}')

    elif 'name' in request.args:
        name = request.args['name']

        cursor.execute(
            f"SELECT * FROM customer WHERE cust_name LIKE \'%{name}%\'")

    else:
        cursor.execute(f"SELECT * FROM customer")

    messege = "Data Fetched Successfully"

    return showData(cursor, messege)


@app.route('/rents', methods=['GET'])
def rents():

    cursor = mysql.connection.cursor()

    if 'id' in request.args:
        id = request.args['id']

        cursor.execute(f"SELECT rent.rent_id, customer.cust_name, car.car_name, rent.day, car.price*rent.day AS `total_price`, \
                        rent.start_date, DATE_ADD(rent.start_date, INTERVAL rent.day DAY) AS `end_date` FROM customer \
                        JOIN rent on rent.cust_id = customer.cust_id\
                        JOIN car on car.car_id = rent.car_id\
                        where rent.rent_id = {id}")

    elif 'custname' in request.args:
        custname = request.args['custname']

        cursor.execute(f"SELECT rent.rent_id, customer.cust_name, car.car_name, rent.day, car.price*rent.day AS `total_price`, \
                        rent.start_date, DATE_ADD(rent.start_date, INTERVAL rent.day DAY) AS `end_date` FROM customer \
                        JOIN rent on rent.cust_id = customer.cust_id\
                        JOIN car on car.car_id = rent.car_id\
                        where customer.cust_name LIKE \'%{custname}%\'")

    else:
        cursor.execute(f"SELECT rent.rent_id, customer.cust_name, car.car_name, rent.day, car.price*rent.day AS `total_price`, \
                        rent.start_date, DATE_ADD(rent.start_date, INTERVAL rent.day DAY) AS `end_date` FROM customer \
                        JOIN rent on rent.cust_id = customer.cust_id\
                        JOIN car on car.car_id = rent.car_id")

    messege = "Data Fetched Successfully"

    return showData(cursor, messege)


@app.route('/editcust', methods=['POST', 'PUT', 'DELETE'])
def editCustomer():
    cursor = mysql.connection.cursor()

    if request.method == 'POST':
        cust_name = request.json['cust_name']
        phone = request.json['phone']
        address = request.json['address']

        cursor.execute(f"INSERT INTO customer(cust_name, phone, address) VALUES\
                        ('{cust_name}', '{phone}', '{address}')")

        messege = "Customer Added Successfully"

    elif request.method == 'PUT':
        cust_id = request.args['id']
        cust_name = request.json['cust_name']
        phone = request.json['phone']
        address = request.json['address']

        cursor.execute(f"UPDATE customer SET \
                        cust_name = '{cust_name}', \
                        phone = '{phone}', \
                        address = '{address}' \
                        WHERE cust_id = {cust_id}")

        messege = "Customer Updated Successfully"

    elif request.method == 'DELETE':
        cust_id = request.args['id']
        cursor.execute(f"DELETE FROM customer WHERE cust_id = {cust_id}")

        messege = "Customer Deleted Successfully"

    mysql.connection.commit()

    messege = {
        "statuscode": 200,
        "message": messege
    }

    return messege


@app.route('/editcar', methods=['POST', 'PUT', 'DELETE'])
def editCar():
    cursor = mysql.connection.cursor()

    if request.method == 'POST':
        car_name = request.json['car_name']
        plat = request.json['plat']
        passanger = request.json['passanger']
        year = request.json['year']
        fuel = request.json['fuel']
        transmision = request.json['transmision']
        price = request.json['price']

        cursor.execute(f"INSERT INTO car(car_name, plat, passanger, year, fuel, transmision, price) VALUES\
                        ('{car_name}', '{plat}', {passanger}, {year}, '{fuel}', '{transmision}', {price})")

        messege = "Car Added Successfully"

    elif request.method == 'PUT':
        car_id = request.args['id']
        car_name = request.json['car_name']
        plat = request.json['plat']
        passanger = request.json['passanger']
        year = request.json['year']
        fuel = request.json['fuel']
        transmision = request.json['transmision']
        price = request.json['price']

        cursor.execute(f"UPDATE car SET \
                        car_name = '{car_name}', \
                        plat = '{plat}', \
                        passanger = {passanger}, \
                        year = {year}, \
                        fuel = '{fuel}', \
                        transmision = '{transmision}', \
                        price = {price} \
                        WHERE car_id = {car_id}")

        messege = "Car Updated Successfully"

    elif request.method == 'DELETE':
        car_id = request.args['id']

        cursor.execute(f"DELETE FROM car WHERE car_id = {car_id}")

        messege = "Car Deleted Successfully"

    mysql.connection.commit()

    messege = {
        "statuscode": 200,
        "message": messege
    }

    return messege


@app.route('/editrent', methods=['POST', 'PUT'])
def editRent():
    cursor = mysql.connection.cursor()

    if request.method == 'POST':
        cust_id = request.json['cust_id']
        car_id = request.json['car_id']
        day = request.json['day']
        start_date = request.json['start_date']

        cursor.execute(f"INSERT INTO rent(cust_id, car_id, day, start_date) VALUES\
                        ('{cust_id}', '{car_id}', {day}, '{start_date}')")

        messege = "Rent Record Added Successfully"

    elif request.method == 'PUT':
        rent_id = request.args['id']
        cust_id = request.json['cust_id']
        car_id = request.json['car_id']
        day = request.json['day']
        start_date = request.json['start_date']

        cursor.execute(f"UPDATE rent SET \
                        cust_id = '{cust_id}', \
                        car_id = '{car_id}', \
                        day = {day}, \
                        start_date = '{start_date}'\
                        WHERE rent_id={rent_id}")

        messege = "Rent Record Updated Successfully"

    mysql.connection.commit()

    messege = {
        "statuscode": 200,
        "message": messege
    }

    return messege


if __name__ == '__main__':
    app.run(host='localhost', port=50, debug=True)
