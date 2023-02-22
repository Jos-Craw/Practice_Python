from sqlalchemy import Column, Date, Integer,Text,Date
from sqlalchemy.ext.declarative import declarative_base


Base  = declarative_base()


class Post(Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True)
	rubrics = Column(Text, nullable=False)
	text = Column(Text, nullable=False)
	created_date = Column(Date, nullable=False)