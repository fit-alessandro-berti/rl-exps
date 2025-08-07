import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_acq     = Transition(label='Site Acquisition')
impact_assess= Transition(label='Impact Assess')
mod_setup    = Transition(label='Modular Setup')
crop_plant   = Transition(label='Crop Planting')
nutrient_ctrl= Transition(label='Nutrient Control')
pest_ctrl    = Transition(label='Pest Control')
growth_mon   = Transition(label='Growth Monitor')
community_eng= Transition(label='Community Engage')
yield_forest = Transition(label='Yield Forecast')
supply_coord = Transition(label='Supply Coordinate')
compliance_chk= Transition(label='Compliance Check')
waste_recycle= Transition(label='Waste Recycle')
energy_opt   = Transition(label='Energy Optimize')
market_strat = Transition(label='Market Strategy')
perf_review  = Transition(label='Performance Review')

# Loop for continuous monitoring and optimization
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_mon, nutrient_ctrl, pest_ctrl]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_acq,
    impact_assess,
    mod_setup,
    crop_plant,
    monitor_loop,
    community_eng,
    yield_forest,
    supply_coord,
    compliance_chk,
    waste_recycle,
    energy_opt,
    market_strat,
    perf_review
])

# Define the control-flow dependencies
root.order.add_edge(site_acq, impact_assess)
root.order.add_edge(impact_assess, mod_setup)
root.order.add_edge(mod_setup, crop_plant)
root.order.add_edge(crop_plant, monitor_loop)
root.order.add_edge(monitor_loop, community_eng)
root.order.add_edge(community_eng, yield_forest)
root.order.add_edge(yield_forest, supply_coord)
root.order.add_edge(supply_coord, compliance_chk)
root.order.add_edge(compliance_chk, waste_recycle)
root.order.add_edge(waste_recycle, energy_opt)
root.order.add_edge(energy_opt, market_strat)
root.order.add_edge(market_strat, perf_review)