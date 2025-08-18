import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
impact_study = Transition(label='Impact Study')
structure_check = Transition(label='Structure Check')
soil_testing = Transition(label='Soil Testing')
system_design = Transition(label='System Design')
seed_selection = Transition(label='Seed Selection')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_install = Transition(label='Lighting Install')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
regulation_review = Transition(label='Regulation Review')
waste_plan = Transition(label='Waste Plan')
crop_monitor = Transition(label='Crop Monitor')
harvest_prep = Transition(label='Harvest Prep')
market_launch = Transition(label='Market Launch')

skip = SilentTransition()

# Site Survey
site_survey_node = site_survey

# Impact Study
impact_study_node = impact_study

# Structure Check
structure_check_node = structure_check

# Soil Testing
soil_testing_node = soil_testing

# System Design
system_design_node = system_design

# Seed Selection
seed_selection_node = seed_selection

# Irrigation Setup
irrigation_setup_node = irrigation_setup

# Lighting Install
lighting_install_node = lighting_install

# Pest Control
pest_control_node = pest_control

# Community Meet
community_meet_node = community_meet

# Regulation Review
regulation_review_node = regulation_review

# Waste Plan
waste_plan_node = waste_plan

# Crop Monitor
crop_monitor_node = crop_monitor

# Harvest Prep
harvest_prep_node = harvest_prep

# Market Launch
market_launch_node = market_launch

# Build the POWL model
root = StrictPartialOrder(nodes=[
    site_survey_node,
    impact_study_node,
    structure_check_node,
    soil_testing_node,
    system_design_node,
    seed_selection_node,
    irrigation_setup_node,
    lighting_install_node,
    pest_control_node,
    community_meet_node,
    regulation_review_node,
    waste_plan_node,
    crop_monitor_node,
    harvest_prep_node,
    market_launch_node
])

# Define dependencies
root.order.add_edge(site_survey_node, impact_study_node)
root.order.add_edge(impact_study_node, structure_check_node)
root.order.add_edge(structure_check_node, soil_testing_node)
root.order.add_edge(soil_testing_node, system_design_node)
root.order.add_edge(system_design_node, seed_selection_node)
root.order.add_edge(seed_selection_node, irrigation_setup_node)
root.order.add_edge(irrigation_setup_node, lighting_install_node)
root.order.add_edge(lighting_install_node, pest_control_node)
root.order.add_edge(pest_control_node, community_meet_node)
root.order.add_edge(community_meet_node, regulation_review_node)
root.order.add_edge(regulation_review_node, waste_plan_node)
root.order.add_edge(waste_plan_node, crop_monitor_node)
root.order.add_edge(crop_monitor_node, harvest_prep_node)
root.order.add_edge(harvest_prep_node, market_launch_node)

print(root)