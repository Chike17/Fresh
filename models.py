import datetime
from peewee import *

DATABASE = SqliteDatabase('fresh.db')

class User(Model):
  user_name = CharField()
  email = CharField()
  # pw = CharField()
  
  class Meta:
    database = DATABASE
    
class Barber(Model):
  name = CharField()
  neighborhood = CharField()
  profile_pic = CharField()
  portfolio_pic = CharField()

  class Meta:
    database = DATABASE

class Review(Model):
  timestamp = DateTimeField(default=datetime.datetime.now)
  barber = ForeignKeyField(Barber, backref='barber')
  user = ForeignKeyField(User, backref='user')
  text = TextField()
  rating = CharField()

  class Meta:
    database = DATABASE
    order_by = ('-timestamp',)

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Review], safe=True)
  DATABASE.close()






# class Review(db.Model):
#   __table_args__ = {'extend_existing': True} 

#   id = db.Column(db.Integer, primary_key=True)
#   barber = db.Column(db.String, db.ForeignKey("barber.id"))
#   user = db.Column(db.String, db.ForeignKey("user.id"))
#   text = db.Column(db.String(300))
#   rating = db.Column(db.Integer)

# ######################################################
# ################### Initiate Model ###################
# ######################################################

# def __init__(self, barber, user, text, rating):
#     self.barber = barber
#     self.user = user
#     self.text = text
#     self.rating = rating

# ##########################################################
# ################### Review Model Methods ###################
# ##########################################################

# #CREATE A Review 
#     @classmethod
#     def create_review(cls, user, barber, text, rating):
#         new_review = Review(user, barber, text, rating)  #
#         try:                                        # Try & Except  is like a success & error or then catch. If I get a exception/error my except needs to handle that error for me.
#             db.session.add(new_review)                #create a sessions using sqlAlchemy --> Then place the values into the database
#             db.session.commit()                     #saves the data to the database
#         except:
#             db.session.rollback()                   #rollback simply closes a opened session if there are exceptions/errors
#             raise Exception('Session rollback')
#         return review_schema.jsonify(new_review)        #once we are done creating the Review scheme convert it into a json and return it to app.py
# ######################## End of CREATE Review Method

# class ReviewSchema(marshmallow.Schema):
#   class Meta:
#     fields = ('id', 'barber', 'user', 'text', 'rating')

# review_schema = ReviewSchema(strict=True)
# reviews_schema = ReviewSchema(many=True, strict=True)

# if __name__ == 'models':
#   db.create_all()