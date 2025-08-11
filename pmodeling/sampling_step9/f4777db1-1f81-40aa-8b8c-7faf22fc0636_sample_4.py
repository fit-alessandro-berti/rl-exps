import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loop nodes
site_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[structure_check, impact_study])
soil_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, system_design])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, irrigation_setup])
lighting_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[lighting_install, pest_control])
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, regulation_review])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_plan, crop_monitor])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_prep, market_launch])

# Define exclusive choices
site_check_xor = OperatorPOWL(operator=Operator.XOR, children=[site_check_loop, skip])
soil_testing_xor = OperatorPOWL(operator=Operator.XOR, children=[soil_testing_loop, skip])
seed_selection_xor = OperatorPOWL(operator=Operator.XOR, children=[seed_selection_loop, skip])
lighting_install_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_install_loop, skip])
community_xor = OperatorPOWL(operator=Operator.XOR, children=[community_loop, skip])
waste_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_loop, skip])
harvest_xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_loop, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[site_check_xor, soil_testing_xor, seed_selection_xor, lighting_install_xor, community_xor, waste_xor, harvest_xor])
root.order.add_edge(site_check_xor, soil_testing_xor)
root.order.add_edge(soil_testing_xor, seed_selection_xor)
root.order.add_edge(seed_selection_xor, lighting_install_xor)
root.order.add_edge(lighting_install_xor, community_xor)
root.order.add_edge(community_xor, waste_xor)
root.order.add_edge(waste_xor, harvest_xor)

print(root)