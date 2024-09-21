from sqlalchemy import Column, Integer, String, Float, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Carrera(Base):
    __tablename__ = 'carreras'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    abierta = Column(Boolean, default=True) 
    ganador = Column(Integer, nullable=True)
    competidores = relationship("Competidor", back_populates="carrera")

class Competidor(Base):
    __tablename__ = 'competidores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    probabilidad = Column(Float)
    carrera_id = Column(Integer, ForeignKey('carreras.id'))
    carrera = relationship("Carrera", back_populates="competidores")

class Apostador(Base):
    __tablename__ = 'apostadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

class Apuesta(Base):
    __tablename__ = 'apuestas'
    id = Column(Integer, primary_key=True)
    monto = Column(Float)
    competidor_id = Column(Integer)
    apostador_id = Column(Integer)

# Crear la base de datos SQLite
engine = create_engine('sqlite:///carrerasx.db')
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()


