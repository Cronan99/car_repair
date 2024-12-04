from typing import Any


class BaseModel:
    def to_dict(self) -> dict[str: Any]:
        return {k: v for k, v in self.__dict__.items()}
    
    def __str__(self) -> str:
        return str(self.to_dict())