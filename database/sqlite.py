import sqlite3

connection = sqlite3.connect('coffee.db')

with open('schema.sql',encoding='utf-8') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO Branch (Name, Address, Tel) VALUES (?, ?, ?)", ('Taipei', 'No.11 Xinglong Road.', '022387657'))
cur.execute("INSERT INTO Branch (Name, Address, Tel) VALUES (?, ?, ?)", ('Kaohsiung', 'No.22 Zhongzheng Road.', '072638148'))
cur.execute("INSERT INTO Branch (Name, Address, Tel) VALUES (?, ?, ?)", ('Tainan', 'No. 123 Mingzu Road.', '062353657'))
cur.execute("INSERT INTO Branch (Name, Address, Tel) VALUES (?, ?, ?)", ('Taoyuan', 'No. 56 Chunghua Road.', '038467657'))
cur.execute("INSERT INTO Branch (Name, Address, Tel) VALUES (?, ?, ?)", ('Taichung', 'No. 131 Keelong Road.', '042387234'))
cur.execute("INSERT INTO  Branch (Name, Address, Tel) VALUES (?, ?, ?)",
            ('鹿港店','彰化縣鹿港鎮','0988375864'))
cur.execute("INSERT INTO  Branch (Name, Address, Tel) VALUES (?, ?, ?)",
            ('文山店','台北縣文山區','0988324521'))

cur.execute("INSERT INTO Producer (P_ID, Name) VALUES (?, ?)", ('101','Emart'))
cur.execute("INSERT INTO Producer (P_ID, Name) VALUES (?, ?)", ('102','Costco'))
cur.execute("INSERT INTO Producer (P_ID, Name) VALUES (?, ?)", ('103','PX'))
cur.execute("INSERT INTO Producer (P_ID, Name) VALUES (?, ?)", ('104','7-11'))
cur.execute("INSERT INTO Producer (P_ID, Name) VALUES (?, ?)", ('105','Family'))

#Menu
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('101', 'Coffee', 95))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('102', 'Espresso', 80))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('103', 'Caffe Latte', 135))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('104', 'Cappuccino', 135))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('105', 'Caramel Macchiato', 155))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('106', 'Cocoa Macchiato', 155))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('107', 'Cold Brew Coffee', 140))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('201', 'Matcha Latte', 150))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('202', 'Earl Grey Tea Latte', 145))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('203', 'Black Tea Latte', 145))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('204', 'Rose Fancy Tea Latte', 145))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('205', 'Hot Chocolate', 150))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('206', 'Mango Juice', 135))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('301', 'Blueberry Chocolate Cake', 145))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('302', 'Citrus Fruit Cake', 130))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('303', 'Sponge Cheese Cake', 80))
cur.execute("INSERT INTO Menu (Item_ID, Name, Price) VALUES (?, ?, ?)", ('304', 'Black Forest Cake', 120))

#Material
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('101', 'coffee beans', 1200, 0, '104')) #KG
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('102', 'milk', 200, 0, '102')) #2L
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('103', 'caramel syrup', 250, 0, '103')) #250ml
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('104', 'chocolate sauce', 250, 0, '103')) #250ml
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('105', 'matcha', 2500, 0, '103')) #500g
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('106', 'earl gray tea', 1200, 0, '105')) #400g
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('107', 'rose tea', 1200, 0, '105')) #400g
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('108', 'black tea', 1200, 0, '105')) #400g
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('109', 'mango juice', 350, 0, '101')) #1L
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('110', 'ice', 120, 0, '101')) #10L
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('201', 'Blueberry Chocolate Cake', 700, 0, '101')) #12pieces
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('202', 'Citrus Fruit Cake', 500, 0, '104')) #12pieces
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('203', 'Sponge Cheese Cake', 300, 0, '105')) #12pieces
cur.execute("INSERT INTO Material (Ma_ID, Name, Cost, Remain_num, Producer) VALUES (?, ?, ?, ?, ?)", ('204', 'Black Forest Cake', 500, 0, '103')) #12pieces

#Recipe
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('101','101'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('102','101'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('103','101'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('103','102'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('104','101'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('104','102'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('105','101'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('105','102'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('105','103'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('106','101'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('106','102'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('106','104'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('107','101'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('201','102'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('201','105'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('202','102'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('202','106'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('203','102'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('203','108'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('204','102'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('204','107'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('205','104'))
cur.execute("INSERT INTO Recipe (Item_ID, Ma_ID) VALUES (?, ?)", ('206','109'))

#Member
cur.execute("INSERT INTO Member (Email,Name,Password,Tel) VALUES (?, ?, ?,?)",
            ('a@gmail.com','小小','123', '0988384859'))
cur.execute("INSERT INTO Member (Email,Name,Password,Tel) VALUES (?, ?, ?,?)",
            ('ab@gmail.com','大大','13', '0988239405'))

#Purchase
cur.execute("INSERT INTO Purchase (Purchase_Time, Buyer, Branch) VALUES (?, ?, ?)",
            ('2022-01-02', 'a@gmail.com', '6'))
cur.execute("INSERT INTO Purchase (Purchase_Time, Buyer, Branch) VALUES (?, ?, ?)",
            ('2022-01-01', 'a@gmail.com', '6'))
cur.execute("INSERT INTO Purchase (Purchase_Time, Buyer, Branch) VALUES (?, ?, ?)",
            ('2022-01-01', 'ab@gmail.com', '7'))

#Order_description
cur.execute("INSERT INTO Order_description (O_ID, Item_ID) VALUES (?, ?)",
            ('1','101'))
cur.execute("INSERT INTO Order_description (O_ID, Item_ID) VALUES (?, ?)",
            ('1','102'))
cur.execute("INSERT INTO Order_description (O_ID, Item_ID) VALUES (?, ?)",
            ('3','101'))
cur.execute("INSERT INTO Order_description (O_ID, Item_ID) VALUES (?, ?)",
            ('3','105'))
cur.execute("INSERT INTO Order_description (O_ID, Item_ID) VALUES (?, ?)",
            ('2','101'))
cur.execute("INSERT INTO Order_description (O_ID, Item_ID) VALUES (?, ?)",
            ('2','103'))
cur.execute("INSERT INTO Order_description (O_ID, Item_ID) VALUES (?, ?)",
            ('3','103'))
cur.execute("INSERT INTO Order_description (O_ID, Item_ID) VALUES (?, ?)",
            ('1','103'))

connection.commit()
connection.close()