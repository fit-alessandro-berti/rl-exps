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

# Define the loop for the planting cycle
loop_planting = OperatorPOWL(operator=Operator.LOOP, children=[planting_cycle, pest_control])

# Define the XOR for the harvesting mode
xor_harvesting = OperatorPOWL(operator=Operator.XOR, children=[harvesting_mode, skip])

# Define the loop for the growth monitor
loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, climate_adjust])

# Define the XOR for the nutrient mix
xor_nutrient = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the loop for the quality check
loop_quality = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, waste_recycling])

# Define the loop for the packaging phase
loop_packaging = OperatorPOWL(operator=Operator.LOOP, children=[packaging_phase, system_maintain])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_analysis, infrastructure_setup, seed_selection, xor_nutrient, loop_planting,
    xor_harvesting, loop_growth, loop_quality, loop_packaging, order_dispatch, cold_storage
])

# Add edges to the POWL model
root.order.add_edge(site_analysis, infrastructure_setup)
root.order.add_edge(infrastructure_setup, seed_selection)
root.order.add_edge(seed_selection, xor_nutrient)
root.order.add_edge(xor_nutrient, loop_planting)
root.order.add_edge(loop_planting, xor_harvesting)
root.order.add_edge(xor_harvesting, loop_growth)
root.order.add_edge(loop_growth, loop_quality)
root.order.add_edge(loop_quality, loop_packaging)
root.order.add_edge(loop_packaging, order_dispatch)
root.order.add_edge(order_dispatch, cold_storage)

print(root)