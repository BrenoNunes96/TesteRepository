import datetime
from sqlalchemy import Column, Integer, String, ForeignKey,Date
from sqlalchemy.orm import declarative_base, relationship



#*Tabela clientes:** id_cliente (INT, PK), nome (VARCHAR), estado (VARCHAR)

#*Tabela processos:** id_processo (INT, PK), id_cliente (INT, FK), assunto (VARCHAR), data_abertura (DATE)


Base =  declarative_base()


class clientes(Base):
 __tablename__ = 'clientes'

 id_cliente = Column(Integer,primary_key =True)
 nome = Column(String(255),nullable=False)
 estado =Column(String(50))  

relacionarProcessos = relationship("processos",back_populates='clientes') 


class processos(Base):
 __tablename__= 'processos'

 id_processo = Column(Integer,primary_key=True)
 assunto = Column(String(255),nullable=False)
 data_abertura =Column(Date)

 id_ciente = Column(Integer,ForeignKey('clientes.id_cliente'))

 relacionarCliente = relationship('clientes',back_populates='processos')


print(processos)