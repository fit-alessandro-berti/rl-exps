import pm4py
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

# Define the loop for nutrient mix and water recirc
loop_nutrient_mix_water_recirc = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, water_recirc])

# Define the choice for pest inspection and bio control
xor_pest_inspection_bio_control = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, bio_control])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    loop_nutrient_mix_water_recirc,
    xor_pest_inspection_bio_control,
    growth_monitor,
    harvest_plan,
    yield_forecast,
    quality_check,
    packaging_prep,
    cold_storage,
    delivery_route,
    energy_audit,
    sustain_report
])

# Add dependencies (source --> target)
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, loop_nutrient_mix_water_recirc)
root.order.add_edge(loop_nutrient_mix_water_recirc, xor_pest_inspection_bio_control)
root.order.add_edge(xor_pest_inspection_bio_control, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, yield_forecast)
root.order.add_edge(yield_forecast, quality_check)
root.order.add_edge(quality_check, packaging_prep)
root.order.add_edge(packaging_prep, cold_storage)
root.order.add_edge(cold_storage, delivery_route)
root.order.add_edge(delivery_route, energy_audit)
root.order.add_edge(energy_audit, sustain_report)

print(root)