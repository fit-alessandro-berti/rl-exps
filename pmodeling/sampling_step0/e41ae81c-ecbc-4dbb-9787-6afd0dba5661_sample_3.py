import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
structure_reinforce = Transition(label='Structure Reinforce')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_install = Transition(label='Climate Install')
ai_integration = Transition(label='AI Integration')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_prep = Transition(label='Nutrient Prep')
system_testing = Transition(label='System Testing')
staff_training = Transition(label='Staff Training')
crop_planting = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_schedule = Transition(label='Harvest Schedule')
quality_check = Transition(label='Quality Check')
market_dispatch = Transition(label='Market Dispatch')
waste_recycle = Transition(label='Waste Recycle')
data_analysis = Transition(label='Data Analysis')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, climate_install, ai_integration, system_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seed_sourcing, nutrient_prep, staff_training, crop_planting])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control, harvest_schedule, quality_check])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[market_dispatch, waste_recycle, data_analysis])

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])

# Define the root node
root = StrictPartialOrder(nodes=[site_survey, xor1, xor2, xor3, xor4])
root.order.add_edge(site_survey, xor1)
root.order.add_edge(site_survey, xor2)
root.order.add_edge(site_survey, xor3)
root.order.add_edge(site_survey, xor4)

print(root)