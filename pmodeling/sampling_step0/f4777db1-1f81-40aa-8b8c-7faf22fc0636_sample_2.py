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

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_prep, market_launch])
xor = OperatorPOWL(operator=Operator.XOR, children=[system_design, skip])
partial_order = StrictPartialOrder(nodes=[loop, xor])

# Define the dependencies
partial_order.order.add_edge(loop, xor)
partial_order.order.add_edge(xor, site_survey)
partial_order.order.add_edge(site_survey, impact_study)
partial_order.order.add_edge(impact_study, structure_check)
partial_order.order.add_edge(structure_check, soil_testing)
partial_order.order.add_edge(soil_testing, system_design)
partial_order.order.add_edge(system_design, seed_selection)
partial_order.order.add_edge(seed_selection, irrigation_setup)
partial_order.order.add_edge(irrigation_setup, lighting_install)
partial_order.order.add_edge(lighting_install, pest_control)
partial_order.order.add_edge(pest_control, community_meet)
partial_order.order.add_edge(community_meet, regulation_review)
partial_order.order.add_edge(regulation_review, waste_plan)
partial_order.order.add_edge(waste_plan, crop_monitor)
partial_order.order.add_edge(crop_monitor, harvest_prep)
partial_order.order.add_edge(harvest_prep, market_launch)

# Set the root of the POWL model
root = partial_order