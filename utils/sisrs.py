from .tour import Tour

class SISRs:
    def __init__(self) -> None:
        pass

    def get_initial_sol(self,
                        capacity: int,
                        dist_matrix: list,
                        sites: list,
                        tours: list) -> None:
        """
        A function to populate an initial solution to the SISRs problem.
        The initial solution is built by initialising one route for each
        customer site.
        """
        for i in range(1, len(sites)):
            tours.append(Tour(capacity))
            tours[i-1].route.insert(1, i)
            tours[i-1].cost = dist_matrix[0][i] + dist_matrix[i][0]
            tours[i-1].cardinality += 1
            tours[i-1].cap_slack -= sites[i].demand
            sites[i].route_id = i-1
            sites[i].route_pos = 1
    
    def print_sol(self,
                  tours: list) -> None:
        """
        A function to print a SISRs solution to the routing problem.
        """
        # Print initial solution.
        for i in range(len(tours)):
            print(f'Route #{i+1}: ' +
                  ' '.join([str(c) for c in tours[i].route[1:-1]]))
        print(f'Cost: {sum([tours[i].cost for i in range(len(tours))])}')