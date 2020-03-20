import create_insert
from create_insert import Session, User
#引入create_insert中的引擎和实例定义

print("DEBUG::in query.py")

session = Session()
#session.query(表名).order_by(属性名)

#session.query(可以接受通过Base方法建立关联的类)
#   eg. session.query(User.name)   选择出User类关联的表的name属性的全部元组

#lable方法：类似于as，将某一属性名更改
#   eg. session.query(User.name.label('name_label")).all()

#aliased方法：在orm中引入aliased，可以直接使用：
#   化名 = aliased(表名， 原表属性名='化名')

#filter方法:filter(属性名 = ‘属性’) 类似于sql中的where

#ilike方法:query.filter(User.name.ilike('%ed%')) 类似于sql中的匹配

#and_方法 # use and_()
#使用and_()
    #query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
#直接在filter中使用多个参数限定
    #query.filter(User.name == 'ed', User.fullname == 'Ed Jones')
#链式使用filter
    #query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')

##
#query返回的类型：
#
#all()返回一个list
#first()返回第一个元素
#one()仅仅有一个时候正确返回，否则错误

##
#func.count()计数
#
