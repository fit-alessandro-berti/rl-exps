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

# Define transitions
site_survey_to_impact_study = OperatorPOWL(operator=Operator.XOR, children=[structure_check, soil_testing])
impact_study_to_system_design = OperatorPOWL(operator=Operator.XOR, children=[system_design, site_survey_to_impact_study])
system_design_to_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, impact_study_to_system_design])
seed_selection_to_irrigation_setup = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, system_design_to_seed_selection])
irrigation_setup_to_lighting_install = OperatorPOWL(operator=Operator.XOR, children=[lighting_install, seed_selection_to_irrigation_setup])
lighting_install_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, irrigation_setup_to_lighting_install])
pest_control_to_community_meet = OperatorPOWL(operator=Operator.XOR, children=[community_meet, pest_control])
community_meet_to_regulation_review = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, community_meet])
regulation_review_to_waste_plan = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, regulation_review])
waste_plan_to_crop_monitor = OperatorPOWL(operator=Operator.XOR, children=[crop_monitor, waste_plan])
crop_monitor_to_harvest_prep = OperatorPOWL(operator=Operator.XOR, children=[harvest_prep, crop_monitor])
harvest_prep_to_market_launch = OperatorPOWL(operator=Operator.XOR, children=[market_launch, harvest_prep])

# Define loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, impact_study_to_system_design, seed_selection_to_irrigation_setup, lighting_install_to_pest_control, community_meet_to_regulation_review, waste_plan_to_crop_monitor, harvest_prep_to_market_launch])

# Define root
root = StrictPartialOrder(nodes=[loop, site_survey, impact_study_to_system_design, seed_selection_to_irrigation_setup, lighting_install_to_pest_control, community_meet_to_regulation_review, waste_plan_to_crop_monitor, harvest_prep_to_market_launch])
root.order.add_edge(loop, site_survey)
root.order.add_edge(loop, impact_study_to_system_design)
root.order.add_edge(loop, seed_selection_to_irrigation_setup)
root.order.add_edge(loop, lighting_install_to_pest_control)
root.order.add_edge(loop, community_meet_to_regulation_review)
root.order.add_edge(loop, waste_plan_to_crop_monitor)
root.order.add_edge(loop, harvest_prep_to_market_launch)

# Return root
return root