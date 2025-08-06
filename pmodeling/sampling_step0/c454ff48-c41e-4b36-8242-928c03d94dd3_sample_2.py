import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop_site_assess = OperatorPOWL(operator=Operator.LOOP, children=[site_assess, permit_obtain])
loop_energy_integrate = OperatorPOWL(operator=Operator.LOOP, children=[energy_integrate, pest_control])

xor_soil_testing_crop_select = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, crop_select])
xor_irrigation_setup_drainage_install = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, drainage_install])

xor_logistics_plan_supply_coordinate = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, supply_coordinate])
xor_distribution_map_community_engage = OperatorPOWL(operator=Operator.XOR, children=[distribution_map, community_engage])

xor_monitoring_setup_yield_optimize = OperatorPOWL(operator=Operator.XOR, children=[monitoring_setup, yield_optimize])

root = StrictPartialOrder(nodes=[loop_site_assess, xor_soil_testing_crop_select, loop_energy_integrate, xor_irrigation_setup_drainage_install, xor_logistics_plan_supply_coordinate, xor_distribution_map_community_engage, xor_monitoring_setup_yield_optimize])
root.order.add_edge(loop_site_assess, xor_soil_testing_crop_select)
root.order.add_edge(loop_site_assess, loop_energy_integrate)
root.order.add_edge(xor_soil_testing_crop_select, xor_irrigation_setup_drainage_install)
root.order.add_edge(xor_irrigation_setup_drainage_install, xor_logistics_plan_supply_coordinate)
root.order.add_edge(xor_logistics_plan_supply_coordinate, xor_distribution_map_community_engage)
root.order.add_edge(xor_distribution_map_community_engage, xor_monitoring_setup_yield_optimize)

return root