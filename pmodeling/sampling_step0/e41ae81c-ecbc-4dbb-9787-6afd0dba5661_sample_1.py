import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, nutrient_prep])
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_testing, staff_training])
choice1 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, waste_recycle])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, market_dispatch])

# Define the root node of the POWL model
root = StrictPartialOrder(nodes=[site_survey, structure_reinforce, hydroponic_setup, climate_install, ai_integration, exclusive_choice, loop, choice1, choice2, choice3])
root.order.add_edge(site_survey, structure_reinforce)
root.order.add_edge(site_survey, hydroponic_setup)
root.order.add_edge(site_survey, climate_install)
root.order.add_edge(site_survey, ai_integration)
root.order.add_edge(structure_reinforce, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_install)
root.order.add_edge(climate_install, ai_integration)
root.order.add_edge(ai_integration, exclusive_choice)
root.order.add_edge(exclusive_choice, system_testing)
root.order.add_edge(exclusive_choice, staff_training)
root.order.add_edge(system_testing, staff_training)
root.order.add_edge(system_testing, growth_monitor)
root.order.add_edge(system_testing, pest_control)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, quality_check)
root.order.add_edge(pest_control, waste_recycle)
root.order.add_edge(quality_check, waste_recycle)
root.order.add_edge(waste_recycle, data_analysis)
root.order.add_edge(data_analysis, market_dispatch)
root.order.add_edge(market_dispatch, choice3)
root.order.add_edge(choice1, choice3)
root.order.add_edge(choice2, choice3)

# Print the POWL model
print(root)