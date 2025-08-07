import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection     = Transition(label='Seed Selection')
germination_start  = Transition(label='Germination Start')
nutrient_mix       = Transition(label='Nutrient Mix')
climate_adjust     = Transition(label='Climate Adjust')
light_scheduling   = Transition(label='Light Scheduling')
pest_inspection    = Transition(label='Pest Inspection')
bio_control        = Transition(label='Bio Control')
growth_monitor     = Transition(label='Growth Monitor')
water_recirc       = Transition(label='Water Recirc')
harvest_plan       = Transition(label='Harvest Plan')
yield_forecast     = Transition(label='Yield Forecast')
quality_check      = Transition(label='Quality Check')
packaging_prep     = Transition(label='Packaging Prep')
cold_storage       = Transition(label='Cold Storage')
delivery_route     = Transition(label='Delivery Route')
energy_audit       = Transition(label='Energy Audit')
sustain_report     = Transition(label='Sustain Report')

# Loop for continuous monitoring and adjustment during growth
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, water_recirc]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    nutrient_mix,
    climate_adjust,
    light_scheduling,
    pest_inspection,
    bio_control,
    growth_loop,
    harvest_plan,
    yield_forecast,
    quality_check,
    packaging_prep,
    cold_storage,
    delivery_route,
    energy_audit,
    sustain_report
])

# Define the control‐flow dependencies
root.order.add_edge(seed_selection,    germination_start)
root.order.add_edge(germination_start, nutrient_mix)
root.order.add_edge(germination_start, climate_adjust)
root.order.add_edge(germination_start, light_scheduling)
root.order.add_edge(nutrient_mix,      growth_loop)
root.order.add_edge(climate_adjust,    growth_loop)
root.order.add_edge(light_scheduling,  growth_loop)
root.order.add_edge(growth_loop,       pest_inspection)
root.order.add_edge(pest_inspection,   bio_control)
root.order.add_edge(bio_control,       harvest_plan)
root.order.add_edge(harvest_plan,      yield_forecast)
root.order.add_edge(harvest_plan,      quality_check)
root.order.add_edge(harvest_plan,      packaging_prep)
root.order.add_edge(quality_check,     cold_storage)
root.order.add_edge(packaging_prep,    cold_storage)
root.order.add_edge(cold_storage,      delivery_route)
root.order.add_edge(delivery_route,    energy_audit)
root.order.add_edge(energy_audit,      sustain_report)