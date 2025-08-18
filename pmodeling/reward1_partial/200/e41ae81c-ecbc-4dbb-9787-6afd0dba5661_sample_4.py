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

# Define loops and choices
structure_loop = OperatorPOWL(operator=Operator.LOOP, children=[structure_reinforce])
hydroponic_loop = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, climate_install, ai_integration])
seed_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_sourcing, nutrient_prep, system_testing])
staff_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, crop_planting, growth_monitor])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, harvest_schedule, quality_check])
market_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_dispatch, waste_recycle, data_analysis])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[structure_loop, hydroponic_loop, seed_loop, staff_loop, pest_loop, market_loop])
root.order.add_edge(structure_loop, hydroponic_loop)
root.order.add_edge(hydroponic_loop, seed_loop)
root.order.add_edge(seed_loop, staff_loop)
root.order.add_edge(staff_loop, pest_loop)
root.order.add_edge(pest_loop, market_loop)

# Print the root of the POWL model
print(root)