import math
from .instance import Instance
from .site import Site

class Data:
    def __init__(self) -> None:
        pass

    def read_instance_X(file: str,
                        sites: list) -> Instance:
        """
        A function to read an instance file of set X, populate the sites list,
        and return an Instance class instance.
        """
        # Try to open file and throw error if it fails.
        try:
            with open(file, 'r') as f:
                name = f.readline().split()[2]
                _ = f.readline()
                _ = f.readline()
                n = int(f.readline().split()[2])
                _ = f.readline()
                capacity = int(f.readline().split()[2])
                _ = f.readline()
                instance = Instance(name, int(n), int(capacity))
                # print(f'Instance: {instance.name}, with {instance.n} sites and'\
                #       f' capacity {instance.capacity}')
                # First loop to read coordinates.
                for i in range(n):
                    line = f.readline().split()
                    sites.append(Site(i, int(line[1]), int(line[2])))
                    # print(f'Site {sites[i].id} at ({sites[i].x}, {sites[i].y})')
                # Skip line.
                _ = f.readline()
                # Second loop to read demands.
                for i in range(n):
                    line = f.readline().split()
                    sites[i].demand = int(line[1])
                    # print(f'Site {sites[i].id} has demand {sites[i].demand}')
                # Return Instance class instance.
                return instance
        except:
            raise FileNotFoundError(f'File {file} not found!')
    
    def get_dist_matrix(sites: list) -> list:
        """
        A function to compute the distance matrix between sites.
        """
        # Initialize distance matrix.
        dist_matrix = [[0 for _ in range(len(sites))] for _ in range(len(sites))]
        # Compute distance matrix.
        for i in range(len(sites)):
            for j in range(len(sites)):
                dist_matrix[i][j] = round(math.sqrt((sites[i].x - sites[j].x)**2
                                                  + (sites[i].y - sites[j].y)**2),
                                         4)
        # Print distance matrix.
        # print('Distance matrix:')
        # for i in range(len(sites)):
        #     print(dist_matrix[i])
        # Return distance matrix.
        return dist_matrix