# A class containing the configuration for the application.
class Config:
    def __init__(self,
                 c_bar: int = 10,
                 L_max: int = 10,
                 split_rate: float = 0.5,
                 beta: float = 0.01,
                 blink_rate: float = 0.01,
                 min_fleet_iters_percentage: float = 0.1,
                 t0: int = 100,
                 tF: int = 1) -> None:
        self.c_bar = c_bar
        self.L_max = L_max
        self.split_rate = split_rate
        self.beta = beta
        self.blink_rate = blink_rate
        self.min_fleet_iters_percentage = min_fleet_iters_percentage
        self.t0 = t0
        self.tF = tF