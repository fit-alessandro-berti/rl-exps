import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey       = Transition(label='Site Survey')
impact_study      = Transition(label='Impact Study')
structure_check   = Transition(label='Structure Check')
soil_testing      = Transition(label='Soil Testing')
system_design     = Transition(label='System Design')
seed_selection    = Transition(label='Seed Selection')
irrigation_setup  = Transition(label='Irrigation Setup')
lighting_install  = Transition(label='Lighting Install')
pest_control      = Transition(label='Pest Control')
community_meet    = Transition(label='Community Meet')
regulation_review = Transition(label='Regulation Review')
waste_plan        = Transition(label='Waste Plan')
crop_monitor      = Transition(label='Crop Monitor')
harvest_prep      = Transition(label='Harvest Prep')
market_launch     = Transition(label='Market Launch')

# Silent transition for loop exit
skip = SilentTransition()

# Loop: after each monitoring cycle, choose to exit or do another cycle
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_monitor, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, impact_study, structure_check, soil_testing, system_design,
    seed_selection, irrigation_setup, lighting_install, pest_control,
    community_meet, regulation_review, waste_plan,
    monitor_loop, harvest_prep, market_launch
])

# Sequence of activities before monitoring starts
root.order.add_edge(site_survey, impact_study)
root.order.add_edge(impact_study, structure_check)
root.order.add_edge(structure_check, soil_testing)
root.order.add_edge(soil_testing, system_design)
root.order.add_edge(system_design, seed_selection)
root.order.add_edge(seed_selection, irrigation_setup)
root.order.add_edge(irrigation_setup, lighting_install)
root.order.add_edge(lighting_install, pest_control)
root.order.add_edge(pest_control, community_meet)
root.order.add_edge(community_meet, regulation_review)
root.order.add_edge(regulation_review, waste_plan)

# After monitoring, either exit or do another cycle
root.order.add_edge(monitor_loop, harvest_prep)
root.order.add_edge(monitor_loop, market_launch)