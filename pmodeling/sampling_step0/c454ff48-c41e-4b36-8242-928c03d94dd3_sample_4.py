import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the choices
site_assess_permit = OperatorPOWL(operator=Operator.XOR, children=[site_assess, permit_obtain])
soil_testing_crop = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, crop_select])
irrigation_drainage = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, drainage_install])
energy_logistics = OperatorPOWL(operator=Operator.XOR, children=[energy_integrate, logistics_plan])
staff_pest = OperatorPOWL(operator=Operator.XOR, children=[staff_train, pest_control])
supply_distribution = OperatorPOWL(operator=Operator.XOR, children=[supply_coordinate, distribution_map])
community_monitor = OperatorPOWL(operator=Operator.XOR, children=[community_engage, monitoring_setup])
optimize_yield = OperatorPOWL(operator=Operator.XOR, children=[yield_optimize, None])

# Define the loops
site_assess_permit_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_assess_permit])
soil_testing_crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing_crop])
irrigation_drainage_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_drainage])
energy_logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_logistics])
staff_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_pest])
supply_distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_distribution])
community_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_monitor])
optimize_yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[optimize_yield])

# Define the root
root = StrictPartialOrder(nodes=[
    site_assess_permit_loop,
    soil_testing_crop_loop,
    irrigation_drainage_loop,
    energy_logistics_loop,
    staff_pest_loop,
    supply_distribution_loop,
    community_monitor_loop,
    optimize_yield_loop
])

# Add edges to the root
root.order.add_edge(site_assess_permit_loop, soil_testing_crop_loop)
root.order.add_edge(site_assess_permit_loop, irrigation_drainage_loop)
root.order.add_edge(site_assess_permit_loop, energy_logistics_loop)
root.order.add_edge(site_assess_permit_loop, staff_pest_loop)
root.order.add_edge(site_assess_permit_loop, supply_distribution_loop)
root.order.add_edge(site_assess_permit_loop, community_monitor_loop)
root.order.add_edge(site_assess_permit_loop, optimize_yield_loop)
root.order.add_edge(soil_testing_crop_loop, irrigation_drainage_loop)
root.order.add_edge(soil_testing_crop_loop, energy_logistics_loop)
root.order.add_edge(soil_testing_crop_loop, staff_pest_loop)
root.order.add_edge(soil_testing_crop_loop, supply_distribution_loop)
root.order.add_edge(soil_testing_crop_loop, community_monitor_loop)
root.order.add_edge(soil_testing_crop_loop, optimize_yield_loop)
root.order.add_edge(irrigation_drainage_loop, energy_logistics_loop)
root.order.add_edge(irrigation_drainage_loop, staff_pest_loop)
root.order.add_edge(irrigation_drainage_loop, supply_distribution_loop)
root.order.add_edge(irrigation_drainage_loop, community_monitor_loop)
root.order.add_edge(irrigation_drainage_loop, optimize_yield_loop)
root.order.add_edge(energy_logistics_loop, staff_pest_loop)
root.order.add_edge(energy_logistics_loop, supply_distribution_loop)
root.order.add_edge(energy_logistics_loop, community_monitor_loop)
root.order.add_edge(energy_logistics_loop, optimize_yield_loop)
root.order.add_edge(staff_pest_loop, supply_distribution_loop)
root.order.add_edge(staff_pest_loop, community_monitor_loop)
root.order.add_edge(staff_pest_loop, optimize_yield_loop)
root.order.add_edge(supply_distribution_loop, community_monitor_loop)
root.order.add_edge(supply_distribution_loop, optimize_yield_loop)
root.order.add_edge(community_monitor_loop, optimize_yield_loop)

print(root)