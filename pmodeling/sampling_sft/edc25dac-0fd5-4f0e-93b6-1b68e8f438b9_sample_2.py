import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
load = Transition(label='Load Assess')
permit = Transition(label='Permit Review')
survey = Transition(label='Site Survey')
design = Transition(label='Design Layout')
soil = Transition(label='Soil Mix')
install = Transition(label='Install Beds')
irrigate = Transition(label='Irrigation Set')
climate = Transition(label='Climate Test')
sensor = Transition(label='Sensor Deploy')
energy = Transition(label='Energy Setup')
crop = Transition(label='Crop Select')
plant = Transition(label='Plant Seeding')
community = Transition(label='Community Meet')
compliance = Transition(label='Compliance Check')
growth = Transition(label='Growth Monitor')
harvest = Transition(label='Harvest Plan')
waste = Transition(label='Waste Recycle')

# Define the monitoring and adaptive loop: Growth Monitor then optionally Harvest Plan
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, harvest])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    load, permit, survey, design, soil, install, irrigate, climate,
    sensor, energy, crop, plant, community, compliance, monitor_loop, waste
])

# Define the control-flow dependencies
root.order.add_edge(load, survey)
root.order.add_edge(survey, design)
root.order.add_edge(design, soil)
root.order.add_edge(soil, install)
root.order.add_edge(install, irrigate)
root.order.add_edge(irrigate, climate)
root.order.add_edge(climate, sensor)
root.order.add_edge(sensor, energy)
root.order.add_edge(energy, crop)
root.order.add_edge(crop, plant)
root.order.add_edge(plant, community)
root.order.add_edge(community, compliance)
root.order.add_edge(compliance, monitor_loop)
root.order.add_edge(monitor_loop, waste)