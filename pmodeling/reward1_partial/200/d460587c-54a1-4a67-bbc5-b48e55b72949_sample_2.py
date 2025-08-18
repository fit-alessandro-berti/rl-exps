from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
load_testing = Transition(label='Load Testing')
soil_sampling = Transition(label='Soil Sampling')
water_testing = Transition(label='Water Testing')
system_design = Transition(label='System Design')
solar_setup = Transition(label='Solar Setup')
crop_planning = Transition(label='Crop Planning')
stakeholder_meet = Transition(label='Stakeholder Meet')
material_order = Transition(label='Material Order')
system_install = Transition(label='System Install')
environmental_audit = Transition(label='Environmental Audit')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
market_launch = Transition(label='Market Launch')

# Define the loop for system installation and environmental audit
system_install_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_install, environmental_audit])

# Define the XOR for material order and solar setup
xor_material_order_solar_setup = OperatorPOWL(operator=Operator.XOR, children=[material_order, solar_setup])

# Define the root node with the defined activities and loop
root = StrictPartialOrder(nodes=[site_survey, permit_filing, load_testing, soil_sampling, water_testing, system_design, xor_material_order_solar_setup, crop_planning, stakeholder_meet, system_install_audit_loop, growth_monitoring, pest_control, market_launch])
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, load_testing)
root.order.add_edge(load_testing, soil_sampling)
root.order.add_edge(soil_sampling, water_testing)
root.order.add_edge(water_testing, system_design)
root.order.add_edge(system_design, xor_material_order_solar_setup)
root.order.add_edge(xor_material_order_solar_setup, crop_planning)
root.order.add_edge(crop_planning, stakeholder_meet)
root.order.add_edge(stakeholder_meet, system_install_audit_loop)
root.order.add_edge(system_install_audit_loop, growth_monitoring)
root.order.add_edge(growth_monitoring, pest_control)
root.order.add_edge(pest_control, market_launch)

print(root)