from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import socket

engine = create_engine('rqlite+pyrqlite://localhost:4001/', echo=True)

class Base(DeclarativeBase):
      pass

class Node(Base):
      __tablename__ = 'node'

      id: Mapped[int] = mapped_column(primary_key=True)
      name: Mapped[str] = mapped_column(String(30))
      ip:   Mapped[str] = mapped_column(String)
      enable: Mapped[bool] = mapped_column(unique=False,default=False)
      alive:  Mapped[bool] = mapped_column(unique=False,default=False)

Base.metadata.create_all(engine)
with Session(engine) as session:
     thenode = Node(name=socket.getfqdn()),
