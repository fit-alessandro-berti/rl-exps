import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
site_analysis = Transition(label='Site Analysis')
infrastructure_setup = Transition(label='Infrastructure Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_cycle = Transition(label='Planting Cycle')
climate_adjust = Transition(label='Climate Adjust')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvesting_mode = Transition(label='Harvesting Mode')
quality_check = Transition(label='Quality Check')
packaging_phase = Transition(label='Packaging Phase')
cold_storage = Transition(label='Cold Storage')
order_dispatch = Transition(label='Order Dispatch')
waste_recycling = Transition(label='Waste Recycling')
system_maintain = Transition(label='System Maintain')

# Define the exclusive choice for seed selection and nutrient mix
xor1 = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])

# Define the exclusive choice for pest control and growth monitor
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, growth_monitor])

# Define the exclusive choice for harvesting mode and quality check
xor3 = OperatorPOWL(operator=Operator.XOR, children=[harvesting_mode, quality_check])

# Define the exclusive choice for packaging phase and cold storage
xor4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_phase, cold_storage])

# Define the loop for waste recycling and system maintain
loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling, system_maintain])

# Define the root node with all the children
root = StrictPartialOrder(nodes=[site_analysis, infrastructure_setup, xor1, xor2, xor3, xor4, loop])

# Add the edges to connect the nodes
root.order.add_edge(site_analysis, infrastructure_setup)
root.order.add_edge(infrastructure_setup, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, loop)