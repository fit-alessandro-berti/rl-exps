import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the loop for nutrient mix and water recirculation
loop_nutrient_water = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, water_recirc])

# Define the XOR for pest inspection and bio control
xor_pest_bio = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, bio_control])

# Define the XOR for quality check and packaging prep
xor_quality_packaging = OperatorPOWL(operator=Operator.XOR, children=[quality_check, packaging_prep])

# Define the XOR for cold storage and delivery route
xor_cold_delivery = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, delivery_route])

# Define the XOR for energy audit and sustain report
xor_energy_sustain = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, sustain_report])

# Define the root node as a partial order
root = StrictPartialOrder(nodes=[loop_nutrient_water, xor_pest_bio, xor_quality_packaging, xor_cold_delivery, xor_energy_sustain])
root.order.add_edge(loop_nutrient_water, xor_pest_bio)
root.order.add_edge(loop_nutrient_water, xor_quality_packaging)
root.order.add_edge(xor_pest_bio, xor_cold_delivery)
root.order.add_edge(xor_quality_packaging, xor_cold_delivery)
root.order.add_edge(xor_pest_bio, xor_energy_sustain)
root.order.add_edge(xor_quality_packaging, xor_energy_sustain)

# Print the root node
print(root)