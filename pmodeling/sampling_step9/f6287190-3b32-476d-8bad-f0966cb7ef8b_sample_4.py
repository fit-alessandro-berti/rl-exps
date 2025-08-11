import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition
skip = SilentTransition()

# Define the loops and exclusive choices
loop_nutrient = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, sensor_check, light_adjust, water_cycle])
loop_pest = OperatorPOWL(operator=Operator.LOOP, children=[pest_scan, growth_audit])
loop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, demand_sync, quality_grade, pack_items])
loop_waste = OperatorPOWL(operator=Operator.LOOP, children=[waste_compost, data_review, cycle_reset])

# Define the exclusive choice between loop_nutrient and loop_pest
xor_nutrient_pest = OperatorPOWL(operator=Operator.XOR, children=[loop_nutrient, loop_pest])

# Define the root process
root = StrictPartialOrder(nodes=[xor_nutrient_pest, loop_harvest, loop_waste])
root.order.add_edge(xor_nutrient_pest, loop_harvest)
root.order.add_edge(xor_nutrient_pest, loop_waste)