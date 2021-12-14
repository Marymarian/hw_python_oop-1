"""
Программный модуль для фитнес-трекера.
Этот модуль будет рассчитывать и отображать результаты тренировки.
"""
<<<<<<< HEAD
from dataclasses import dataclass
from typing import Callable, Union


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
        return (f'Тип тренировки: {self.training_type}; '
                + f'Длительность: {self.duration:.3f} ч.; '
                + f'Дистанция: {self.distance:.3f} км; '
                + f'Ср. скорость: {self.speed:.3f} км/ч; '
                + f'Потрачено ккал: {self.calories:.3f}.')
=======


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Вывод строки сообщения"""
        return f'Тип тренировки: {self.training_type}; ' \
               f'Длительность: {self.duration:.3f} ч.; ' \
               f'Дистанция: {self.distance:.3f} км; ' \
               f'Ср. скорость: {self.speed:.3f} км/ч; ' \
               f'Потрачено ккал: {self.calories:.3f}.'
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3


class Training:
    """Базовый класс тренировки."""

    # Константа для перевода значений из метров в километры
<<<<<<< HEAD
    M_IN_KM: float = 1000
    # Расстояние, которое спортсмен преодолевает за один шаг
    LEN_STEP: float = 0.65
    # Константа для перевода часов в минуты
    MIN_IN_HOUR: float = 60
=======
    M_IN_KM = 1000
    # Расстояние, которое спортсмен преодолевает за один шаг
    LEN_STEP = 0.65
    # Константа для перевода часов в минуты
    MIN_IN_HOUR = 60
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
<<<<<<< HEAD
        self.duration_in_hours = duration
        self.duration_in_min = duration * self.MIN_IN_HOUR
=======
        self.duration = duration
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
<<<<<<< HEAD
        return self.get_distance() / self.duration_in_hours
=======
        return self.get_distance() / self.duration
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(type(self).__name__ + '.get_spent_calories')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
<<<<<<< HEAD
        return InfoMessage(type(self).__name__,
                           self.duration_in_hours,
=======
        return InfoMessage(self.__class__.__name__,
                           self.duration,
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

<<<<<<< HEAD
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
                * self.duration_in_min)
=======
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        return ((coeff_calorie_1
                * super().get_mean_speed()
                - coeff_calorie_2)
                * self.weight
                / self.M_IN_KM
                * (self.duration * self.MIN_IN_HOUR))
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

<<<<<<< HEAD
    # Константы коэфициентов каллорий
    COEFF_CALORIE_1: float = 0.035
    COEFF_CALORIE_2: float = 0.029

=======
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3
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
<<<<<<< HEAD
        return ((self.COEFF_CALORIE_1
                 * self.weight
                 + (super().get_mean_speed()**2 // self.height)
                 * self.COEFF_CALORIE_2
                 * self.weight)
                * self.duration_in_min)
=======
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        return ((coeff_calorie_1
                 * self.weight
                 + (super().get_mean_speed()**2 // self.height)
                 * coeff_calorie_2
                 * self.weight)
                * (self.duration * self.MIN_IN_HOUR))
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3


class Swimming(Training):
    """Тренировка: плавание."""
<<<<<<< HEAD
=======

    LEN_STEP = 1.38

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
                / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        return ((self.get_mean_speed() + coeff_calorie_1)
                * coeff_calorie_2
                * self.weight)
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3

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
                / self.duration_in_hours)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.get_mean_speed() + self.COEFF_CALORIE_1)
                * self.COEFF_CALORIE_2
                * self.weight)


def read_package(workout_type: str, data: list) -> Union[Training, str]:
    """Прочитать данные полученные от датчиков."""
<<<<<<< HEAD
    training_dict: dict[str, Callable[..., Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
        }
    if workout_type in training_dict:
        return training_dict[workout_type](*data)
    else:
        return 'Данный вид тренировки отсутствует в базе!'
=======
    training_dict = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking
                     }
    if workout_type in training_dict:
        return training_dict[workout_type](*data)
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3


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
<<<<<<< HEAD
        if type(training).__name__ != 'str':
            main(training)
        else:
            print(training)
=======
        main(training)
>>>>>>> 334689691f0926b981f95b557cb0146f39135bb3
