import json
import ast
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__, template_folder='templates')


@app.route('/')
def orders():
    conn = sqlite3.connect('coffee.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Purchase, Member WHERE Member.Email = Purchase.Buyer order by Purchase_time desc")
    rows = c.fetchall()
    conn.close()
    return render_template('showorder.html', rows=rows)


@app.route('/get_detail', methods=['POST'])
def get_value():
    value = request.form['value']
    conn = sqlite3.connect('coffee.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Purchase WHERE O_ID = ?', (value,))
    order_data = cursor.fetchone()

    cursor.execute(
        'SELECT Order_description.Item_ID, Name, Quantity, Quantity*Price FROM Order_description, Menu WHERE O_ID = ? AND Order_description.Item_ID = Menu.Item_ID Order by Order_description.Item_ID',
        (value,))
    purchase_data = cursor.fetchall()
    total_price = 0
    for i in purchase_data:
        total_price += i[3]

    member_mail = order_data[2]
    sql = "SELECT * FROM Member WHERE Email = ?"
    cursor.execute(sql, (member_mail,))
    member_data = cursor.fetchone()
    conn.close()
    return render_template('showorder_detail.html', order_data=order_data, purchase_data=purchase_data,
                           total_price=total_price, member_data=member_data)


@app.route('/customer_order')
def customer_order():
    conn = sqlite3.connect('coffee.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Menu order by Item_ID")
    rows = c.fetchall()
    conn.close()
    return render_template('customer_order.html', rows=rows)

@app.route('/submit_order', methods=['POST'])
def submit_order():
    selections = request.form.getlist('selections[]')
    item_quantities = {}
    for selection in selections:
        item_id, quantity = selection.split('-')
        if quantity != '0' :
            item_quantities[item_id] = int(quantity)
    rows = [{'item_id': key, 'quantity': value} for key, value in item_quantities.items()]
    total_price = 0

    # 計算價錢
    conn = sqlite3.connect('coffee.db')
    c = conn.cursor()
    c.execute("SELECT Name, Price FROM Menu")
    menu = c.fetchall()
    menu = dict(menu)
    for row in rows:
        row['price'] = menu[row['item_id']]
        total_price += menu[row['item_id']] * row['quantity']

    # 分店資訊
    c.execute("SELECT Name FROM Branch")
    branch_names = c.fetchall()
    conn.close()
    return render_template('order_check.html', rows=rows, total_price=total_price, branch_names=branch_names)


@app.route('/order_success', methods=['POST'])
def order_success():
    selected_branch = request.form.get('selected_branch')
    rows_str = request.form.get('rows')
    rows = ast.literal_eval(rows_str)


    conn = sqlite3.connect('coffee.db')
    c = conn.cursor()
    c.execute('SELECT Max(O_ID) FROM Purchase')
    max_O_ID = c.fetchone()
    max_O_ID = int(max_O_ID[0]) + 1
    purchase_time = datetime.now().strftime("%Y-%m-%d")

    c.execute("SELECT Name, Item_ID FROM Menu")
    menu = c.fetchall()
    menu = dict(menu)

    c.execute("INSERT INTO Purchase (O_ID, Purchase_time, Buyer, Branch) VALUES (?, ?, ?, ?)", (str(max_O_ID), purchase_time, 'doubleegg@gmail.com', selected_branch))

    for i in rows:
        c.execute("INSERT INTO Order_description (O_ID, Item_ID, Quantity) VALUES (?, ?, ?)", (max_O_ID, menu[i['item_id']], i['quantity']))
    conn.commit()
    c.close()
    return render_template('order_success.html', rows=rows, selected_branch=selected_branch)


if __name__ == '__main__':
    app.run(debug=True)
