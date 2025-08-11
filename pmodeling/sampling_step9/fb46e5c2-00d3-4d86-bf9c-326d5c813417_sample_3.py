import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
site_analysis = Transition(label='Site Analysis')
impact_review = Transition(label='Impact Review')
modular_design = Transition(label='Modular Design')
system_integration = Transition(label='System Integration')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
light_config = Transition(label='Light Config')
staff_training = Transition(label='Staff Training')
pest_monitor = Transition(label='Pest Monitor')
drone_deploy = Transition(label='Drone Deploy')
health_scan = Transition(label='Health Scan')
data_logging = Transition(label='Data Logging')
supply_sync = Transition(label='Supply Sync')
maintenance_plan = Transition(label='Maintenance Plan')
waste_manage = Transition(label='Waste Manage')

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix, light_config])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, drone_deploy, health_scan, data_logging])
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync, maintenance_plan, waste_manage])

# Define the exclusive choice
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[maintenance_loop, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[climate_loop, pest_loop, staff_training, exclusive_choice])
root.order.add_edge(climate_loop, pest_loop)
root.order.add_edge(climate_loop, staff_training)
root.order.add_edge(pest_loop, staff_training)
root.order.add_edge(exclusive_choice, staff_training)

# Print the root POWL model
print(root)