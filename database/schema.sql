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
    Price REAL NOT NULL,
    class VARCHAR
);

-- 建立 Branch 表格
DROP TABLE IF EXISTS Branch;
CREATE TABLE Branch (
    Name VARCHAR PRIMARY KEY,
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
    Cost_per_unit REAL NOT NULL,
    Remain_num INTEGER NOT NULL,
    Producer VARCHAR,
    FOREIGN KEY (Producer) REFERENCES Producer(P_ID)
);


-- 建立 Purchase 表格
DROP TABLE IF EXISTS Purchase;
CREATE TABLE Purchase (
    O_ID VARCHAR PRIMARY KEY,
    Purchase_time DATE NOT NULL,
    Buyer VARCHAR NOT NULL,
    Branch VARCHAR NOT NULL,
    FOREIGN KEY (Buyer) REFERENCES Member(Email),
    FOREIGN KEY (Branch) REFERENCES Branch(Name)
);

-- 建立 Order_description 表格
DROP TABLE IF EXISTS Order_description;
CREATE TABLE Order_description (
    O_ID VARCHAR,
    Item_ID VARCHAR,
    Quantity INTEGER NOT NULL,
    PRIMARY KEY (O_ID, Item_ID),
    FOREIGN KEY (O_ID) REFERENCES Purchase(O_ID),
    FOREIGN KEY (Item_ID) REFERENCES Menu(Item_ID) ON DELETE CASCADE ON UPDATE CASCADE 
);

-- 建立 Ma_Purchase 表格
DROP TABLE IF EXISTS Ma_Purchase;
CREATE TABLE Ma_Purchase (
    MaP_ID VARCHAR PRIMARY KEY,
    Ma_Purchase_time DATE NOT NULL,
    Buyer VARCHAR NOT NULL,
    Supply VARCHAR NOT NULL,
    FOREIGN KEY (Buyer) REFERENCES Branch(Name),
    FOREIGN KEY (Supply) REFERENCES Producer(P_ID)
);

-- 建立 Ma_Purchase_description 表格
DROP TABLE IF EXISTS Ma_Purchase_description;
CREATE TABLE Ma_Purchase_description (
    MaP_ID VARCHAR,
    Ma_ID VARCHAR,
    Quantity INTEGER NOT NULL,
    PRIMARY KEY (MaP_ID, Ma_ID),
    FOREIGN KEY (MaP_ID) REFERENCES Ma_Purchase(MaP_ID),
    FOREIGN KEY (Ma_ID) REFERENCES Material(Ma_ID) ON DELETE CASCADE ON UPDATE CASCADE 
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
