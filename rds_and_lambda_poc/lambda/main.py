import pymysql
import logging
import sys
from config import config
from uuid import uuid4
import json

rds_host = config.host
db_username = config.username
db_password = config.password
db_name = config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)


try:
    mysql_conn = pymysql.connect(
        host = rds_host,
        user = db_username,
        passwd = db_password,
        db = db_name
    )
except pymysql.MySQLError as err:
    logger.error(f"[ERROR]: Unexpected error - could not connect to RDS instance with db_name: {db_name}, username: {db_username}, password: {db_password}")
    logger.error(err)
    sys.exit()

logger.info("[Connection Established]: Successfully connected to RDS instance.")


def handler(event, context):
    """
    this function creates the Employees table should it not already
    exist and then inserted some data provided via the `event` into it.
    """

    with mysql_conn.cursor() as cursor:
        cursor.execute("create table if not exists Employee ( EmpID  varchar(32) NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        id = str(uuid4())
        cursor.execute(f"insert into Employee (EmpID, Name) values({id}, 'Dan')")
        logger.info(f"[handler]: {event['data']}")
        logger.info(f"[handler]: Generated UUID: {id}")

    mysql_conn.commit()
    return json.dumps({"uuid": id})
