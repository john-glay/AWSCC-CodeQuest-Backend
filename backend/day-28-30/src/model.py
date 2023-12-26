from . import db

class PasswordEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<PasswordEntry {self.website}: {self.email} - {self.password}>'
