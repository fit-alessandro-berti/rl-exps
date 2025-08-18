from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
climate_sim = Transition(label='Climate Sim')
seed_select = Transition(label='Seed Select')
module_setup = Transition(label='Module Setup')
nutrient_mix = Transition(label='Nutrient Mix')
water_cycle = Transition(label='Water Cycle')
energy_link = Transition(label='Energy Link')
sensor_install = Transition(label='Sensor Install')
pest_detect = Transition(label='Pest Detect')
growth_scan = Transition(label='Growth Scan')
data_sync = Transition(label='Data Sync')
community_meet = Transition(label='Community Meet')
reg_compliance = Transition(label='Reg Compliance')
system_test = Transition(label='System Test')
maintenance_plan = Transition(label='Maintenance Plan')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_pest_detection = OperatorPOWL(operator=Operator.LOOP, children=[pest_detect, data_sync])
xor_data_sync = OperatorPOWL(operator=Operator.XOR, children=[data_sync, skip])
xor_reg_compliance = OperatorPOWL(operator=Operator.XOR, children=[reg_compliance, skip])
xor_community_meet = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
xor_system_test = OperatorPOWL(operator=Operator.XOR, children=[system_test, skip])
xor_maintenance_plan = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, skip])

root = StrictPartialOrder(nodes=[
    site_survey, system_design, climate_sim, seed_select, module_setup, nutrient_mix, water_cycle, energy_link,
    sensor_install, loop_pest_detection, xor_data_sync, xor_reg_compliance, xor_community_meet, xor_system_test,
    xor_maintenance_plan
])

# Add edges to the partial order
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, climate_sim)
root.order.add_edge(climate_sim, seed_select)
root.order.add_edge(seed_select, module_setup)
root.order.add_edge(module_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, water_cycle)
root.order.add_edge(water_cycle, energy_link)
root.order.add_edge(energy_link, sensor_install)
root.order.add_edge(sensor_install, loop_pest_detection)
root.order.add_edge(loop_pest_detection, xor_data_sync)
root.order.add_edge(xor_data_sync, xor_reg_compliance)
root.order.add_edge(xor_reg_compliance, xor_community_meet)
root.order.add_edge(xor_community_meet, xor_system_test)
root.order.add_edge(xor_system_test, xor_maintenance_plan)