from flask_sqlalchemy import SQLAlchemy

from app import univerzita

mariadbLogin = SQLAlchemy()
mariadbUjep = SQLAlchemy()

class Login(mariadbLogin.Model):
    username = mariadbLogin.Column(mariadbLogin.String, primary_key=True, nullable=False)
    password = mariadbLogin.Column(mariadbLogin.String, nullable=False)

fakultaHasClovek = mariadbUjep.Table('fakultaHasClovek',
    mariadbUjep.Column('fakulta_id', mariadbUjep.Integer, mariadbUjep.ForeignKey('fakulta.id')),
    mariadbUjep.Column('clovek_id', mariadbUjep.Integer, mariadbUjep.ForeignKey('clovek.id')))

clovekHasTitul = mariadbUjep.Table('clovekHasTitul',
    mariadbUjep.Column('clovek_id', mariadbUjep.Integer, mariadbUjep.ForeignKey('clovek.id')),
    mariadbUjep.Column('titul_id', mariadbUjep.Integer, mariadbUjep.ForeignKey('titul.id')))

clovekHasPozice = mariadbUjep.Table('clovekHasPozice',
    mariadbUjep.Column('clovek_id', mariadbUjep.Integer, mariadbUjep.ForeignKey('clovek.id')),
    mariadbUjep.Column('pozice_id', mariadbUjep.Integer, mariadbUjep.ForeignKey('pozice.id')))

class Univerzita(mariadbUjep.Model):
    id = mariadbUjep.Column(mariadbUjep.Integer, primary_key=True)
    nazev = mariadbUjep.Column(mariadbUjep.String)
    #fakulty = mariadbUjep.relationship('Fakulta', backref='univerzita')

class Fakulta(mariadbUjep.Model):
    id = mariadbUjep.Column(mariadbUjep.Integer, primary_key=True)
    nazev = mariadbUjep.Column(mariadbUjep.String)
    univerzita_id = mariadbUjep.Column(mariadbUjep.Integer, mariadbUjep.ForeignKey('univerzita.id'))
    lidi = mariadbUjep.relationship('Clovek', secondary=fakultaHasClovek)

class Clovek(mariadbUjep.Model):
    id = mariadbUjep.Column(mariadbUjep.Integer, primary_key=True)
    jmeno = mariadbUjep.Column(mariadbUjep.String)
    prijmeni = mariadbUjep.Column(mariadbUjep.String)
    tituly = mariadbUjep.relationship('Titul', secondary=clovekHasTitul)
    pozice = mariadbUjep.relationship('Pozice', secondary=clovekHasPozice)

class Pozice(mariadbUjep.Model):
    id = mariadbUjep.Column(mariadbUjep.Integer, primary_key=True)
    pozice = mariadbUjep.Column(mariadbUjep.String)

class Titul(mariadbUjep.Model):
    id = mariadbUjep.Column(mariadbUjep.Integer, primary_key=True)
    titul = mariadbUjep.Column(mariadbUjep.String)