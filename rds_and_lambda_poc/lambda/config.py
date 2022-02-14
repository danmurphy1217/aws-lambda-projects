from dataclasses import dataclass

@dataclass
class Config:
    host: str
    username: str
    password: str
    db_name: str
