from sqlalchemy import Column, String, Integer, Date, MetaData, Table, ForeignKey, create_engine
from base import Base, engine
from sqlalchemy.orm import sessionmaker

metadata = MetaData()

reserve = Table('reserves', metadata,
        Column('sid', Integer, primary_key=True),
        Column('bid', Integer, primary_key=True),
        Column('day', Date, primary_key=True),
        Column('earning',Integer))

sailors = Table('sailors', metadata,
        Column('sid', Integer, primary_key=True),
        Column('sname', String(30)),
        Column('rating', Integer),
        Column('age', Integer),
        Column('salary', Integer))

boats = Table('boats', metadata,
        Column('bid', Integer, primary_key=True),
        Column('bname', String(20)),
        Column('color', String(10)),
        Column('length', Integer))

work_record = Table('work_record', metadata,
             Column('day', Date, primary_key=True),
             Column('sid', Integer,ForeignKey('sailors.sid'),primary_key=True),
             Column('hours', Integer))

cost_record = Table('cost_record', metadata,
             Column('cid', Integer, primary_key=True),
             Column('bid', Integer, ForeignKey('boats.bid')),
             Column('sid', Integer, ForeignKey('sailors.sid')),
             Column('cost', Integer),
             Column('day', Date))

# ORM representation here but for easiness of insertion I just use the Table way
# class Employees(Base):
#     __tablename__ = 'employees'
#
#     Column('eid', Integer, primary_key=True)
#     Column('ename', String(20))
#     Column('salary', Integer)
#
# class Hours(Base):
#     __tablename__ = 'hours'
#
#     Column('day', Date, primary_key=True)
#     Column('employees_eid', Integer, ForeignKey('employees.eid'), primary_key=True)
#     Column('hours', Integer)

if __name__ == '__main__':
    #clear and create the schema
    metadata.drop_all(engine)
    metadata.create_all(engine)
    #insert with raw SQL lines
   # with engine.connect() as conn:
    #    with open('../input2.txt', 'r') as lines:
     #       for line in lines:
      #          line = line.strip('\n')
       #         conn.execute(line)
    

    """ Another way to import instead of using raw SQL lines """
    with engine.connect() as conn:
        conn.execute(work_record.insert(), [
            {'day': '1998/10/10', 'sid': 22, 'hours': 5},
            {'day': '1998/10/10', 'sid': 22, 'hours': 3},
            {'day': '1998/10/10', 'sid': 22, 'hours': 8},
            {'day': '1998/10/10', 'sid': 22, 'hours': 6}
        ])
        conn.execute(cost_record.insert(), [
            {'cid': 1, 'boat_id': 101, 'sid': 22, 'cost': 50, 'day': '1998/10/10'},
            {'cid': 2, 'boat_id': 102, 'sid': 22, 'cost': 50, 'day': '1998/10/10'},
            {'cid': 3, 'boat_id': 103, 'sid': 22, 'cost': 80, 'day': '1998/10/10'},
            {'cid': 4, 'boat_id': 104, 'sid': 22, 'cost': 100, 'day': '1998/10/10'},
            {'cid': 5, 'boat_id': 102, 'sid': 22, 'cost': 100, 'day': '1998/10/10'}
        ])
