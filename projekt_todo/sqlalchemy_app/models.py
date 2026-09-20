import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# Tabela pośrednia dla relacji wiele-do-wielu.
# Łączy zadania z tagami.
zadania_tagi = Table(
    "zadania_tagi",
    Base.metadata,
    Column(
        "zadanie_id",
        ForeignKey("zadania.id"),
        primary_key=True
    ),
    Column(
        "tag_id",
        ForeignKey("tagi.id"),
        primary_key=True
    )
)


class Zadanie(Base):
    __tablename__ = "zadania"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    opis: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    zrobione: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    data_utworzenia: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.utcnow
    )

    # Jedno zadanie może mieć wiele tagów.
    # Jeden tag może należeć do wielu zadań.
    tagi: Mapped[list["Tag"]] = relationship(
        secondary=zadania_tagi,
        back_populates="zadania"
    )


class Tag(Base):
    __tablename__ = "tagi"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    nazwa: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    # Relacja odwrotna:
    # jeden tag może być przypisany do wielu zadań.
    zadania: Mapped[list["Zadanie"]] = relationship(
        secondary=zadania_tagi,
        back_populates="tagi"
    )