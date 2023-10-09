import sys
from config.config import Config
from utils.data import Data
from utils.sisrs import SISRs

# Get name of instance file as first command line argument.
instance_file = sys.argv[1]

# Instantiate Config class instance.
config = Config()

# Read instance file and instantiate Data class instance.
sites = list()
tours = list()
instance = Data.read_instance_X(instance_file, sites)
dist_matrix = Data.get_dist_matrix(sites)

print(f'Instance: {instance.name}, with {instance.n} sites and '\
      f'capacity {instance.capacity}')
print(f'Sites has size {len(sites)}')

# Instantiate SISRs class instance.
sisrs = SISRs()

# Get initial solution.
sisrs.get_initial_sol(instance.capacity, dist_matrix, sites, tours)

# Print initial solution.
sisrs.print_sol(tours)