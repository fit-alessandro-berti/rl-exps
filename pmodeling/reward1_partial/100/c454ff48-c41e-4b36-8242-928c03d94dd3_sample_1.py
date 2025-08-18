import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL model structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[permit_obtain, site_assess])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, crop_select])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, drainage_install])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[energy_integrate, staff_train])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, logistics_plan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[supply_coordinate, distribution_map])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[community_engage, monitoring_setup])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[yield_optimize])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Define the dependencies between activities
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

# Print the root POWL model
print(root)