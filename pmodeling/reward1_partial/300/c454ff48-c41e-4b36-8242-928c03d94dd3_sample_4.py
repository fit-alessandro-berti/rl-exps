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

site_assess_permits = OperatorPOWL(operator=Operator.XOR, children=[site_assess, permit_obtain])
soil_soil_crops = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, crop_select])
irrigation_drainage = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, drainage_install])
energy_energy_staff = OperatorPOWL(operator=Operator.XOR, children=[energy_integrate, staff_train])
pest_logistics = OperatorPOWL(operator=Operator.XOR, children=[pest_control, logistics_plan])
supply_distribution = OperatorPOWL(operator=Operator.XOR, children=[supply_coordinate, distribution_map])
community_monitoring = OperatorPOWL(operator=Operator.XOR, children=[community_engage, monitoring_setup])
yield_yield = OperatorPOWL(operator=Operator.XOR, children=[yield_optimize, skip])

root = StrictPartialOrder(nodes=[site_assess_permits, soil_soil_crops, irrigation_drainage, energy_energy_staff, pest_logistics, supply_distribution, community_monitoring, yield_yield])
root.order.add_edge(site_assess_permits, soil_soil_crops)
root.order.add_edge(soil_soil_crops, irrigation_drainage)
root.order.add_edge(irrigation_drainage, energy_energy_staff)
root.order.add_edge(energy_energy_staff, pest_logistics)
root.order.add_edge(pest_logistics, supply_distribution)
root.order.add_edge(supply_distribution, community_monitoring)
root.order.add_edge(community_monitoring, yield_yield)