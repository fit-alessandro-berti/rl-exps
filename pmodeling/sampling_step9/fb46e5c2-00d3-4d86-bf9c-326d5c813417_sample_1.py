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

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix, light_config])
xor = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, drone_deploy])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[health_scan, data_logging])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, maintenance_plan])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)

# Save the final result in the variable 'root'