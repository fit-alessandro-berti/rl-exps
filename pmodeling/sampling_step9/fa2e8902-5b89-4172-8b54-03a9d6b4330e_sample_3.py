import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
nutrient_mix = Transition(label='Nutrient Mix')
climate_adjust = Transition(label='Climate Adjust')
light_scheduling = Transition(label='Light Scheduling')
pest_inspection = Transition(label='Pest Inspection')
bio_control = Transition(label='Bio Control')
growth_monitor = Transition(label='Growth Monitor')
water_recirc = Transition(label='Water Recirc')
harvest_plan = Transition(label='Harvest Plan')
yield_forecast = Transition(label='Yield Forecast')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
delivery_route = Transition(label='Delivery Route')
energy_audit = Transition(label='Energy Audit')
sustain_report = Transition(label='Sustain Report')

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, bio_control])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[water_recirc, quality_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, cold_storage])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[delivery_route, energy_audit])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[sustain_report, yield_forecast])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[germination_start, nutrient_mix])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, light_scheduling])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, harvest_plan])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, xor5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, xor5)
root.order.add_edge(xor5, loop5)
root.order.add_edge(loop5, xor5)

# Print the POWL model
print(root)