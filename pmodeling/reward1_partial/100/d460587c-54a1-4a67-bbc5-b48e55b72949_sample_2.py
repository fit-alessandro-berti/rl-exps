from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
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

# Define the process steps
site_survey_then_permit_filing = OperatorPOWL(operator=Operator.XOR, children=[site_survey, permit_filing])
soil_sampling_then_water_testing = OperatorPOWL(operator=Operator.XOR, children=[soil_sampling, water_testing])
system_design_then_solar_setup = OperatorPOWL(operator=Operator.XOR, children=[system_design, solar_setup])
crop_planning_then_stakeholder_meet = OperatorPOWL(operator=Operator.XOR, children=[crop_planning, stakeholder_meet])
material_order_then_system_install = OperatorPOWL(operator=Operator.XOR, children=[material_order, system_install])
environmental_audit_then_growth_monitoring = OperatorPOWL(operator=Operator.XOR, children=[environmental_audit, growth_monitoring])
pest_control_then_market_launch = OperatorPOWL(operator=Operator.XOR, children=[pest_control, market_launch])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey_then_permit_filing, soil_sampling_then_water_testing, system_design_then_solar_setup, crop_planning_then_stakeholder_meet, material_order_then_system_install, environmental_audit_then_growth_monitoring, pest_control_then_market_launch])
root.order.add_edge(site_survey_then_permit_filing, soil_sampling_then_water_testing)
root.order.add_edge(site_survey_then_permit_filing, system_design_then_solar_setup)
root.order.add_edge(soil_sampling_then_water_testing, crop_planning_then_stakeholder_meet)
root.order.add_edge(system_design_then_solar_setup, material_order_then_system_install)
root.order.add_edge(material_order_then_system_install, environmental_audit_then_growth_monitoring)
root.order.add_edge(environmental_audit_then_growth_monitoring, pest_control_then_market_launch)

print(root)