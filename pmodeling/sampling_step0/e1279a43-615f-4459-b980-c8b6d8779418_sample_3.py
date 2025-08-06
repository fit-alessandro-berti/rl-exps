import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL model
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, infrastructure_setup])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[planting_cycle, climate_adjust])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[harvesting_mode, quality_check])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[packaging_phase, cold_storage])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[order_dispatch, waste_recycling])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[system_maintain, waste_recycling])

root = StrictPartialOrder(nodes=[loop_1, xor_1, loop_2, xor_2, loop_3, xor_3, loop_4, xor_4])
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(xor_1, loop_2)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(xor_2, loop_3)
root.order.add_edge(loop_3, xor_3)
root.order.add_edge(xor_3, loop_4)
root.order.add_edge(loop_4, xor_4)
root.order.add_edge(xor_4, loop_1)