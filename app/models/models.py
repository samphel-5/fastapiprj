from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Owner(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    first_name: str
    last_name: str
    phone_no: int = Field(index=True)

class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    first_name: str
    last_name: str
    phone_no: int = Field(index=True)

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    first_name: str
    last_name: str
    phone_no: int = Field(index=True)

class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="owner.id")
    client_id: int = Field(foreign_key="client.id")
    name: str = Field(index=True)
    address: str
    city: Optional[str] = Field(default=None)
    state: Optional[str] = Field(default=None)
    province: Optional[str] = Field(default=None)
    zip: Optional[int] = Field(default=None)
    country: Optional[str] = Field(default=None)
    phone_no: str = Field(index=True)

class Area(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    location_id: int = Field(foreign_key="location.id")
    name: str = Field(index=True)
    description: str

class Shift(SQLModel, table=True):
    id: int = Field(primary_key=True)
    location_id: int = Field(foreign_key="location.id")
    name: str = Field(index=True)
    start_time: str
    end_time: str

class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    shift_id: int = Field(foreign_key="shift.id")
    name: str = Field(index=True)
    description: Optional[str] = Field(default=None)

class ShiftAssignment(SQLModel, table=True):
    location_id: int = Field(primary_key=True, foreign_key="location.id")
    shift_id: int = Field(primary_key=True, foreign_key="shift.id")
    team_id: int = Field(primary_key=True, foreign_key="team.id")