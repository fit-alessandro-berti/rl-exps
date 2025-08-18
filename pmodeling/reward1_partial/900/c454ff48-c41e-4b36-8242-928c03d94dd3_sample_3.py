import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[site_assess, permit_obtain])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, crop_select])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup, drainage_install])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[energy_integrate, staff_train])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, logistics_plan])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[supply_coordinate, distribution_map])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[community_engage, monitoring_setup])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[yield_optimize, ])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor, loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(xor, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)

# Add silent transitions if needed