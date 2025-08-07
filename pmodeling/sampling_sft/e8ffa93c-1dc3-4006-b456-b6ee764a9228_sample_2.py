import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey      = Transition(label='Site Survey')
env_analysis     = Transition(label='Env Analysis')
structure_build  = Transition(label='Structure Build')
hydroponics_fit  = Transition(label='Hydroponics Fit')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_setup    = Transition(label='Climate Setup')
energy_audit     = Transition(label='Energy Audit')
crop_select      = Transition(label='Crop Select')
pest_control     = Transition(label='Pest Control')
growth_monitor   = Transition(label='Growth Monitor')
harvest_plan     = Transition(label='Harvest Plan')
waste_recycle    = Transition(label='Waste Recycle')
community_meet   = Transition(label='Community Meet')
supply_sync      = Transition(label='Supply Sync')
data_review      = Transition(label='Data Review')

# Build the main linear workflow
linear_workflow = StrictPartialOrder(nodes=[
    site_survey, env_analysis, structure_build,
    hydroponics_fit, nutrient_mix, climate_setup,
    energy_audit, crop_select, pest_control,
    growth_monitor, harvest_plan, waste_recycle,
    community_meet, supply_sync, data_review
])

# Define the control-flow dependencies
linear_workflow.order.add_edge(site_survey, env_analysis)
linear_workflow.order.add_edge(env_analysis, structure_build)
linear_workflow.order.add_edge(structure_build, hydroponics_fit)
linear_workflow.order.add_edge(hydroponics_fit, nutrient_mix)
linear_workflow.order.add_edge(nutrient_mix, climate_setup)
linear_workflow.order.add_edge(climate_setup, energy_audit)
linear_workflow.order.add_edge(energy_audit, crop_select)
linear_workflow.order.add_edge(crop_select, pest_control)
linear_workflow.order.add_edge(pest_control, growth_monitor)
linear_workflow.order.add_edge(growth_monitor, harvest_plan)
linear_workflow.order.add_edge(harvest_plan, waste_recycle)
linear_workflow.order.add_edge(waste_recycle, community_meet)
linear_workflow.order.add_edge(community_meet, supply_sync)
linear_workflow.order.add_edge(supply_sync, data_review)

# Final root node is the data review at the end of the linear workflow
root = data_review