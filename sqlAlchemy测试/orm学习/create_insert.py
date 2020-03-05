from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://postgres:20001003@localhost:5432/test', echo = True)
Base = declarative_base()
Session = sessionmaker(bind = engine) #hasn't opened any connections yet
#ervery time to creat a new session
#usage:
#new_session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    password = Column(String, primary_key = True)


    def fun(self, id):  #可以直接初始化赋值，然后使用session添加到数据库中，如果已经存在，则查询会出错！
        self.id = id
        print(id)

    def __repr__(self): #内置函数，类似于c++中的<<的重载
        return "<User(name='%s', password='%s')>" % ( self.name, self.password)


my_user = User(id = 1, name = 'before', password = '111')
#print(my_user)

session = Session() #新建一个session 注意这里还没有commit
#session.add(my_user)    #此时提交至session的一个buffer（pending）中并没有上传到数据库
                        #如果在数据库中查询是查不到的
q = session.query(User).filter_by(name='before').first()
#print(q)

my_user.name = 'after' #在session修改属性，session已经追踪了


q = session.query(User).filter_by(name='after').first()#在缓冲区中仅有after了
#print(q)

#在commit前，如果要清楚buffer（pending）中的操作，可以使用rollback()

#session.commit()    #session的生命周期结束
