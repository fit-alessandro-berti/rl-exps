import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_analysis     = Transition(label='Site Analysis')
zoning_review     = Transition(label='Zoning Review')
modular_design    = Transition(label='Modular Design')
climate_setup     = Transition(label='Climate Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
seed_selection    = Transition(label='Seed Selection')
ai_monitoring     = Transition(label='AI Monitoring')
lighting_control  = Transition(label='Lighting Control')
energy_audit      = Transition(label='Energy Audit')
water_reclaim     = Transition(label='Water Reclaim')
waste_sorting     = Transition(label='Waste Sorting')
community_meet    = Transition(label='Community Meet')
staff_training    = Transition(label='Staff Training')
yield_forecast    = Transition(label='Yield Forecast')
market_sync       = Transition(label='Market Sync')
supply_chain      = Transition(label='Supply Chain')

# Define the loop for ongoing monitoring and adjustments
# Body A: AI Monitoring, Lighting Control, Energy Audit, Water Reclaim, Waste Sorting
body_A = StrictPartialOrder(nodes=[ai_monitoring, lighting_control, energy_audit, water_reclaim, waste_sorting])
# Body B: repeat A
body_B = StrictPartialOrder(nodes=[body_A])
body_B.order.add_edge(body_A, body_B)

# Loop: Site Analysis -> Zoning Review -> Modular Design -> Climate Setup -> Nutrient Mix -> Seed Selection -> LOOP(A)
loop = OperatorPOWL(operator=Operator.LOOP, children=[body_A, body_B])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis, zoning_review, modular_design, climate_setup, nutrient_mix, seed_selection,
    loop, community_meet, staff_training, yield_forecast, market_sync, supply_chain
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis, zoning_review)
root.order.add_edge(zoning_review, modular_design)
root.order.add_edge(modular_design, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, loop)
root.order.add_edge(loop, community_meet)
root.order.add_edge(loop, staff_training)
root.order.add_edge(community_meet, yield_forecast)
root.order.add_edge(community_meet, market_sync)
root.order.add_edge(community_meet, supply_chain)
root.order.add_edge(staff_training, yield_forecast)
root.order.add_edge(staff_training, market_sync)
root.order.add_edge(staff_training, supply_chain)