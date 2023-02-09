from app.extensions import db, ma

class Blp1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))

    def __repr__(self):
        return f'<BLP 1 "{self.id}">'

class Blp1Schema(ma.ModelSchema):
    class Meta:
        model = Blp1

blp1_schema = Blp1Schema()