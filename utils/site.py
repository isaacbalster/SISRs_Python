class Site:
    def __init__(self,
                 id: int,
                 x: int,
                 y: int) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.demand = 0
        self.adj_list = list()
        self.route_id = 0
        self.route_pos = 0