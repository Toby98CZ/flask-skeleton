from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, Integer, String, DateTime
from datetime import datetime

from ..database import db
from ..mixins import CRUDModel

class Databaze(CRUDModel):
    __tablename__ = 'Hodnoty'
    __table_args__ = {'sqlite_autoincrement': True}
    hodnota1 = Column(String, nullable=False, index=False)
    hodnota2 = Column(String, nullable=False, index=True)

    datum_insertu = Column(DateTime, default=datetime.now())

