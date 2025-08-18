import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, light_scheduling, pest_inspection, bio_control, growth_monitor, water_recirc])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, quality_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, cold_storage, delivery_route])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, sustain_report])

root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)