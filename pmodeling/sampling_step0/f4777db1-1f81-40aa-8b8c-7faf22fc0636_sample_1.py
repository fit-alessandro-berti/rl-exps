import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the process tree operators
xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_design, seed_selection, irrigation_setup, lighting_install, pest_control])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[crop_monitor, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[harvest_prep, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[market_launch, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, impact_study, structure_check, soil_testing, xor, loop, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(site_survey, impact_study)
root.order.add_edge(impact_study, structure_check)
root.order.add_edge(structure_check, soil_testing)
root.order.add_edge(soil_testing, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, market_launch)

print(root)