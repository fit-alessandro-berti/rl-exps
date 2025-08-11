import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
seed_select = Transition(label='Seed Select')
climate_map = Transition(label='Climate Map')
iot_setup = Transition(label='IoT Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_check = Transition(label='Sensor Check')
light_adjust = Transition(label='Light Adjust')
water_cycle = Transition(label='Water Cycle')
pest_scan = Transition(label='Pest Scan')
growth_audit = Transition(label='Growth Audit')
harvest_plan = Transition(label='Harvest Plan')
demand_sync = Transition(label='Demand Sync')
quality_grade = Transition(label='Quality Grade')
pack_items = Transition(label='Pack Items')
waste_compost = Transition(label='Waste Compost')
data_review = Transition(label='Data Review')
cycle_reset = Transition(label='Cycle Reset')

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the exclusive choice nodes (XOR)
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, sensor_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[light_adjust, water_cycle])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[growth_audit, harvest_plan])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[quality_grade, pack_items])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_compost, data_review])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[climate_map, iot_setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, xor1])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor2, xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor4, xor5])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop1)

# Print the root model
print(root)