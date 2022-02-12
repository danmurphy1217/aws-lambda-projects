from dataclasses import dataclass

@dataclass
class Config:
    host: str
    username: str
    password: str
    db_name: str


config = Config(
    host = "lambda-poc.cqr3wactoekt.us-east-1.rds.amazonaws.com",
    username = "admin",
    password = "Daniel#1217",
    db_name = "lambdapoc"
)
