class Tour:
    def __init__(self,
                 capacity: int) -> None:
        self.tour = [0,0]
        self.cost = 0
        self.cardinality = 0
        self.cap_slack = capacity
        self.spatial_slack = 0