from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop and XOR nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, light_scheduling])
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, bio_control])

# Define the root node with its dependencies
root = StrictPartialOrder(nodes=[seed_selection, germination_start, nutrient_mix, loop, xor, water_recirc, harvest_plan, yield_forecast, quality_check, packaging_prep, cold_storage, delivery_route, energy_audit, sustain_report])
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, nutrient_mix)
root.order.add_edge(nutrient_mix, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, water_recirc)
root.order.add_edge(water_recirc, harvest_plan)
root.order.add_edge(harvest_plan, yield_forecast)
root.order.add_edge(yield_forecast, quality_check)
root.order.add_edge(quality_check, packaging_prep)
root.order.add_edge(packaging_prep, cold_storage)
root.order.add_edge(cold_storage, delivery_route)
root.order.add_edge(delivery_route, energy_audit)
root.order.add_edge(energy_audit, sustain_report)

print(root)