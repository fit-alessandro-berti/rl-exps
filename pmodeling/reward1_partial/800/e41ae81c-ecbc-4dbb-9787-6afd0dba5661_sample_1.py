import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop nodes
structure_loop = OperatorPOWL(operator=Operator.LOOP, children=[structure_reinforce, hydroponic_setup])
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_install, ai_integration])
seed_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_sourcing, nutrient_prep])
system_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_testing, staff_training])
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting, growth_monitor, pest_control, harvest_schedule, quality_check, market_dispatch])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, data_analysis])

# Define partial order
root = StrictPartialOrder(nodes=[structure_loop, climate_loop, seed_sourcing_loop, system_loop, crop_loop, waste_loop])

# Define dependencies
root.order.add_edge(structure_loop, climate_loop)
root.order.add_edge(climate_loop, seed_sourcing_loop)
root.order.add_edge(seed_sourcing_loop, system_loop)
root.order.add_edge(system_loop, crop_loop)
root.order.add_edge(crop_loop, waste_loop)

# Print the root
print(root)