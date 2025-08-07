import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_acq     = Transition(label='Site Acquisition')
impact_assess= Transition(label='Impact Assess')
modular_setup= Transition(label='Modular Setup')
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
performance_r= Transition(label='Performance Review')

# Define the inner loop body: Pest Control -> Growth Monitor -> Community Engage
inner_loop = StrictPartialOrder(nodes=[pest_ctrl, growth_mon, community_eng])
inner_loop.order.add_edge(pest_ctrl, growth_mon)
inner_loop.order.add_edge(growth_mon, community_eng)

# Define the loop: do Nutrient Control, then either exit or do the inner loop and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_ctrl, inner_loop])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_acq, impact_assess, modular_setup, crop_plant,
    loop, yield_forest, supply_coord, compliance_chk,
    waste_recycle, energy_opt, market_strat, performance_r
])

# Define the control-flow dependencies
root.order.add_edge(site_acq, impact_assess)
root.order.add_edge(impact_assess, modular_setup)
root.order.add_edge(modular_setup, crop_plant)
root.order.add_edge(crop_plant, loop)
root.order.add_edge(loop, yield_forest)
root.order.add_edge(yield_forest, supply_coord)
root.order.add_edge(supply_coord, compliance_chk)
root.order.add_edge(compliance_chk, waste_recycle)
root.order.add_edge(waste_recycle, energy_opt)
root.order.add_edge(energy_opt, market_strat)
root.order.add_edge(market_strat, performance_r)