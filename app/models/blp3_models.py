from app.extensions import db, ma

class Blp3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))

    def __repr__(self):
        return f'<BLP 3 "{self.id}">'

class Blp3Schema(ma.ModelSchema):
    class Meta:
        model = Blp3

blp3_schema = Blp3Schema()
