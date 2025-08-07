import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_analysis       = Transition(label='Site Analysis')
design_layout       = Transition(label='Design Layout')
module_assembly     = Transition(label='Module Assembly')
climate_setup       = Transition(label='Climate Setup')
sensor_install      = Transition(label='Sensor Install')
water_testing       = Transition(label='Water Testing')
nutrient_mix        = Transition(label='Nutrient Mix')
seed_selection      = Transition(label='Seed Selection')
planting_phase      = Transition(label='Planting Phase')
growth_monitor      = Transition(label='Growth Monitor')
pest_control        = Transition(label='Pest Control')
harvest_plan        = Transition(label='Harvest Plan')
yield_audit         = Transition(label='Yield Audit')
packaging_prep      = Transition(label='Packaging Prep')
market_delivery     = Transition(label='Market Delivery')
waste_recycling     = Transition(label='Waste Recycling')

# Define the operational cycle as a partial order
cycle = StrictPartialOrder(nodes=[
    planting_phase, growth_monitor, pest_control,
    harvest_plan, yield_audit, packaging_prep, market_delivery, waste_recycling
])
cycle.order.add_edge(planting_phase, growth_monitor)
cycle.order.add_edge(growth_monitor, pest_control)
cycle.order.add_edge(pest_control, harvest_plan)
cycle.order.add_edge(harvest_plan, yield_audit)
cycle.order.add_edge(yield_audit, packaging_prep)
cycle.order.add_edge(packaging_prep, market_delivery)
cycle.order.add_edge(market_delivery, waste_recycling)

# Define the overall workflow as a loop: analyze -> design -> assemble -> setup -> monitor cycle
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, design_layout, module_assembly, climate_setup, sensor_install, water_testing, nutrient_mix, seed_selection, cycle])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[loop])
# No additional edges needed as the loop covers all sub‐steps