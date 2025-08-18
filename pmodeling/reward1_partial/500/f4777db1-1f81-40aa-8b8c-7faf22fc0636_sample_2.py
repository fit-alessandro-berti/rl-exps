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

# Define exclusive choices
community_meet_xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet])
regulation_review_xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_review])
waste_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_plan])

# Define loop for ongoing monitoring and crop health checks
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_monitor, harvest_prep])

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    impact_study,
    structure_check,
    soil_testing,
    system_design,
    seed_selection,
    irrigation_setup,
    lighting_install,
    pest_control,
    community_meet_xor,
    regulation_review_xor,
    waste_plan_xor,
    monitor_loop,
    market_launch
])

# Connect the nodes appropriately
root.order.add_edge(site_survey, impact_study)
root.order.add_edge(impact_study, structure_check)
root.order.add_edge(structure_check, soil_testing)
root.order.add_edge(soil_testing, system_design)
root.order.add_edge(system_design, seed_selection)
root.order.add_edge(seed_selection, irrigation_setup)
root.order.add_edge(irrigation_setup, lighting_install)
root.order.add_edge(lighting_install, pest_control)
root.order.add_edge(pest_control, community_meet_xor)
root.order.add_edge(community_meet_xor, regulation_review_xor)
root.order.add_edge(regulation_review_xor, waste_plan_xor)
root.order.add_edge(waste_plan_xor, monitor_loop)
root.order.add_edge(monitor_loop, market_launch)

print(root)