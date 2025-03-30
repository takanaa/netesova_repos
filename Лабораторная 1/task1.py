

class Browser:
    def __init__(self, name: str, version: str) -> None:
        """
        Инициализация браузера.

        :param name: Название браузера (например, Chrome, Firefox).
        :param version: Версия браузера (например, 98.0).
        :raises ValueError: Если версия браузера не в формате X.Y.Z.

        Пример:
        >>> braus = Browser('Yandex', '51.39.9')
        """
        if not self._is_valid_version(version):
            raise ValueError("Версия должна быть в формате X.Y.Z.")
        self.name = name
        self.version = version

    def _is_valid_version(self, version: str) -> bool:
        """
        Проверка правильности формата версии.

        :param version: Строка версии браузера.
        :returns: True, если версия правильная, иначе False.
        Пример:
        >>> braus = Browser('Yandex', '5.1.3')
        >>> braus_is_valid_version()
        """
        parts = version.split(".")
        return len(parts) == 3 and all(part.isdigit() for part in parts)


    def open_tab(self, url: str) -> None:
        """
        Открытие новой вкладки.

        :param url: URL для открытия.
        :returns: None
        :raises ValueError: Если URL не является валидным.
        Пример:
        >>> braus = Browser('Yandex', '98.0.1')
        >>> braus.open_tab('https://example.com')
        """
        ...


    def clear_history(self) -> None:
        """
        Очистка истории браузера.

        :returns: None
        Пример:
        >>> braus = Browser('Yandex', '92.5.1', [])
        >>> braus.clear_history()
        """
        ...

    class Garland():
        def __init__(self, bulb_type: str, num_bulbs: int, color: str) -> None:
            """
            Инициализация гирлянды.

            :param bulb_type: Тип лампочек (например, LED, обычные).
            :param num_bulbs: Количество лампочек в гирлянде.
            :param color: Цвет гирлянды.
            :raises ValueError: Если количество лампочек меньше 1.
            """
            if num_bulbs < 1:
                raise ValueError("Количество лампочек не может быть меньше 1.")
            if not isinstance(num_bulbs, (int)):
                raise TypeError("Количество жидкости должно быть int или float")
            self.bulb_type = bulb_type
            self.num_bulbs = num_bulbs
            self.color = color

        def turn_on(self) -> None:
            """
            Включение гирлянды.

            :returns: None
            Пример:
            >>> garland = Garland('LED', 50, 'multicolor')
            >>> garland.turn_on()
            """
            ...

        def turn_off(self) -> None:
            """
            Выключение гирлянды.

            :returns: None
            Пример:
            >>> garland = Garland('LED', 50, 'multicolor')
            >>> garland.turn_off()
            """
            ...

        def replace_bulb(self, position: int) -> None:
            """
            Замена лампочки на указанной позиции.

            :param position: Позиция лампочки для замены (от 1 до num_bulbs).
            :returns: None
            :raises IndexError: Если позиция вне допустимого диапазона.
            Пример:
            >>> garland = Garland('LED', 50, 'multicolor')
            >>> garland.replace_bulb(5)
            """
            if position < 1 or position > self.num_bulbs:
                raise IndexError("Неверная позиция лампочки.")
            ...

        class Whiteboard():
            def __init__(self, material: str, size: tuple[int, int]) -> None:
                """
                Инициализация доски для маркеров.

                :param material: Материал доски.
                :param size: Размер доски (ширина, высота) в сантиметрах.
                :raises ValueError: Если хотя бы одно из измерений меньше 30 см.
                """
                if size[0] < 30 or size[1] < 30:
                    raise ValueError("Размер доски должен быть не меньше 30x30 см.")
                self.material = material
                self.size = size

            def write(self, text: str) -> None:
                """
                Написание текста на доске.

                :param text: Текст для написания.
                :returns: None
                Пример:
                >>> board = Whiteboard('glass', (100, 60))
                >>> board.write('Hello, world!')
                """
                ...

            def erase(self) -> None:
                """
                Стирание всего текста с доски.

                :returns: None
                Пример:
                >>> board = Whiteboard('glass', (100, 60))
                >>> board.erase()
                """
                ...

            def change_marker(self, color: str) -> None:
                """
                Замена маркера на новый цвет.

                :param color: Цвет маркера.
                :returns: None
                :raises ValueError: Если цвет маркера не поддерживается.
                Пример:
                >>> board = Whiteboard('glass', (100, 60))
                >>> board.change_marker('blue')
                """
                supported_colors = ['red', 'blue', 'green', 'black']
                if color not in supported_colors:
                    raise ValueError(f"Цвет '{color}' не поддерживается.")
                ...