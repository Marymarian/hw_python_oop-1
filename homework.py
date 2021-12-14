"""
Программный модуль для фитнес-трекера.
Этот модуль будет рассчитывать и отображать результаты тренировки.
"""
from dataclasses import dataclass, asdict
from typing import Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        """Вывод строки сообщения"""
        return ('Тип тренировки: {training_type}; '
                'Длительность: {duration:.3f} ч.; '
                'Дистанция: {distance:.3f} км; '
                'Ср. скорость: {speed:.3f} км/ч; '
                'Потрачено ккал: {calories:.3f}.'.format(**asdict(self))
                )


class Training:
    """Базовый класс тренировки."""

    # Константа для перевода значений из метров в километры
    M_IN_KM: float = 1000
    # Расстояние, которое спортсмен преодолевает за один шаг
    LEN_STEP: float = 0.65
    # Константа для перевода часов в минуты
    MIN_IN_HOUR: float = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration_in_hours = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration_in_hours

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(type(self).__name__ + '.get_spent_calories')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration_in_hours,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


class Running(Training):
    """Тренировка: бег."""

    # Константы коэфициентов каллорий
    COEFF_CALORIE_1: float = 18
    COEFF_CALORIE_2: float = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.COEFF_CALORIE_1
                * super().get_mean_speed()
                - self.COEFF_CALORIE_2)
                * self.weight
                / self.M_IN_KM
                * (self.duration_in_hours * self.MIN_IN_HOUR)
                )


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    # Константы коэфициентов каллорий
    COEFF_CALORIE_1: float = 0.035
    COEFF_CALORIE_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.COEFF_CALORIE_1
                 * self.weight
                 + (super().get_mean_speed()**2 // self.height)
                 * self.COEFF_CALORIE_2
                 * self.weight)
                * (self.duration_in_hours * self.MIN_IN_HOUR)
                )


class Swimming(Training):
    """Тренировка: плавание."""

    # Расстояние, которое спортсмен преодолевает за один гребок
    LEN_STEP: float = 1.38
    # Константы коэфициентов каллорий
    COEFF_CALORIE_1: float = 1.1
    COEFF_CALORIE_2: float = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool
                * self.count_pool
                / self.M_IN_KM
                / self.duration_in_hours
                )

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.get_mean_speed() + self.COEFF_CALORIE_1)
                * self.COEFF_CALORIE_2
                * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_dict: dict[str, Type[Training]]
    training_dict = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    if workout_type in training_dict:
        return training_dict[workout_type](*data)
    else:
        raise ValueError("Несоответствующее значение")


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
