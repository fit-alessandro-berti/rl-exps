import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
setup = Transition(label='Planting Setup')
climate = Transition(label='Climate Control')
water = Transition(label='Water Cycling')
light = Transition(label='Light Adjustment')
growth = Transition(label='Growth Monitoring')
pest = Transition(label='Pest Detection')
analysis = Transition(label='Data Analysis')
harvest = Transition(label='Harvest Planning')
crop = Transition(label='Crop Harvest')
sort = Transition(label='Yield Sorting')
pack = Transition(label='Packaging Prep')
dist = Transition(label='Distribution Plan')
reg_check = Transition(label='Regulation Check')
waste = Transition(label='Waste Recycling')
maint = Transition(label='System Maintenance')

# Loop for continuous monitoring and data analysis
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth, analysis]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed, nutrient, setup,
    climate, water, light,
    monitor_loop,
    harvest, sort,
    pack, dist,
    reg_check, waste, maint
])

# Define the control-flow dependencies
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, setup)
root.order.add_edge(setup, climate)
root.order.add_edge(setup, water)
root.order.add_edge(setup, light)

# After setup, enter the monitoring loop
root.order.add_edge(climate, monitor_loop)
root.order.add_edge(water, monitor_loop)
root.order.add_edge(light, monitor_loop)

# After monitoring, decide on harvest or maintenance
root.order.add_edge(monitor_loop, harvest)
root.order.add_edge(monitor_loop, maint)

# Harvest leads to sorting, packaging, and distribution
root.order.add_edge(harvest, sort)
root.order.add_edge(sort, pack)
root.order.add_edge(pack, dist)

# Maintenance then either repeat monitoring or exit with regulation check
root.order.add_edge(maint, monitor_loop)
root.order.add_edge(maint, reg_check)

# Regulation check then waste recycling, then maintenance again
root.order.add_edge(reg_check, waste)
root.order.add_edge(waste, maint)