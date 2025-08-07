import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
load_test         = Transition(label='Load Test')
soil_sample       = Transition(label='Soil Sample')
water_check       = Transition(label='Water Check')
design_plan       = Transition(label='Design Plan')
bed_setup         = Transition(label='Bed Setup')
irrigation_install= Transition(label='Irrigation Install')
climate_setup     = Transition(label='Climate Setup')
seed_selection    = Transition(label='Seed Selection')
planting_phase    = Transition(label='Planting Phase')
pest_control      = Transition(label='Pest Control')
growth_monitor    = Transition(label='Growth Monitor')
harvest_prep      = Transition(label='Harvest Prep')
community_meet    = Transition(label='Community Meet')
waste_manage      = Transition(label='Waste Manage')
yield_report      = Transition(label='Yield Report')

# Loop for continuous growth monitoring and pest control
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, soil_sample, water_check,
    design_plan, bed_setup, irrigation_install, climate_setup,
    seed_selection, planting_phase, monitor_loop,
    community_meet, waste_manage, yield_report
])

# Define the control-flow edges
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, soil_sample)
root.order.add_edge(site_survey, water_check)
root.order.add_edge(load_test, design_plan)
root.order.add_edge(soil_sample, design_plan)
root.order.add_edge(water_check, design_plan)
root.order.add_edge(design_plan, bed_setup)
root.order.add_edge(bed_setup, irrigation_install)
root.order.add_edge(bed_setup, climate_setup)
root.order.add_edge(irrigation_install, planting_phase)
root.order.add_edge(climate_setup, planting_phase)
root.order.add_edge(planting_phase, monitor_loop)
root.order.add_edge(monitor_loop, community_meet)
root.order.add_edge(community_meet, waste_manage)
root.order.add_edge(community_meet, yield_report)