from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from create_insert import Session, User, Base, Column, Integer, String, engine

print("DEBUG::in Relationship.py")

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    #两个关系表互相建立指向关系
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
       return "<Address(email_address='%s')>" % self.email_address


#User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

jack = User(id = 122, name = 'jack', password = '111')
print(jack.addresses)

#一旦建立获得了一个User的对象，我们可以直接通关关系来为另外一个表赋值
