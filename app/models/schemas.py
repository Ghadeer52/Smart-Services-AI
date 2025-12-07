"""
Pydantic Models for API validation
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional


class Service(BaseModel):
    """Service model"""
    service_id: int
    name: str
    category: str
    expiry_date: str
    days_left: int
    usage_count: int = 0
    category_importance: float = 0.5
    seasonality: Optional[str] = None
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_id": 101,
                "name": "Passport Renewal",
                "category": "travel",
                "expiry_date": "2026-01-25",
                "days_left": 28,
                "usage_count": 4,
                "category_importance": 0.8,
                "seasonality": "in_season"
            }
        }
    )


class User(BaseModel):
    """User model"""
    id: int
    name: str
    national_id: str
    city: str
    activity_level: str = "medium"
    phone: str
    last_login: str
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Ghadeer Sameer",
                "national_id": "2190065411",
                "city": "Riyadh",
                "activity_level": "high",
                "phone": "+966500000000",
                "last_login": "2025-01-18T09:32:00Z"
            }
        }
    )


class RecommendationRequest(BaseModel):
    """Recommendation request model"""
    user: User
    services: List[Service]
    top_n: int = Field(default=5, ge=1, le=10, description="Number of top recommendations to return")