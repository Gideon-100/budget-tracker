from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<User id={self.id} name={self.name!r}>"

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Category id={self.id} name={self.name!r}>"

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    # store date as DATE; default to current date if not provided
    date = Column(Date, server_default=func.current_date(), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    user = relationship("User", backref="expenses")
    category = relationship("Category", backref="expenses")

    def __repr__(self):
        return f"<Expense id={self.id} desc={self.description!r} amount={self.amount}>"

