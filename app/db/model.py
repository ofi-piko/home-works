from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine("sqlite:///db.sqlite3")

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "User"

    name: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(String(17), unique=True)

class master(Base):
    __tablename__ = "service"

    name: Mapped[int] = mapped_column(primary_key=True)
    age: Mapped[str] = mapped_column(String(3), unique=True)
    rating: Mapped[str] = mapped_column(String(5), unique=True)



class Service(Base):
    __tablename__ = "service"

    service_id: Mapped[int] = mapped_column(primary_key=True)
    style: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column()


class Location(Base):
    __tablename__ = "location"

    Location: Mapped[int] = mapped_column(primary_key=True)



async def start_running():
    with engine.begin() as conn:
        Base.metadata.create_all(conn)
