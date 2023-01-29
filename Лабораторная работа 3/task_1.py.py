class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

        @property
        def name(self) -> str:
            return self._name

        @property
        def author(self) -> str:
            return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

        @property
        def pages(self) -> int:
            return self._pages

        @pages.setter
        def pages(self, set_pages: int) -> None:
            if not isinstance(set_pages, int):
                raise TypeError('Число страниц - целое')
            if set_pages <= 0:
                raise ValueError('Чило страниц больше 0')
            self._pages = set_pages

    def __str__(self):
        return f"Книга бумажная {self.name}. Автор {self.author}. Число страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

        @property
        def duration(self) -> float:
            return self._duration

        @duration.setter
        def duration(self, set_duration: float) -> None:
            if not isinstance(set_duration, float):
                raise TypeError('Продолжительность')
            if set_duration <= 0:
                raise ValueError('Продолжительность больше 0')
            self._duration = set_duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

