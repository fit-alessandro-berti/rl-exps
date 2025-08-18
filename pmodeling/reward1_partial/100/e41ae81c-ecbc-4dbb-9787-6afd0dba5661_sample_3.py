import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the loop nodes and exclusive choices
loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting, quality_check])
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, waste_recycle])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[market_dispatch, data_analysis])

# Define the root partial order
root = StrictPartialOrder(nodes=[site_survey, structure_reinforce, hydroponic_setup, climate_install, ai_integration, seed_sourcing, nutrient_prep, system_testing, staff_training, loop, xor, xor2])
root.order.add_edge(site_survey, structure_reinforce)
root.order.add_edge(structure_reinforce, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_install)
root.order.add_edge(climate_install, ai_integration)
root.order.add_edge(ai_integration, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(nutrient_prep, system_testing)
root.order.add_edge(system_testing, staff_training)
root.order.add_edge(staff_training, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor, xor2)

# Print the final result
print(root)