import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_acq     = Transition(label='Site Acquisition')
impact_assess= Transition(label='Impact Assess')
modular_setup= Transition(label='Modular Setup')
crop_plant   = Transition(label='Crop Planting')
nutrient_ctrl= Transition(label='Nutrient Control')
pest_control = Transition(label='Pest Control')
growth_mon   = Transition(label='Growth Monitor')
community_engage= Transition(label='Community Engage')
yield_forecast= Transition(label='Yield Forecast')
supply_coord  = Transition(label='Supply Coordinate')
compliance_check= Transition(label='Compliance Check')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize= Transition(label='Energy Optimize')
market_strategy= Transition(label='Market Strategy')
performance_review= Transition(label='Performance Review')

# Build the main growth process: Planting -> Nutrient Control -> Pest Control -> Growth Monitor
growth_seq = StrictPartialOrder(nodes=[
    crop_plant, nutrient_ctrl, pest_control, growth_mon
])
growth_seq.order.add_edge(crop_plant, nutrient_ctrl)
growth_seq.order.add_edge(nutrient_ctrl, pest_control)
growth_seq.order.add_edge(pest_control, growth_mon)

# Loop for continuous monitoring: repeat Growth Monitor and then either exit or re-enter
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_mon, growth_seq]
)

# Assemble the full root partial order
root = StrictPartialOrder(nodes=[
    site_acq, impact_assess, modular_setup,
    monitor_loop,
    community_engage,
    yield_forecast,
    supply_coord,
    compliance_check,
    waste_recycle,
    energy_optimize,
    market_strategy,
    performance_review
])

# Define the control-flow dependencies
root.order.add_edge(site_acq, impact_assess)
root.order.add_edge(impact_assess, modular_setup)
root.order.add_edge(modular_setup, monitor_loop)
root.order.add_edge(monitor_loop, community_engage)
root.order.add_edge(community_engage, yield_forecast)
root.order.add_edge(yield_forecast, supply_coord)
root.order.add_edge(supply_coord, compliance_check)
root.order.add_edge(compliance_check, waste_recycle)
root.order.add_edge(waste_recycle, energy_optimize)
root.order.add_edge(energy_optimize, market_strategy)
root.order.add_edge(market_strategy, performance_review)