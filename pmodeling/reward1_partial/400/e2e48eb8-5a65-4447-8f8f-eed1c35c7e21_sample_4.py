import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
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

# Define the relationships between activities
site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_check])
climate_study_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_study, soil_prep])
seed_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, irrigation_setup])
nutrient_mix_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, nutrient_mix])
sensor_install_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, pest_monitor])
data_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, regulation_review])
community_meet_choice = OperatorPOWL(operator=Operator.XOR, children=[community_meet, harvest_plan])
packaging_design_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, distribution_map])
feedback_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, maintenance_schedule])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey_choice, climate_study_choice, seed_selection_choice, nutrient_mix_choice, sensor_install_choice, data_analysis_choice, community_meet_choice, packaging_design_choice, feedback_loop_choice])
root.order.add_edge(site_survey_choice, climate_study_choice)
root.order.add_edge(climate_study_choice, soil_prep)
root.order.add_edge(soil_prep, seed_selection_choice)
root.order.add_edge(seed_selection_choice, irrigation_setup)
root.order.add_edge(irrigation_setup, nutrient_mix_choice)
root.order.add_edge(nutrient_mix_choice, sensor_install_choice)
root.order.add_edge(sensor_install_choice, pest_monitor)
root.order.add_edge(pest_monitor, data_analysis_choice)
root.order.add_edge(data_analysis_choice, regulation_review)
root.order.add_edge(regulation_review, community_meet_choice)
root.order.add_edge(community_meet_choice, harvest_plan)
root.order.add_edge(harvest_plan, packaging_design_choice)
root.order.add_edge(packaging_design_choice, distribution_map)
root.order.add_edge(distribution_map, feedback_loop_choice)
root.order.add_edge(feedback_loop_choice, maintenance_schedule)

print(root)