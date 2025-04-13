from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, Float, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..utils.database import Base

class Screener(Base):
    __tablename__ = "screeners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    criteria = Column(JSON)  # Stores the screening criteria
    created_by = Column(Integer, ForeignKey("users.id"))
    is_public = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    creator = relationship("User", back_populates="screeners")
    runs = relationship("ScreenerRun", back_populates="screener")

class ScreenerRun(Base):
    __tablename__ = "screener_runs"

    id = Column(Integer, primary_key=True, index=True)
    screener_id = Column(Integer, ForeignKey("screeners.id"))
    run_by = Column(Integer, ForeignKey("users.id"))
    results = Column(JSON)  # Stores the screening results
    execution_time = Column(Float)  # Time taken to run the screener
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    screener = relationship("Screener", back_populates="runs")
    user = relationship("User", back_populates="screener_runs")

class BacktestResult(Base):
    __tablename__ = "backtest_results"

    id = Column(Integer, primary_key=True, index=True)
    screener_id = Column(Integer, ForeignKey("screeners.id"))
    run_by = Column(Integer, ForeignKey("users.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    results = Column(JSON)  # Stores backtest results including metrics
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    screener = relationship("Screener")
    user = relationship("User") 