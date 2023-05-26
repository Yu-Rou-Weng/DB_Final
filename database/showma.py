from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__, template_folder='templates')


@app.route('/')
def menu():
    conn = sqlite3.connect('coffee.db')
    c = conn.cursor()
    c.execute("SELECT Material.Name,Cost,Cost_per_unit,Remain_num,Producer.Name FROM Material, Producer WHERE P_ID=Producer")
    MaRemain = c.fetchall()
    conn.close()
    return render_template('showma.html', MaRemain=MaRemain)



if __name__ == '__main__':
    app.run(debug=True)