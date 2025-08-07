import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection   = Transition(label='Seed Selection')
germination      = Transition(label='Germination Start')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_adjust   = Transition(label='Climate Adjust')
light_scheduling = Transition(label='Light Scheduling')
pest_inspect     = Transition(label='Pest Inspection')
bio_control      = Transition(label='Bio Control')
growth_monitor   = Transition(label='Growth Monitor')
water_recirc     = Transition(label='Water Recirc')
harvest_plan     = Transition(label='Harvest Plan')
yield_forecast   = Transition(label='Yield Forecast')
quality_check    = Transition(label='Quality Check')
packaging_prep   = Transition(label='Packaging Prep')
cold_storage     = Transition(label='Cold Storage')
delivery_route   = Transition(label='Delivery Route')
energy_audit     = Transition(label='Energy Audit')
sustain_report   = Transition(label='Sustain Report')

# Loop for continuous monitoring and adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, water_recirc, climate_adjust, light_scheduling]
)

# Sequence for nutrient mix and pest bio control
nutrient_seq = StrictPartialOrder(nodes=[nutrient_mix, pest_inspect, bio_control])
nutrient_seq.order.add_edge(nutrient_mix, pest_inspect)
nutrient_seq.order.add_edge(pest_inspect, bio_control)

# Main production partial order
production_po = StrictPartialOrder(nodes=[
    seed_selection,
    germination,
    nutrient_seq,
    monitor_loop,
    harvest_plan,
    yield_forecast,
    quality_check,
    packaging_prep,
    cold_storage,
    delivery_route
])
production_po.order.add_edge(seed_selection, germination)
production_po.order.add_edge(germination, nutrient_seq)
production_po.order.add_edge(nutrient_seq, monitor_loop)
production_po.order.add_edge(monitor_loop, harvest_plan)
production_po.order.add_edge(harvest_plan, yield_forecast)
production_po.order.add_edge(yield_forecast, quality_check)
production_po.order.add_edge(quality_check, packaging_prep)
production_po.order.add_edge(packaging_prep, cold_storage)
production_po.order.add_edge(cold_storage, delivery_route)

# Final loop for continuous energy audit and sustainability reporting
sustain_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[energy_audit, sustain_report]
)

# Root partial order combining both production and sustainability loops
root = StrictPartialOrder(nodes=[production_po, sustain_loop])
root.order.add_edge(production_po, sustain_loop)