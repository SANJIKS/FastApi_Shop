from config.settings import Base
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped



class Category(Base):
    __tablename__ = 'categories'

    id:Mapped[int] = mapped_column(primary_key=True)
    slug:Mapped[str] = mapped_column(unique=True)
    name:Mapped[str] = mapped_column()

    def __str__(self):
        return self.name