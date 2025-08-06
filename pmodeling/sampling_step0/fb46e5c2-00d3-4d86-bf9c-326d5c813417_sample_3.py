import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loop and choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, impact_review, modular_design, system_integration, climate_setup, nutrient_mix, light_config, staff_training, pest_monitor, drone_deploy, health_scan, data_logging, supply_sync, maintenance_plan, waste_manage])
xor = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, waste_manage])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Save the final result in the variable 'root'