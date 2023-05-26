from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__, template_folder='templates')


@app.route('/')
def orders():
    conn = sqlite3.connect('coffee.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Purchase order by Purchase_time desc")
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

    cursor.execute('SELECT Order_description.Item_ID, Name, Quantity, Quantity*Price FROM Order_description, Menu WHERE O_ID = ? AND Order_description.Item_ID = Menu.Item_ID Order by Order_description.Item_ID', (value,))
    purchase_data = cursor.fetchall()
    total_price = 0
    for i in purchase_data:
        total_price += i[3]

    member_mail = order_data[2]
    sql = "SELECT * FROM Member WHERE Email = ?"
    cursor.execute(sql, (member_mail,))
    member_data = cursor.fetchone()
    return render_template('showorder_detail.html', order_data=order_data, purchase_data=purchase_data, total_price=total_price, member_data=member_data)


if __name__ == '__main__':
    app.run(debug=True)
