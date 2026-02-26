from enum import Enum


class UserLevel(str, Enum):
    beginner = "новичок"
    amateur = "любитель"
    medium = "средний"
    advanced = "продвинутый"
    pro = "профессионал"
