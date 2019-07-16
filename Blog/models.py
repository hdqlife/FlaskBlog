from Blog import db

class Author(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32))
    age=db.Column(db.String(32))
    gender=db.String(db.String(32))
    email=db.Column(db.String(32))
    photo=db.Column(db.String(32))
    article=db.relationship("Article",backref="author")

registration=db.Table(
    "registrations",
    db.Column("type_id",db.Integer,db.ForeignKey("type.id")),#type表的id
    db.Column("article_id",db.Integer,db.ForeignKey("article.id"))#article表的id
)#多对多的关系

class Article(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(32))
    description=db.Column(db.Text)
    content=db.Column(db.Text)
    time=db.Column(db.Date)
    click=db.Column(db.Integer,default=0)
    recommend=db.Column(db.Integer) #1推荐，0不推荐
    picture=db.Column(db.String(32))

    author=db.Column(db.String(32),db.ForeignKey("author.id"))
    types=db.relationship(
        "Type",#外键对那个表
        secondary=registration,#关系表是哪个
        backref=db.backref("article",lazy="dynamic"),#关系维持
        lazy="dynamic" #删除关系
    )
    comment=db.relationship("Comment",backref="article")
class Type(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    lable=db.Column(db.String(32))
    description=db.Column(db.Text)
    article=db.relationship("Article",backref="type")

class Comment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    comtent=db.Column(db.Text)
    time=db.Column(db.DateTime)
    persion=db.Column(db.String(32))
    article=db.Column(db.Integer,db.ForeignKey("article.id"))