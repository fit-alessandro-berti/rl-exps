import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions
skip = SilentTransition()

# Define loop for soil and water testing
soil_water_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_sampling, water_testing])

# Define xor for crop planning and skip
crop_planning_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planning, skip])

# Define xor for system design and solar setup
system_design_solar_xor = OperatorPOWL(operator=Operator.XOR, children=[system_design, solar_setup])

# Define xor for stakeholder meet and material order
stakeholder_meet_material_order_xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, material_order])

# Define xor for system install and environmental audit
system_install_environmental_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, environmental_audit])

# Define xor for growth monitoring and pest control
growth_monitoring_pest_control_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, pest_control])

# Define xor for pest control and market launch
pest_control_market_launch_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, market_launch])

# Define root POWL model
root = StrictPartialOrder(nodes=[site_survey, permit_filing, load_testing, soil_water_loop, crop_planning_xor, system_design_solar_xor, stakeholder_meet_material_order_xor, system_install_environmental_audit_xor, growth_monitoring_pest_control_xor, pest_control_market_launch_xor])
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, load_testing)
root.order.add_edge(load_testing, soil_water_loop)
root.order.add_edge(soil_water_loop, crop_planning_xor)
root.order.add_edge(crop_planning_xor, system_design_solar_xor)
root.order.add_edge(system_design_solar_xor, stakeholder_meet_material_order_xor)
root.order.add_edge(stakeholder_meet_material_order_xor, system_install_environmental_audit_xor)
root.order.add_edge(system_install_environmental_audit_xor, growth_monitoring_pest_control_xor)
root.order.add_edge(growth_monitoring_pest_control_xor, pest_control_market_launch_xor)