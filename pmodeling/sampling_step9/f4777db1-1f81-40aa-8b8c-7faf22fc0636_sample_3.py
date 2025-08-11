import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loops
structure_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[structure_check])
soil_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing])
system_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_design])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection])
irrigation_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup])
lighting_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[lighting_install])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
community_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet])
regulation_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_review])
waste_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_plan])
crop_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_monitor])
harvest_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_prep])
market_launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_launch])

# Define exclusive choices
impact_study_xor = OperatorPOWL(operator=Operator.XOR, children=[impact_study, skip])
structure_check_xor = OperatorPOWL(operator=Operator.XOR, children=[structure_check_loop, skip])
soil_testing_xor = OperatorPOWL(operator=Operator.XOR, children=[soil_testing_loop, skip])
system_design_xor = OperatorPOWL(operator=Operator.XOR, children=[system_design_loop, skip])
seed_selection_xor = OperatorPOWL(operator=Operator.XOR, children=[seed_selection_loop, skip])
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup_loop, skip])
lighting_install_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_install_loop, skip])
pest_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control_loop, skip])
community_meet_xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet_loop, skip])
regulation_review_xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_review_loop, skip])
waste_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_plan_loop, skip])
crop_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_monitor_loop, skip])
harvest_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_prep_loop, skip])
market_launch_xor = OperatorPOWL(operator=Operator.XOR, children=[market_launch_loop, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[impact_study_xor, structure_check_xor, soil_testing_xor, system_design_xor, seed_selection_xor, irrigation_setup_xor, lighting_install_xor, pest_control_xor, community_meet_xor, regulation_review_xor, waste_plan_xor, crop_monitor_xor, harvest_prep_xor, market_launch_xor])
root.order.add_edge(impact_study_xor, structure_check_xor)
root.order.add_edge(structure_check_xor, soil_testing_xor)
root.order.add_edge(soil_testing_xor, system_design_xor)
root.order.add_edge(system_design_xor, seed_selection_xor)
root.order.add_edge(seed_selection_xor, irrigation_setup_xor)
root.order.add_edge(irrigation_setup_xor, lighting_install_xor)
root.order.add_edge(lighting_install_xor, pest_control_xor)
root.order.add_edge(pest_control_xor, community_meet_xor)
root.order.add_edge(community_meet_xor, regulation_review_xor)
root.order.add_edge(regulation_review_xor, waste_plan_xor)
root.order.add_edge(waste_plan_xor, crop_monitor_xor)
root.order.add_edge(crop_monitor_xor, harvest_prep_xor)
root.order.add_edge(harvest_prep_xor, market_launch_xor)

# Print the root POWL model
print(root)