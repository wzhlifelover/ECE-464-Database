import pytest
from sqlalchemy import Column, String, Integer, Date, MetaData, ForeignKey, desc, func
from base import Base, engine, Session

metadata = MetaData()

#Create ORM
class Boats(Base):
    __tablename__ = 'boats'

    bid = Column(Integer, primary_key=True)
    bname = Column(String)
    color = Column(String)
    length = Column(Integer)

class Sailors(Base):
    __tablename__ = 'sailors'

    sid = Column(Integer, primary_key=True)
    sname = Column(String)
    rating = Column(Integer)
    age = Column(Integer)

class Reserves(Base):
    __tablename__ = 'reserves'

    sid = Column(Integer, ForeignKey('sailors.sid'), primary_key=True)
    bid = Column(Integer, ForeignKey('boats.bid'), primary_key=True)
    day = Column(Date, primary_key=True)

#Tests
def custom_assert(raw_query, api_query):
    #Create a list from connect().execute() to compare with Query objects
    raw_list = []
    api_list = []
    with engine.connect() as conn:
        result = conn.execute(raw_query)
        for x in result:
            raw_list.append(x)
    print(raw_list)
    for x in api_query:
        api_list.append(x)
    print(api_list)
    assert raw_list == api_list

session = Session()


def test_query2():
    api_q2 = session.query(Boats.bid, Boats.bname, func.count('*')).filter(Reserves.bid == Boats.bid).group_by(Reserves.bid)
    raw_q2 = "SELECT b.bid, b.bname, COUNT(*) FROM reserves AS r, boats AS b WHERE r.bid = b.bid GROUP BY r.bid;"
    custom_assert(raw_q2, api_q2)


def test_query6():
    query1 = session.query(Boats.bid).filter(Boats.color == "red")
    query2 = session.query(Reserves.sid).filter(Reserves.bid.in_(query1))
    query3 = session.query(Sailors.sname).filter(Sailors.sid.notin_(query2))
    raw_q6 = "SELECT s.sid, s.sname FROM sailors AS s WHERE s.sid NOT IN (SELECT r.sid FROM reserves AS r JOIN boats AS b ON r.bid = b.bid WHERE b.color = 'red');"
    custom_assert (raw_q6, query3)


def test_query7():
    query_7 = session.query(func.avg(Sailors.age)).filter(Sailors.rating == 10).all()
    raw_q7 = "SELECT AVG(s.age) FROM sailors AS s WHERE s.rating=10;"
    custom_assert (raw_q7,query_7)


if  __name__ == "__main__":
    test_query2()
    #test_query6()
    #test_query7()
    session.commit()
    session.close()