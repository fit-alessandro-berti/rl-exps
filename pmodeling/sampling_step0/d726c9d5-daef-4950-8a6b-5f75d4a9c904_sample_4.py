import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
soil_sample = Transition(label='Soil Sample')
water_test = Transition(label='Water Test')
crop_selection = Transition(label='Crop Selection')
material_order = Transition(label='Material Order')
planter_setup = Transition(label='Planter Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
solar_setup = Transition(label='Solar Setup')
data_integration = Transition(label='Data Integration')
community_meet = Transition(label='Community Meet')
training_session = Transition(label='Training Session')
yield_monitor = Transition(label='Yield Monitor')
adjust_plan = Transition(label='Adjust Plan')

# Define silent activities
skip = SilentTransition()

# Define loop nodes
loop_structure_check = OperatorPOWL(operator=Operator.LOOP, children=[structure_check])
loop_soil_sample = OperatorPOWL(operator=Operator.LOOP, children=[soil_sample])
loop_water_test = OperatorPOWL(operator=Operator.LOOP, children=[water_test])
loop_crop_selection = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection])
loop_material_order = OperatorPOWL(operator=Operator.LOOP, children=[material_order])
loop_planter_setup = OperatorPOWL(operator=Operator.LOOP, children=[planter_setup])
loop_irrigation_install = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_install])
loop_sensor_deploy = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy])
loop_solar_setup = OperatorPOWL(operator=Operator.LOOP, children=[solar_setup])
loop_data_integration = OperatorPOWL(operator=Operator.LOOP, children=[data_integration])
loop_community_meet = OperatorPOWL(operator=Operator.LOOP, children=[community_meet])
loop_training_session = OperatorPOWL(operator=Operator.LOOP, children=[training_session])
loop_yield_monitor = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitor])
loop_adjust_plan = OperatorPOWL(operator=Operator.LOOP, children=[adjust_plan])

# Define exclusive choice nodes
xor_structure_check_soil_sample = OperatorPOWL(operator=Operator.XOR, children=[structure_check, skip])
xor_water_test_crop_selection = OperatorPOWL(operator=Operator.XOR, children=[water_test, skip])
xor_material_order_planter_setup = OperatorPOWL(operator=Operator.XOR, children=[material_order, skip])
xor_irrigation_install_sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[irrigation_install, skip])
xor_solar_setup_data_integration = OperatorPOWL(operator=Operator.XOR, children=[solar_setup, skip])
xor_community_meet_training_session = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
xor_yield_monitor_adjust_plan = OperatorPOWL(operator=Operator.XOR, children=[yield_monitor, skip])

# Define root node
root = StrictPartialOrder(nodes=[
    loop_structure_check,
    xor_structure_check_soil_sample,
    loop_soil_sample,
    xor_water_test_crop_selection,
    loop_water_test,
    xor_crop_selection_material_order,
    loop_material_order,
    xor_planter_setup_irrigation_install,
    loop_planter_setup,
    xor_sensor_deploy_solar_setup,
    loop_irrigation_install,
    xor_data_integration_community_meet,
    loop_sensor_deploy,
    xor_training_session_yield_monitor,
    loop_solar_setup,
    xor_yield_monitor_adjust_plan,
    loop_data_integration,
    xor_community_meet_training_session,
    loop_yield_monitor,
    xor_adjust_plan
])

# Add dependencies
root.order.add_edge(loop_structure_check, xor_structure_check_soil_sample)
root.order.add_edge(xor_structure_check_soil_sample, loop_soil_sample)
root.order.add_edge(loop_soil_sample, xor_water_test_crop_selection)
root.order.add_edge(xor_water_test_crop_selection, loop_water_test)
root.order.add_edge(loop_water_test, xor_crop_selection_material_order)
root.order.add_edge(xor_crop_selection_material_order, loop_material_order)
root.order.add_edge(loop_material_order, xor_planter_setup_irrigation_install)
root.order.add_edge(xor_planter_setup_irrigation_install, loop_planter_setup)
root.order.add_edge(loop_planter_setup, xor_sensor_deploy_solar_setup)
root.order.add_edge(xor_sensor_deploy_solar_setup, loop_irrigation_install)
root.order.add_edge(loop_irrigation_install, xor_data_integration_community_meet)
root.order.add_edge(xor_data_integration_community_meet, loop_sensor_deploy)
root.order.add_edge(loop_sensor_deploy, xor_training_session_yield_monitor)
root.order.add_edge(xor_training_session_yield_monitor, loop_solar_setup)
root.order.add_edge(loop_solar_setup, xor_yield_monitor_adjust_plan)
root.order.add_edge(xor_yield_monitor_adjust_plan, loop_data_integration)
root.order.add_edge(loop_data_integration, xor_community_meet_training_session)
root.order.add_edge(xor_community_meet_training_session, loop_yield_monitor)
root.order.add_edge(loop_yield_monitor, xor_adjust_plan)

print(root)