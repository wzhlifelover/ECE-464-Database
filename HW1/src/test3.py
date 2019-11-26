from sqlalchemy import Column, String, Integer, Date, MetaData, Table, ForeignKey, create_engine
from base import Base, engine

metadata = MetaData()

reserves = Table('reserves', metadata,
        Column('sid', Integer, primary_key=True),
        Column('bid', Integer, primary_key=True),
        Column('day', Date, primary_key=True),
        Column('earning',Integer, primary_key=True))

sailors = Table('sailors', metadata,
        Column('sid', Integer, primary_key=True),
        Column('sname', String(30)),
        Column('rating', Integer),
        Column('age', Integer),
        Column('salary', Integer))

boats = Table('boats', metadata,
        Column('bid', Integer, primary_key=True),
        Column('bname', String(20)),
        Column('color', String(10)))

work_record = Table('work_record', metadata,
             Column('day', Date, primary_key=True),
             Column('sid', Integer, primary_key=True),
             Column('hours', Integer))

metadata.drop_all(engine)
metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sailors.insert(), [
    {'sid': 22, 'sname': 'abc', 'rating': '7', 'age': 18, 'salary': 11},
    {'sid': 23, 'sname': 'def', 'rating': '8', 'age': 18, 'salary': 12},
    {'sid': 32, 'sname': 'ghi', 'rating': '9', 'age': 18, 'salary': 13},
    {'sid': 34, 'sname': 'jkl', 'rating': '10', 'age': 18, 'salary': 14},
    {'sid': 56, 'sname': 'mnq', 'rating': '11', 'age': 18, 'salary': 15},
    ])

    conn.execute(reserves.insert(), [
    {'sid': 22, 'bid': 22, 'day': '2019/10/10', 'earning': 100},
    {'sid': 23, 'bid': 23, 'day': '2019/10/12', 'earning': 180},
    {'sid': 32, 'bid': 32, 'day': '2019/10/15', 'earning': 220},
    {'sid': 34, 'bid': 33, 'day': '2019/10/18', 'earning': 150},
    {'sid': 56, 'bid': 44, 'day': '2019/10/20', 'earning': 170}
    ])

    conn.execute(work_record.insert(), [
    {'day': '2019/10/10', 'sid': 22, 'hours': 3},
    {'day': '2019/10/12', 'sid': 23, 'hours': 7},
    {'day': '2019/10/15', 'sid': 32, 'hours': 13},
    {'day': '2019/10/18', 'sid': 34, 'hours': 5},
    {'day': '2019/10/20', 'sid': 56, 'hours': 8}
    ])
