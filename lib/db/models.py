# lib/models.py
# lib/db/models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Base + Engine + Session
Base = declarative_base()
engine = create_engine("sqlite:///clothes_store.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=False)

    # Relationship with ClothingItem
    items = relationship("ClothingItem", back_populates="store", cascade="all, delete")

    @classmethod
    def create(cls, name, location):
        if not name or not location:
            raise ValueError("Name and location cannot be empty")
        store = cls(name=name, location=location)
        session.add(store)
        session.commit()
        return store

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, store_id):
        return session.get(cls, store_id)

    @classmethod
    def delete(cls, store_id):
        store = session.get(cls, store_id)
        if store:
            session.delete(store)
            session.commit()
            return True
        return False

    @classmethod
    def update(cls, store_id, name=None, location=None):
        store = session.get(cls, store_id)
        if not store:
            return None
        if name:
            store.name = name
        if location:
            store.location = location
        session.commit()
        return store


class ClothingItem(Base):
    __tablename__ = "clothing_items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    size = Column(String, nullable=False)
    color = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="items")

    @classmethod
    def create(cls, name, size, color, price, store_id):
        if not name or not size or not color or price < 0:
            raise ValueError("Invalid input for clothing item")
        item = cls(name=name, size=size, color=color, price=price, store_id=store_id)
        session.add(item)
        session.commit()
        return item

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, item_id):
        return session.get(cls, item_id)

    @classmethod
    def delete(cls, item_id):
        item = session.get(cls, item_id)
        if item:
            session.delete(item)
            session.commit()
            return True
        return False

    @classmethod
    def update(cls, item_id, name=None, size=None, color=None, price=None, store_id=None):
        item = session.get(cls, item_id)
        if not item:
            return None
        if name:
            item.name = name
        if size:
            item.size = size
        if color:
            item.color = color
        if price is not None and price >= 0:
            item.price = price
        if store_id:
            item.store_id = store_id
        session.commit()
        return item



Base.metadata.create_all(engine)
