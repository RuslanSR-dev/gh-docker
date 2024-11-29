import os


class Links:

    HOST = f"https://sdesk.{os.environ['STAGE']}.eft-pos.ru"

    LOGIN_PAGE = f"{HOST}/login"
    REQUEST_PAGE = f"{HOST}/requests"
    SERVICES_PAGE = f"{HOST}/categories/services"
    NEW_SERVICES_PAGE = f"{HOST}/categories/service/new"
    NEW_REQUEST_PAGE = f"{HOST}/requests/new"
