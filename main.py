from Blog.views import app
from Blog.models import db

db.create_all()
app.run()