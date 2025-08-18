from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_assembly = Transition(label='System Assembly')
climate_setup = Transition(label='Climate Setup')
light_calibration = Transition(label='Light Calibration')
seed_selection = Transition(label='Seed Selection')
seedling_prep = Transition(label='Seedling Prep')
nutrient_mix = Transition(label='Nutrient Mix')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
data_integration = Transition(label='Data Integration')
waste_routing = Transition(label='Waste Routing')
energy_audit = Transition(label='Energy Audit')
regulation_check = Transition(label='Regulation Check')
operational_test = Transition(label='Operational Test')
community_outreach = Transition(label='Community Outreach')

# Define the process steps
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, system_assembly])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, light_calibration, seed_selection])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[seedling_prep, nutrient_mix, irrigation_setup])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, data_integration, waste_routing])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, regulation_check])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[operational_test, community_outreach])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)

# Print the final result
print(root)