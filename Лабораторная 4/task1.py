from typing import List


class Science:
    """
    Базовый класс, представляющий общие характеристики науки.

    Атрибуты:
        _name (str): Название науки (инкапсулированный, чтобы предотвратить прямое изменение).
        description (str): Описание науки.
    """

    def __init__(self, name: str, description: str) -> None:
        """
        Конструктор класса Science.

        Args:
            name (str): Название науки.
            description (str): Описание науки.
        """
        self._name = name  # Инкапсуляция: имя не должно изменяться напрямую.
        self.description = description

    def __str__(self) -> str:
        """Возвращает строковое представление объекта для пользователя."""
        return f"Наука: {self._name}"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для разработчика."""
        return f"Science(name={self._name!r}, description={self.description!r})"

    def get_info(self) -> str:
        """
        Возвращает основную информацию о науке.

        Returns:
            str: Описание науки.
        """
        return f"{self._name}: {self.description}"

    def object_info(self) -> str:
        """
        Возвращает информацию о задачах, которые рассматривает данная наука.

        Returns:
            str: Общая информация о задачах науки.
        """
        return f"{self._name} рассматривает задачи, связанные с общим исследованием природы и явлений."


class Physics(Science):
    """
    Дочерний класс, представляющий физику как отдельную науку.

    Атрибуты:
        theories (List[str]): Список основных теорий физики.
    """

    def __init__(self, description: str, theories: List[str]) -> None:
        """
        Конструктор класса Physics. Расширяет базовый конструктор, добавляя теории.

        Args:
            description (str): Описание физики.
            theories (List[str]): Основные теории физики.
        """
        super().__init__("Физика", description)
        self.theories = theories

    def __str__(self) -> str:
        """Возвращает строковое представление объекта для пользователя."""
        return f"Физика: {self.description} (Основные теории: {', '.join(self.theories)})"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для разработчика."""
        return f"Physics(description={self.description!r}, theories={self.theories!r})"

    def object_info(self) -> str:
        """
        Переопределяет метод object_info для физики.

        Обоснование: Физика изучает законы природы, движение, энергию и материю,
        что требует специфического описания задач.

        Returns:
            str: Информация о задачах физики.
        """
        return (f"{self._name} рассматривает задачи, связанные с изучением материи, энергии, "
                "движения и фундаментальных законов природы.")

    def add_theory(self, theory: str) -> None:
        """
        Добавляет новую теорию в список.

        Args:
            theory (str): Новая теория.
        """
        self.theories.append(theory)


class Mathematics(Science):
    """
    Дочерний класс, представляющий математику как отдельную науку.

    Атрибуты:
        branches (List[str]): Список основных разделов математики.
    """

    def __init__(self, description: str, branches: List[str]) -> None:
        """
        Конструктор класса Mathematics. Расширяет базовый класс, добавляя разделы математики.

        Args:
            description (str): Описание математики.
            branches (List[str]): Основные разделы математики.
        """
        super().__init__("Математика", description)
        self.branches = branches

    def get_info(self) -> str:
        """
        Переопределяет метод get_info для добавления разделов математики.

        Returns:
            str: Описание математики с указанием разделов.
        """
        return f"{self._name}: {self.description} (Разделы: {', '.join(self.branches)})"


class ComputerScience(Science):
    """
    Дочерний класс, представляющий компьютерные науки.

    Атрибуты:
        programming_languages (List[str]): Список популярных языков программирования.
    """

    def __init__(self, description: str, programming_languages: List[str]) -> None:
        """
        Конструктор класса ComputerScience. Расширяет базовый класс, добавляя языки программирования.

        Args:
            description (str): Описание компьютерных наук.
            programming_languages (List[str]): Список популярных языков программирования.
        """
        super().__init__("Компьютерные науки", description)
        self.programming_languages = programming_languages

    def __str__(self) -> str:
        """Возвращает строковое представление объекта для пользователя."""
        return f"Компьютерные науки: {self.description} (Языки: {', '.join(self.programming_languages)})"

    def __repr__(self) -> str:
        """
        Переопределяет метод __repr__, чтобы включить языки программирования.

        Returns:
            str: Строковое представление объекта для разработчиков.
        """
        return (f"ComputerScience(description={self.description!r}, "
                f"programming_languages={self.programming_languages!r})")

    def object_info(self) -> str:
        """
        Переопределяет метод object_info для компьютерных наук.

        Обоснование: Компьютерные науки изучают алгоритмы, структуры данных и вычислительные системы,
        что требует специфического описания задач.

        Returns:
            str: Информация о задачах компьютерных наук.
        """
        return (f"{self._name} рассматривает задачи, связанные с разработкой алгоритмов, "
                "решением вычислительных задач и оптимизацией вычислительных систем.")

    def add_language(self, language: str) -> None:
        """
        Добавляет новый язык программирования в список.

        Args:
            language (str): Название нового языка программирования.
        """
        self.programming_languages.append(language)
