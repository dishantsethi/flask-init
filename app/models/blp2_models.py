from app.extensions import db, ma

class Blp2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))

    def __repr__(self):
        return f'<BLP 2 "{self.id}">'

class Blp2Schema(ma.ModelSchema):
    class Meta:
        model = Blp2

blp2_schema = Blp2Schema()
