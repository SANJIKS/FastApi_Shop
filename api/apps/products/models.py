import decimal
from config.settings import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from config.settings import Base
from apps.brands.models import Brand
from apps.categories.models import Category


class Products(Base):
    __tablename__ = 'products'

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column()
    price:Mapped[float]
    article:Mapped[str]
    image:Mapped[str]
    body:Mapped[str]
    category_id:Mapped[int] = mapped_column(ForeignKey('categories.id'))
    brand_id:Mapped[int] = mapped_column(ForeignKey('brands.id'))

    
    category:Mapped['Category'] = relationship(Category, lazy="joined")
    brand:Mapped['Brand'] = relationship(Brand, lazy="joined")

    def __str__(self):
        return self.name