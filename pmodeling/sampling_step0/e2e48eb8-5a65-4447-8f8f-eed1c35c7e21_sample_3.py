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

# Define loop and choice operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_check, climate_study])
xor = OperatorPOWL(operator=Operator.XOR, children=[soil_prep, seed_selection])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, nutrient_mix])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, pest_monitor])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, regulation_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[community_meet, harvest_plan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, distribution_map])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, maintenance_schedule])

# Define root partial order
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

# Save the final result in the variable 'root'