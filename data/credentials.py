import os
from dotenv import load_dotenv

load_dotenv()


class Credentials:

    LOGIN_DOCKER = os.getenv("LOGIN_DOCKER")
    PASSWORD_DOCKER = os.getenv("PASSWORD_DOCKER")
