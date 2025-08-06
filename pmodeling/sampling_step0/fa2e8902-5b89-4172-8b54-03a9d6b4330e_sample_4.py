import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, light_scheduling, pest_inspection, bio_control, growth_monitor, water_recirc])
hydroponics_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, climate_adjust, light_scheduling, pest_inspection, bio_control, growth_monitor, water_recirc])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, yield_forecast, quality_check, packaging_prep, cold_storage, delivery_route])

# Define XOR nodes
hydroponics_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_control_loop, hydroponics_loop])
harvest_xor = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_xor, harvest_loop])

# Define the root node
root = StrictPartialOrder(nodes=[seed_selection, germination_start, hydroponics_xor, harvest_xor, energy_audit, sustain_report])

# Define the partial order edges
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, hydroponics_xor)
root.order.add_edge(hydroponics_xor, harvest_xor)
root.order.add_edge(harvest_xor, energy_audit)
root.order.add_edge(energy_audit, sustain_report)

# Return the root node
return root