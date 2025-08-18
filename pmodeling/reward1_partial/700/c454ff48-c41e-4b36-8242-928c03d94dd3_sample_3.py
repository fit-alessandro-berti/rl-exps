import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
site_assess = Transition(label='Site Assess')
permit_obtain = Transition(label='Permit Obtain')
soil_testing = Transition(label='Soil Testing')
crop_select = Transition(label='Crop Select')
irrigation_setup = Transition(label='Irrigation Setup')
drainage_install = Transition(label='Drainage Install')
energy_integrate = Transition(label='Energy Integrate')
staff_train = Transition(label='Staff Train')
pest_control = Transition(label='Pest Control')
logistics_plan = Transition(label='Logistics Plan')
supply_coordinate = Transition(label='Supply Coordinate')
distribution_map = Transition(label='Distribution Map')
community_engage = Transition(label='Community Engage')
monitoring_setup = Transition(label='Monitoring Setup')
yield_optimize = Transition(label='Yield Optimize')

# Define the loop and exclusive choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_assess, permit_obtain, soil_testing, crop_select, irrigation_setup, drainage_install, energy_integrate, staff_train, pest_control, logistics_plan, supply_coordinate, distribution_map, community_engage, monitoring_setup, yield_optimize])
xor = OperatorPOWL(operator=Operator.XOR, children=[monitoring_setup, yield_optimize])

# Create the root model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root model
print(root)