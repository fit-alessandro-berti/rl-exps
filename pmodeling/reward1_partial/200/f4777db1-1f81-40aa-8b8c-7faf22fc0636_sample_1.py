import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Impact Study', 'Structure Check', 'Soil Testing', 'System Design', 'Seed Selection', 'Irrigation Setup', 'Lighting Install', 'Pest Control', 'Community Meet', 'Regulation Review', 'Waste Plan', 'Crop Monitor', 'Harvest Prep', 'Market Launch']
activities_transitions = [Transition(label=activity) for activity in activities]

# Define the process structure
site_survey = activities_transitions[0]
impact_study = activities_transitions[1]
structure_check = activities_transitions[2]
soil_testing = activities_transitions[3]
system_design = activities_transitions[4]
seed_selection = activities_transitions[5]
irrigation_setup = activities_transitions[6]
lighting_install = activities_transitions[7]
pest_control = activities_transitions[8]
community_meet = activities_transitions[9]
regulation_review = activities_transitions[10]
waste_plan = activities_transitions[11]
crop_monitor = activities_transitions[12]
harvest_prep = activities_transitions[13]
market_launch = activities_transitions[14]

# Define the process flow
root = StrictPartialOrder(nodes=[site_survey, impact_study, structure_check, soil_testing, system_design, seed_selection, irrigation_setup, lighting_install, pest_control, community_meet, regulation_review, waste_plan, crop_monitor, harvest_prep, market_launch])
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
root.order.add_edge(waste_plan, crop_monitor)
root.order.add_edge(crop_monitor, harvest_prep)
root.order.add_edge(harvest_prep, market_launch)

# Print the result
print(root)