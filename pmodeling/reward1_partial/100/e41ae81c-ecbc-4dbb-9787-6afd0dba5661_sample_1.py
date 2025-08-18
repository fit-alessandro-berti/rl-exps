import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for system testing and staff training
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[system_testing, staff_training])

# Define the loop for pest control and waste recycling
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, waste_recycle])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, structure_reinforce, hydroponic_setup, climate_install, ai_integration, seed_sourcing, nutrient_prep, exclusive_choice, crop_planting, growth_monitor, loop, market_dispatch, quality_check])

# Define the dependencies between nodes
root.order.add_edge(site_survey, structure_reinforce)
root.order.add_edge(structure_reinforce, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_install)
root.order.add_edge(climate_install, ai_integration)
root.order.add_edge(ai_integration, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(nutrient_prep, exclusive_choice)
root.order.add_edge(exclusive_choice, crop_planting)
root.order.add_edge(crop_planting, growth_monitor)
root.order.add_edge(growth_monitor, loop)
root.order.add_edge(loop, market_dispatch)
root.order.add_edge(market_dispatch, quality_check)

# Print the final result
print(root)