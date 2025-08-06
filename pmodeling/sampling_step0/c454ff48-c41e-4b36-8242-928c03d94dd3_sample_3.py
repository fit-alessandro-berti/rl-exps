import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.process_tree.obj import ProcessTree

# Define the activities
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

# Define the process tree
tree = ProcessTree()
tree.add_child(site_assess)
tree.add_child(permit_obtain)
tree.add_child(soil_testing)
tree.add_child(crop_select)
tree.add_child(irrigation_setup)
tree.add_child(drainage_install)
tree.add_child(energy_integrate)
tree.add_child(staff_train)
tree.add_child(pest_control)
tree.add_child(logistics_plan)
tree.add_child(supply_coordinate)
tree.add_child(distribution_map)
tree.add_child(community_engage)
tree.add_child(monitoring_setup)
tree.add_child(yield_optimize)

# Define the partial order
root = StrictPartialOrder(nodes=tree.nodes, order=tree.edges)

# Print the partial order
print(root)