import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
climate_study = Transition(label='Climate Study')
soil_prep = Transition(label='Soil Prep')
seed_selection = Transition(label='Seed Selection')
irrigation_setup = Transition(label='Irrigation Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
pest_monitor = Transition(label='Pest Monitor')
data_analysis = Transition(label='Data Analysis')
regulation_review = Transition(label='Regulation Review')
community_meet = Transition(label='Community Meet')
harvest_plan = Transition(label='Harvest Plan')
packaging_design = Transition(label='Packaging Design')
distribution_map = Transition(label='Distribution Map')
feedback_loop = Transition(label='Feedback Loop')
maintenance_schedule = Transition(label='Maintenance Schedule')

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, structural_check, climate_study, soil_prep, seed_selection, irrigation_setup, nutrient_mix, sensor_install, pest_monitor, data_analysis, regulation_review, community_meet, harvest_plan, packaging_design, distribution_map, feedback_loop, maintenance_schedule])

# Add dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(site_survey, soil_prep)
root.order.add_edge(site_survey, seed_selection)
root.order.add_edge(site_survey, irrigation_setup)
root.order.add_edge(site_survey, nutrient_mix)
root.order.add_edge(site_survey, sensor_install)
root.order.add_edge(site_survey, pest_monitor)
root.order.add_edge(site_survey, data_analysis)
root.order.add_edge(site_survey, regulation_review)
root.order.add_edge(site_survey, community_meet)
root.order.add_edge(site_survey, harvest_plan)
root.order.add_edge(site_survey, packaging_design)
root.order.add_edge(site_survey, distribution_map)
root.order.add_edge(site_survey, feedback_loop)
root.order.add_edge(site_survey, maintenance_schedule)

# Print the root to see the complete process
print(root)