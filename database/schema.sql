PRAGMA foreign_keys = true;

-- 建立 Member 表格
DROP TABLE IF EXISTS Member;
CREATE TABLE Member (
    Email VARCHAR PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Password VARCHAR NOT NULL,
    Tel VARCHAR
);

-- 建立 Menu 表格
DROP TABLE IF EXISTS Menu;
CREATE TABLE Menu (
    Item_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR NOT NULL,
    Price REAL NOT NULL
);

-- 建立 Branch 表格
DROP TABLE IF EXISTS Branch;
CREATE TABLE Branch (
    B_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR,
    Address VARCHAR,
    Tel VARCHAR 
);

-- 建立 Producer 表格
DROP TABLE IF EXISTS Producer;
CREATE TABLE Producer (
    P_ID VARCHAR PRIMARY KEY,
    Name VARCHAR
);

-- 建立 Material 表格
DROP TABLE IF EXISTS Material;
CREATE TABLE Material (
    Ma_ID VARCHAR PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Cost REAL NOT NULL,
    Remain_num INTEGER NOT NULL,
    Producer VARCHAR,
    FOREIGN KEY (Producer) REFERENCES Producer(P_ID)
);


-- 建立 Purchase 表格
DROP TABLE IF EXISTS Purchase;
CREATE TABLE Purchase (
    O_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Purchase_Time DATE NOT NULL,
    Buyer VARCHAR NOT NULL,
    Branch VARCHAR NOT NULL,
    FOREIGN KEY (Buyer) REFERENCES Member(Email),
    FOREIGN KEY (Branch) REFERENCES Branch(B_ID)
);

-- 建立 Order_description 表格
DROP TABLE IF EXISTS Order_description;
CREATE TABLE Order_description (
    O_ID VARCHAR,
    Item_ID VARCHAR,
    PRIMARY KEY (O_ID, Item_ID),
    FOREIGN KEY (O_ID) REFERENCES Purchase(O_ID),
    FOREIGN KEY (Item_ID) REFERENCES Menu(Item_ID) ON DELETE CASCADE ON UPDATE CASCADE 
);

-- 建立 Employee 表格
DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (
    E_ID VARCHAR PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Password VARCHAR NOT NULL,
    Tel VARCHAR,
    Branch VARCHAR NOT NULL,
    FOREIGN KEY (Branch) REFERENCES Branch(Name)
);

-- 建立 Recipe 表格
DROP TABLE IF EXISTS Recipe;
CREATE TABLE Recipe (
    Item_ID VARCHAR,
    Ma_ID VARCHAR,
    PRIMARY KEY (Item_ID, Ma_ID),
    FOREIGN KEY (Item_ID) REFERENCES Menu(Item_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Ma_ID) REFERENCES Material(Ma_ID)
);
