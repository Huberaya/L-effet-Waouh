"""
Modèles SQLAlchemy pour V2 - à utiliser avec FastAPI
"""
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Text, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Table liaison N-N
product_categories = Table(
    'product_categories', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    slug = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    description = Column(Text)
    event_type = Column(String) # mariage, gender_reveal...
    position = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    image_url = Column(String)
    
    parent = relationship("Category", remote_side=[id], backref="children")
    products = relationship("Product", secondary=product_categories, back_populates="categories")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    sku = Column(String, unique=True, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    short_desc = Column(String)
    long_desc = Column(Text)
    price_ht = Column(Float, nullable=False)
    price_ttc = Column(Float, nullable=False)
    tva_rate = Column(Float, default=20.0)
    cost_price = Column(Float)
    stock_qty = Column(Integer, default=0)
    weight_grams = Column(Integer, default=0)
    event_type = Column(String)
    is_active = Column(Boolean, default=True)
    is_featured = Column(Boolean, default=False)
    is_consumable = Column(Boolean, default=False)
    brand = Column(String)
    video_url = Column(String)

    categories = relationship("Category", secondary=product_categories, back_populates="products")
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")

    @property
    def marge_pct(self):
        if self.price_ttc and self.cost_price:
            return round((self.price_ttc - self.cost_price) / self.price_ttc * 100, 1)
        return 0

class ProductVariant(Base):
    __tablename__ = 'product_variants'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    sku = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    attribute_type = Column(String) # color, pack_qty
    attribute_value = Column(String) # rose, bleu, x3
    price_ttc = Column(Float)
    stock_qty = Column(Integer, default=0)
    image_url = Column(String)
    is_active = Column(Boolean, default=True)

    product = relationship("Product", back_populates="variants")

class ProductImage(Base):
    __tablename__ = 'product_images'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    url = Column(String, nullable=False)
    alt = Column(String)
    position = Column(Integer, default=0)
    is_main = Column(Boolean, default=False)

    product = relationship("Product", back_populates="images")
