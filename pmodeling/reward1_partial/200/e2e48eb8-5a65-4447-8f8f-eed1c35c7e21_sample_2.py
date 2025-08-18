import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
site_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_check, climate_study, soil_prep])
seed_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, irrigation_setup, nutrient_mix, sensor_install])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, data_analysis, regulation_review, community_meet])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, packaging_design, distribution_map, feedback_loop, maintenance_schedule])

# Define partial order
root = StrictPartialOrder(nodes=[site_loop, seed_loop, pest_loop, harvest_loop])
root.order.add_edge(site_loop, seed_loop)
root.order.add_edge(seed_loop, pest_loop)
root.order.add_edge(pest_loop, harvest_loop)

# Print the root POWL model
print(root)