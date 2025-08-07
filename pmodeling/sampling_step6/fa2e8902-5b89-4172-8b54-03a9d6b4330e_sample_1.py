import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) for the POWL model
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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    nutrient_mix,
    climate_adjust,
    light_scheduling,
    pest_inspection,
    bio_control,
    growth_monitor,
    water_recirc,
    harvest_plan,
    yield_forecast,
    quality_check,
    packaging_prep,
    cold_storage,
    delivery_route,
    energy_audit,
    sustain_report
])

# Add dependencies if any (not specified in the problem description)
# For example, if there is a dependency from 'Seed Selection' to 'Germination Start':
# root.order.add_edge(seed_selection, germination_start)

# The 'root' variable now contains the POWL model for the urban vertical farming facility process.