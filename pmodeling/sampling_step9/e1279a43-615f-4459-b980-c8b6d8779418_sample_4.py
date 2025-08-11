import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, planting_cycle])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, growth_monitor, pest_control])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[harvesting_mode, quality_check])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_phase, cold_storage])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[order_dispatch, waste_recycling])

# Define the partial order
root = StrictPartialOrder(nodes=[site_analysis, infrastructure_setup, seed_selection, loop_1, loop_2, loop_3, loop_4, loop_5, system_maintain])

# Add edges to the partial order
root.order.add_edge(site_analysis, infrastructure_setup)
root.order.add_edge(site_analysis, seed_selection)
root.order.add_edge(infrastructure_setup, loop_1)
root.order.add_edge(seed_selection, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)
root.order.add_edge(loop_4, loop_5)
root.order.add_edge(loop_5, system_maintain)

print(root)