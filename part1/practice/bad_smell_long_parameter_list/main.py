# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:

    _flight_speed_coefficient: float = 1.2
    _crawl_speed_coefficient: float = 0.5

    def __init__(self, x_coord, y_coord, is_fly, crawl):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.is_fly = is_fly
        self.crawl = crawl

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        self._move_methods = {
            "UP": "_move_up",
            "DOWN": "_move_down",
            "LEFT": "_move_left",
            "RIGHT": "_move_right",
        }

    def _refine_speed(self, base_speed):
        if self.is_fly:
            return base_speed * self._flight_speed_coefficient
        if self.crawl:
            return base_speed * self._crawl_speed_coefficient

    def _move_up(self, speed):
        self.y_coord += speed

    def _move_down(self, speed):
        self.y_coord -= speed

    def _move_left(self, speed):
        self.x_coord -= speed

    def _move_right(self, speed):
        self.x_coord += speed

    def _move(self, direction, speed):
        method = self._move_methods.get(direction)
        if method is None:
            raise ValueError('Неправильное направление')
        getattr(self, method)(speed)

    def move(self, field, direction, speed=1):

        speed = self._refine_speed(speed)
        self._move(direction, speed)
        field.set_unit(x=self.x_coord, y=self.y_coord, unit=self)

#     ...
