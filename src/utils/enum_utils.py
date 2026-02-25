from enum import Enum


class PlayerLevel(str, Enum):
    beginner = "новичок"
    amateur = "любитель"
    medium = "средний"
    advanced = "продвинутый"
    pro = "профессионал"
