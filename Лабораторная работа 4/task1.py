from typing import Union


class Car:
    def __init__(self, oil_amount: Union[int, float], oil_consumption: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param oil_amount: текущее количество топлива в баке
        :param oil_consumption: потребление топлива на единицу пути
        """
        self._oil_amount = None  # protected, т к меняется только при заправке/совершении поездки
        self._init_oil_amount(oil_amount)

        self._oil_consumption = None  # protected, т к это неизменная характеристика автомобиля
        self._init_oil_consumption(oil_consumption)

    def __str__(self) -> str:
        """
        Печатный вид экземпляра класса
        """
        return f"Автомобиль. Количество топлива {self.oil_amount} л. Потребление топлива {self.oil_consumption} л/км"

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        """
        return f"{self.__class__.__name__}(oil_amount={self.oil_amount}, oil_consumption={self.oil_consumption})"

    def _init_oil_amount(self, oil_amount: Union[int, float]) -> None:
        """
        Инициализация protected атрибута _oil_amount - текущее количество топлива
        Protected из-за того, что используется только при инициализации экземпляра класса
        :param oil_amount: текущее количество топлива
        """
        if not isinstance(oil_amount, (int, float)):
            raise TypeError('Количество топлива должно быть типа int или float')
        if oil_amount < 0:
            raise ValueError('Количество топлива должно быть не меньше 0')
        self._oil_amount = oil_amount

    def _init_oil_consumption(self, oil_consumption: Union[int, float]) -> None:
        """
        Инициализация protected атрибута _oil_consumption - потребление топлива на единицу пути
        Protected метод из-за того, что используется только при инициализации экземпляра класса
        :param oil_consumption: потребление топлива на единицу пути
        """
        if not isinstance(oil_consumption, (int, float)):
            raise TypeError('Потребление топлива должно быть типа int или float')
        if oil_consumption <= 0:
            raise ValueError('Потребление топлива должно быть больше 0')
        self._oil_consumption = oil_consumption

    @property
    def oil_amount(self) -> Union[int, float]:
        """
        getter для protected атрибута _oil_amount
        setter не используется, т к protected атрибут
        """
        return self._oil_amount

    @property
    def oil_consumption(self) -> Union[int, float]:
        """
        getter для protected атрибута _oil_consumption
        setter не используется, т к protected атрибут
        """
        return self._oil_consumption

    def add_oil(self, extra_oil: Union[int, float]) -> None:
        """
        Добавить топлива в бак
        Публичный метод
        :param extra_oil: дополнительное топливо
        """
        if not isinstance(extra_oil, (int, float)):
            raise TypeError('Добавленное топливо должно быть типа int или float')
        if extra_oil < 0:
            raise ValueError('Добавленное топливо должно быть не меньше 0')
        self._oil_amount += extra_oil

    def make_trip(self, distance: Union[int, float]) -> None:
        """
        Совершить поездку длиной distance, соответственно потратив некоторое количество топлива
        Публичный метод
        :param distance: длина пути
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина пути должна быть типа int или float')
        if distance < 0:
            raise ValueError('Длина пути должна быть не меньше 0')
        ...


class PassengerCar(Car):
    def __init__(self, oil_amount: Union[int, float], oil_consumption: Union[int, float], seats: int):
        """
        Создание и подготовка к работе объекта класса "Пассажирский автомобиль", унаследован от класса "Автомобиль"
        :param oil_amount: текущее количество топлива в баке
        :param oil_consumption: потребление топлива на единицу пути
        :param seats: количество мест в автомобиле
        """
        super().__init__(oil_amount, oil_consumption)
        self._seats = None  # protected, т к это неизменная характеристика автомобиля
        self._init_seats(seats)

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        Перегрузка метода базового класса
        """
        return f"{self.__class__.__name__}(oil_amount={self.oil_amount}, " \
               f"oil_consumption={self.oil_consumption}, seats={self.seats})"

    def _init_seats(self, seats: int) -> None:
        """
        Инициализация protected атрибута _seats - количество мест в автомобиле
        Protected метод из-за того, что используется только при инициализации экземпляра класса
        :param seats: количество мест в автомобиле
        """
        if not isinstance(seats, int):
            raise TypeError('Количество мест в автомобиле должно быть типа int')
        if seats <= 0:
            raise ValueError('Количество мест в автомобиле должно быть больше 0')
        self._seats = seats

    @property
    def seats(self) -> int:
        """
        getter для protected атрибута _seats
        setter не используется, т к protected атрибут
        """
        return self._seats

    def make_trip(self, distance: Union[int, float]) -> None:
        """
        Совершить поездку длиной distance, соответственно потратив некоторое количество топлива
        Перегрузка метода базового класса, т к совершаем поездку на пассажирском автомобиле
        Публичный метод
        :param distance: длина пути
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина пути должна быть типа int или float')
        if distance < 0:
            raise ValueError('Длина пути должна быть не меньше 0')
        ...


class CargoCar(Car):
    def __init__(self, oil_amount: Union[int, float], oil_consumption: Union[int, float], capacity: Union[int, float]):
        """
        Создание и подготовка к работе объекта класса "Грузовой автомобиль", унаследован от класса "Автомобиль"
        :param oil_amount: текущее количество топлива в баке
        :param oil_consumption: потребление топлива на единицу пути
        :param capacity: грузоподъемность
        """
        super().__init__(oil_amount, oil_consumption)
        self._capacity = None  # protected, т к это неизменная характеристика автомобиля
        self._init_capacity(capacity)

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        Перегрузка метода базового класса
        """
        return f"{self.__class__.__name__}(oil_amount={self.oil_amount}, " \
               f"oil_consumption={self.oil_consumption}, capacity={self.capacity})"

    def _init_capacity(self, capacity: Union[int, float]) -> None:
        """
        Инициализация protected атрибута _capacity - грузоподъемность
        Protected метод из-за того, что используется только при инициализации экземпляра класса
        :param capacity: грузоподъемность
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError('Грузоподъемность автомобиля должна быть типа int или float')
        if capacity <= 0:
            raise ValueError('Грузоподъемность автомобиля должна быть больше 0')
        self._capacity = capacity

    @property
    def capacity(self) -> Union[int, float]:
        """
        getter для protected атрибута _capacity
        setter не используется, т к protected атрибут
        """
        return self._capacity

    def make_trip(self, distance: Union[int, float]) -> None:
        """
        Совершить поездку длиной distance, соответственно потратив некоторое количество топлива
        Перегрузка метода базового класса, т к совершаем поездку на грузовом автомобиле
        Публичный метод
        :param distance: длина пути
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина пути должна быть типа int или float')
        if distance < 0:
            raise ValueError('Длина пути должна быть не меньше 0')
        ...