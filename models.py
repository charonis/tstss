from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "qrcode"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    first_name: Mapped[str]
    patronymic:Mapped[str]    
    info: Mapped[str] 
    unique_key: Mapped[str]
    