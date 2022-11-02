from flask_sqlalchemy import SQLAlchemy

mariadb = SQLAlchemy()

class Login(mariadb.Model):
    username = mariadb.Column(mariadb.String, primary_key=True, nullable=False)
    password = mariadb.Column(mariadb.String, nullable=False)

fakulta_has_clovek = mariadb.Table('fakulta_has_clovek',
    mariadb.Column('fakulta_id', mariadb.Integer, mariadb.ForeignKey('fakulta.id'), primary_key=True),
    mariadb.Column('clovek_id', mariadb.Integer, mariadb.ForeignKey('clovek.id'), primary_key=True),
    info={'bind_key': 'mariadbUjep'})

clovek_has_titul = mariadb.Table('clovek_has_titul',
    mariadb.Column('clovek_id', mariadb.Integer, mariadb.ForeignKey('clovek.id'), primary_key=True),
    mariadb.Column('titul_id', mariadb.Integer, mariadb.ForeignKey('titul.id'), primary_key=True),
    info={'bind_key': 'mariadbUjep'})

clovek_has_pozice = mariadb.Table('clovek_has_pozice',
    mariadb.Column('clovek_id', mariadb.Integer, mariadb.ForeignKey('clovek.id'), primary_key=True),
    mariadb.Column('pozice_id', mariadb.Integer, mariadb.ForeignKey('pozice.id'), primary_key=True),
    info={'bind_key': 'mariadbUjep'})

class Univerzita(mariadb.Model):
    __bind_key__ = 'mariadbUjep'
    __tablename__ = 'univerzita'
    id = mariadb.Column(mariadb.Integer, primary_key=True)
    nazev = mariadb.Column(mariadb.String)

class Fakulta(mariadb.Model):
    __bind_key__ = 'mariadbUjep'
    __tablename__ = 'fakulta'
    id = mariadb.Column(mariadb.Integer, primary_key=True)
    nazev = mariadb.Column(mariadb.String)
    univerzita_id = mariadb.Column(mariadb.Integer, mariadb.ForeignKey('univerzita.id'))
    fakulty = mariadb.relationship('Clovek', secondary=fakulta_has_clovek)

class Clovek(mariadb.Model):
    __bind_key__ = 'mariadbUjep'
    __tablename__ = 'clovek'
    id = mariadb.Column(mariadb.Integer, primary_key=True)
    jmeno = mariadb.Column(mariadb.String)
    prijmeni = mariadb.Column(mariadb.String)
    tituly = mariadb.relationship('Titul', secondary=clovek_has_titul)
    pozice = mariadb.relationship('Pozice', secondary=clovek_has_pozice)

class Pozice(mariadb.Model):
    __bind_key__ = 'mariadbUjep'
    __tablename__ = 'pozice'
    id = mariadb.Column(mariadb.Integer, primary_key=True)
    pozice = mariadb.Column(mariadb.String)

class Titul(mariadb.Model):
    __bind_key__ = 'mariadbUjep'
    __tablename__ = 'titul'
    id = mariadb.Column(mariadb.Integer, primary_key=True)
    titul = mariadb.Column(mariadb.String)