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

# Define silent transitions
skip = SilentTransition()

# Define the loop for continuous optimization cycles
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, skip])

# Define the exclusive choice for AI integration and system testing
xor = OperatorPOWL(operator=Operator.XOR, children=[ai_integration, system_testing])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])

# Define the order (dependencies) between nodes
root.order.add_edge(loop, xor)

# Print the root POWL model
print(root)