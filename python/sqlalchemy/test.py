from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# if echo log, echo=True
engine = create_engine('sqlite:///sample_db.sqlite3', echo=True)

# まずベースモデルを生成します
Base = declarative_base()

# 次にベースモデルを継承してモデルクラスを定義します
class Student(Base):
    """
    生徒モデル
    必ず Base を継承
    """
    __tablename__ = 'students'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    score = Column(Integer)  # 点数
 
    def __repr__(self):
        return "<Student(id='%s', name='%s', score='%s')>" % (self.id, self.name, self.score)
 
 
# テーブルの作成
# テーブルがない場合 CREATE TABLE 文が実行される
Base.metadata.create_all(engine)



Session = sessionmaker(bind=engine)
session = Session()

# add
session.add(Student(id=1, name='Suzuki', score=70))

result = session.query(Student).all()  # .all() は省略可
for student in result:
    print(student.name, student.score)
