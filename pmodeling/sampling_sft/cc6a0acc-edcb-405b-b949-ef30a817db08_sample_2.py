import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
load_test       = Transition(label='Load Test')
soil_sample     = Transition(label='Soil Sample')
water_check     = Transition(label='Water Check')
design_plan     = Transition(label='Design Plan')
bed_setup       = Transition(label='Bed Setup')
irrigation_inst = Transition(label='Irrigation Install')
climate_setup   = Transition(label='Climate Setup')
seed_selection  = Transition(label='Seed Selection')
planting_phase  = Transition(label='Planting Phase')
pest_control    = Transition(label='Pest Control')
growth_monitor  = Transition(label='Growth Monitor')
harvest_prep    = Transition(label='Harvest Prep')
community_meet  = Transition(label='Community Meet')
waste_manage    = Transition(label='Waste Manage')
yield_report    = Transition(label='Yield Report')

# Loop for continuous growth monitoring and pest control
loop_body = StrictPartialOrder(nodes=[pest_control, growth_monitor])
loop_body.order.add_edge(pest_control, growth_monitor)

loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, waste_manage])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, soil_sample, water_check,
    design_plan, bed_setup, irrigation_inst, climate_setup,
    seed_selection, planting_phase, loop, community_meet,
    yield_report
])

# Sequential dependencies
root.order.add_edge(site_survey, load_test)
root.order.add_edge(load_test, soil_sample)
root.order.add_edge(soil_sample, water_check)
root.order.add_edge(water_check, design_plan)
root.order.add_edge(design_plan, bed_setup)
root.order.add_edge(bed_setup, irrigation_inst)
root.order.add_edge(irrigation_inst, climate_setup)
root.order.add_edge(climate_setup, seed_selection)
root.order.add_edge(seed_selection, planting_phase)
root.order.add_edge(planting_phase, loop)
root.order.add_edge(loop, community_meet)
root.order.add_edge(community_meet, yield_report)