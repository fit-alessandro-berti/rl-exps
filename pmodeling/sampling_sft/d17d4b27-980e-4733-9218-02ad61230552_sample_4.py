import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_analysis   = Transition(label='Site Analysis')
zoning_review   = Transition(label='Zoning Review')
modular_design  = Transition(label='Modular Design')
climate_setup   = Transition(label='Climate Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
seed_selection  = Transition(label='Seed Selection')
ai_monitoring   = Transition(label='AI Monitoring')
lighting_control= Transition(label='Lighting Control')
energy_audit    = Transition(label='Energy Audit')
water_reclaim   = Transition(label='Water Reclaim')
waste_sorting   = Transition(label='Waste Sorting')
community_meet  = Transition(label='Community Meet')
staff_training  = Transition(label='Staff Training')
yield_forecast  = Transition(label='Yield Forecast')
market_sync     = Transition(label='Market Sync')
supply_chain    = Transition(label='Supply Chain')

# Define the loop for continuous monitoring and control
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ai_monitoring, lighting_control]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    zoning_review,
    modular_design,
    climate_setup,
    nutrient_mix,
    seed_selection,
    monitoring_loop,
    energy_audit,
    water_reclaim,
    waste_sorting,
    community_meet,
    staff_training,
    yield_forecast,
    market_sync,
    supply_chain
])

# Define the control‐flow dependencies
root.order.add_edge(site_analysis, zoning_review)
root.order.add_edge(zoning_review, modular_design)
root.order.add_edge(modular_design, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, monitoring_loop)
root.order.add_edge(monitoring_loop, energy_audit)
root.order.add_edge(monitoring_loop, water_reclaim)
root.order.add_edge(monitoring_loop, waste_sorting)
root.order.add_edge(energy_audit, yield_forecast)
root.order.add_edge(water_reclaim, yield_forecast)
root.order.add_edge(waste_sorting, yield_forecast)
root.order.add_edge(yield_forecast, market_sync)
root.order.add_edge(market_sync, supply_chain)
root.order.add_edge(yield_forecast, community_meet)
root.order.add_edge(yield_forecast, staff_training)