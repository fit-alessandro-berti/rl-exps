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

# Define the partial order model
root = StrictPartialOrder()

# Seed Selection
root.add_transition(seed_selection)

# Germination Start
root.add_transition(germination_start)
root.add_edge(seed_selection, germination_start)

# Nutrient Mix
root.add_transition(nutrient_mix)
root.add_edge(germination_start, nutrient_mix)

# Climate Adjust
root.add_transition(climate_adjust)
root.add_edge(nutrient_mix, climate_adjust)

# Light Scheduling
root.add_transition(light_scheduling)
root.add_edge(climate_adjust, light_scheduling)

# Pest Inspection
root.add_transition(pest_inspection)
root.add_edge(light_scheduling, pest_inspection)

# Bio Control
root.add_transition(bio_control)
root.add_edge(pest_inspection, bio_control)

# Growth Monitor
root.add_transition(growth_monitor)
root.add_edge(bio_control, growth_monitor)

# Water Recirc
root.add_transition(water_recirc)
root.add_edge(growth_monitor, water_recirc)

# Harvest Plan
root.add_transition(harvest_plan)
root.add_edge(water_recirc, harvest_plan)

# Yield Forecast
root.add_transition(yield_forecast)
root.add_edge(harvest_plan, yield_forecast)

# Quality Check
root.add_transition(quality_check)
root.add_edge(yield_forecast, quality_check)

# Packaging Prep
root.add_transition(packaging_prep)
root.add_edge(quality_check, packaging_prep)

# Cold Storage
root.add_transition(cold_storage)
root.add_edge(packaging_prep, cold_storage)

# Delivery Route
root.add_transition(delivery_route)
root.add_edge(cold_storage, delivery_route)

# Energy Audit
root.add_transition(energy_audit)
root.add_edge(delivery_route, energy_audit)

# Sustain Report
root.add_transition(sustain_report)
root.add_edge(energy_audit, sustain_report)