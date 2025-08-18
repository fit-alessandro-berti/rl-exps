import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL transitions
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
pest_scan = Transition(label='Pest Scan')
light_control = Transition(label='Light Control')
growth_monitor = Transition(label='Growth Monitor')
water_cycle = Transition(label='Water Cycle')
air_quality = Transition(label='Air Quality')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check = Transition(label='Quality Check')
data_logging = Transition(label='Data Logging')
packaging = Transition(label='Packaging')
waste_sort = Transition(label='Waste Sort')
energy_audit = Transition(label='Energy Audit')
retail_sync = Transition(label='Retail Sync')

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, environment_setup])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[light_control, water_cycle])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[air_quality, nutrient_mix])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, growth_monitor])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_logging, quality_check])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[packaging, waste_sort])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, retail_sync])

# Define the partial order
root = StrictPartialOrder(nodes=[seed_selection, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(seed_selection, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)