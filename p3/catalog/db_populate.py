#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbset import Base, User, Country, City

engine = create_engine('sqlite:///data.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(name='Rahul Passi', email='rahulpassi2412@gmail.com')
session.add(user1)
session.commit()

country1 = Country(name='U.S.A', user=user1)
session.add(country1)
session.commit()
city1 = City(name='New york city', state='New york',
             description="New York is an important center for inter \
national diplomacy and has been described as the cultural, \
financial and media capital of the world."
, country=country1, user=user1)
session.add(city1)
session.commit()

city2 = City(name='Chicago', state='Illinois',
             description="Positioned along Lake Michigan, the city is an \
international hub for finance, commerce, industry, \
technology,telecommunications, and transportation."
, country=country1, user=user1)
session.add(city2)
session.commit()

city3 = City(name='Las vegas', state='Nevada',
             description="The city famous for its mega casinos,bills\
itself as The Entertainment Capital of the World."
, country=country1, user=user1)
session.add(city3)
session.commit()

country2 = Country(name='Spain', user=user1)
session.add(country2)
session.commit()
city21 = City(name='Barcelona', state='Catalonia',
              description="It is the largest metropolis on the Mediterranean\
Sea, located on the coast between the mouths of the rivers\
Llobregat and Besos."
, country=country2, user=user1)
session.add(city21)
session.commit()

city22 = City(name='Madrid', state='Madrid',
              description="It is the third-largest city in the European \
Union (EU) after London and Berlin."
, country=country2, user=user1)
session.add(city22)
session.commit()

country3 = Country(name='Germany', user=user1)
session.add(country3)
session.commit()
city31 = City(name='Munich', state='Bavaria',
              description="Munich is the third largest city in Germany, \
after Berlin and Hamburg."
, country=country3, user=user1)
session.add(city31)
session.commit()

city32 = City(name='Dortmund', state='North Rhine-Westphalia',
              description="Dortmund is the largest city by area and \
population in the Ruhr Area, an urban area with some \
5.1 million (2011) inhabitants."
, country=country3, user=user1)
session.add(city32)
session.commit()
  		
