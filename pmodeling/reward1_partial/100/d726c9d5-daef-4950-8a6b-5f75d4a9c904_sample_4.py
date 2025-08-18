import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choices
structure_check_or_soil_test = OperatorPOWL(operator=Operator.XOR, children=[structure_check, soil_sample])
water_test_or_crop_select = OperatorPOWL(operator=Operator.XOR, children=[water_test, crop_selection])
material_order_or_planter_setup = OperatorPOWL(operator=Operator.XOR, children=[material_order, planter_setup])
irrigation_or_sensor_deploy = OperatorPOWL(operator=Operator.XOR, children=[irrigation_install, sensor_deploy])
solar_or_data_integration = OperatorPOWL(operator=Operator.XOR, children=[solar_setup, data_integration])

# Define loops
community_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, training_session])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, structure_check_or_soil_test, water_test_or_crop_select, material_order_or_planter_setup, irrigation_or_sensor_deploy, solar_or_data_integration, community_meet_loop, yield_monitor, adjust_plan])

# Add dependencies
root.order.add_edge(site_survey, structure_check_or_soil_test)
root.order.add_edge(site_survey, water_test_or_crop_select)
root.order.add_edge(structure_check_or_soil_test, material_order_or_planter_setup)
root.order.add_edge(water_test_or_crop_select, irrigation_or_sensor_deploy)
root.order.add_edge(material_order_or_planter_setup, solar_or_data_integration)
root.order.add_edge(solar_or_data_integration, community_meet_loop)
root.order.add_edge(community_meet_loop, yield_monitor)
root.order.add_edge(yield_monitor, adjust_plan)

# Print the POWL model
print(root)