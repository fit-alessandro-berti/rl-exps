import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Climate_Study = Transition(label='Climate Study')
Soil_Prep = Transition(label='Soil Prep')
Seed_Selection = Transition(label='Seed Selection')
Irrigation_Setup = Transition(label='Irrigation Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Install = Transition(label='Sensor Install')
Pest_Monitor = Transition(label='Pest Monitor')
Data_Analysis = Transition(label='Data Analysis')
Regulation_Review = Transition(label='Regulation Review')
Community_Meet = Transition(label='Community Meet')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Design = Transition(label='Packaging Design')
Distribution_Map = Transition(label='Distribution Map')
Feedback_Loop = Transition(label='Feedback Loop')
Maintenance_Schedule = Transition(label='Maintenance Schedule')

skip = SilentTransition()

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Structural_Check, Climate_Study, Soil_Prep])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[Seed_Selection, Irrigation_Setup, Nutrient_Mix])
sensor_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[Sensor_Install, Pest_Monitor, Data_Analysis])
regulation_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[Regulation_Review, Community_Meet, Harvest_Plan])
packaging_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Design, Distribution_Map])
feedback_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Maintenance_Schedule])

root = StrictPartialOrder(nodes=[site_survey_loop, seed_selection_loop, sensor_install_loop, regulation_review_loop, packaging_design_loop, feedback_loop_loop])
root.order.add_edge(site_survey_loop, seed_selection_loop)
root.order.add_edge(seed_selection_loop, sensor_install_loop)
root.order.add_edge(sensor_install_loop, regulation_review_loop)
root.order.add_edge(regulation_review_loop, packaging_design_loop)
root.order.add_edge(packaging_design_loop, feedback_loop_loop)

print(root)