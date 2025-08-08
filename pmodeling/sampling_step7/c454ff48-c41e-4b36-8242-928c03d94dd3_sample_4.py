import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
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

# Create the partial order
root = StrictPartialOrder(nodes=[site_assess, permit_obtain, soil_testing, crop_select, irrigation_setup, drainage_install, energy_integrate, staff_train, pest_control, logistics_plan, supply_coordinate, distribution_map, community_engage, monitoring_setup, yield_optimize])

# Define the order between activities
root.order.add_edge(site_assess, permit_obtain)
root.order.add_edge(permit_obtain, soil_testing)
root.order.add_edge(soil_testing, crop_select)
root.order.add_edge(crop_select, irrigation_setup)
root.order.add_edge(irrigation_setup, drainage_install)
root.order.add_edge(drainage_install, energy_integrate)
root.order.add_edge(energy_integrate, staff_train)
root.order.add_edge(staff_train, pest_control)
root.order.add_edge(pest_control, logistics_plan)
root.order.add_edge(logistics_plan, supply_coordinate)
root.order.add_edge(supply_coordinate, distribution_map)
root.order.add_edge(distribution_map, community_engage)
root.order.add_edge(community_engage, monitoring_setup)
root.order.add_edge(monitoring_setup, yield_optimize)

# Print the result
print(root)