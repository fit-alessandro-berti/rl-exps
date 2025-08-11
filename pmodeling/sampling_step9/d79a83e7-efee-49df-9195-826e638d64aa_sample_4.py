import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
env_assessment = Transition(label='Env Assessment')
reg_compliance = Transition(label='Reg Compliance')
modular_setup = Transition(label='Modular Setup')
crop_selection = Transition(label='Crop Selection')
iot_integration = Transition(label='IoT Integration')
nutrient_flow = Transition(label='Nutrient Flow')
light_calibration = Transition(label='Light Calibration')
staff_training = Transition(label='Staff Training')
pest_control = Transition(label='Pest Control')
market_strategy = Transition(label='Market Strategy')
logistics_plan = Transition(label='Logistics Plan')
yield_analysis = Transition(label='Yield Analysis')
data_review = Transition(label='Data Review')
community_engage = Transition(label='Community Engage')

# Define silent activities
skip = SilentTransition()

# Define loop nodes
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
loop_env_assessment = OperatorPOWL(operator=Operator.LOOP, children=[env_assessment])
loop_reg_compliance = OperatorPOWL(operator=Operator.LOOP, children=[reg_compliance])
loop_modular_setup = OperatorPOWL(operator=Operator.LOOP, children=[modular_setup])
loop_crop_selection = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection])
loop_iot_integration = OperatorPOWL(operator=Operator.LOOP, children=[iot_integration])
loop_nutrient_flow = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_flow])
loop_light_calibration = OperatorPOWL(operator=Operator.LOOP, children=[light_calibration])
loop_staff_training = OperatorPOWL(operator=Operator.LOOP, children=[staff_training])
loop_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
loop_market_strategy = OperatorPOWL(operator=Operator.LOOP, children=[market_strategy])
loop_logistics_plan = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan])
loop_yield_analysis = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis])
loop_data_review = OperatorPOWL(operator=Operator.LOOP, children=[data_review])
loop_community_engage = OperatorPOWL(operator=Operator.LOOP, children=[community_engage])

# Define exclusive choices
xor_site_survey = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_site_survey])
xor_env_assessment = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_env_assessment])
xor_reg_compliance = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_reg_compliance])
xor_modular_setup = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_modular_setup])
xor_crop_selection = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_crop_selection])
xor_iot_integration = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_iot_integration])
xor_nutrient_flow = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_nutrient_flow])
xor_light_calibration = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_light_calibration])
xor_staff_training = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_staff_training])
xor_pest_control = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_pest_control])
xor_market_strategy = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_market_strategy])
xor_logistics_plan = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_logistics_plan])
xor_yield_analysis = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_yield_analysis])
xor_data_review = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_data_review])
xor_community_engage = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_community_engage])

# Define the root model
root = StrictPartialOrder(nodes=[xor_site_survey, xor_env_assessment, xor_reg_compliance, xor_modular_setup, xor_crop_selection, xor_iot_integration, xor_nutrient_flow, xor_light_calibration, xor_staff_training, xor_pest_control, xor_market_strategy, xor_logistics_plan, xor_yield_analysis, xor_data_review, xor_community_engage])

# Add edges
root.order.add_edge(xor_site_survey, loop_site_survey)
root.order.add_edge(xor_env_assessment, loop_env_assessment)
root.order.add_edge(xor_reg_compliance, loop_reg_compliance)
root.order.add_edge(xor_modular_setup, loop_modular_setup)
root.order.add_edge(xor_crop_selection, loop_crop_selection)
root.order.add_edge(xor_iot_integration, loop_iot_integration)
root.order.add_edge(xor_nutrient_flow, loop_nutrient_flow)
root.order.add_edge(xor_light_calibration, loop_light_calibration)
root.order.add_edge(xor_staff_training, loop_staff_training)
root.order.add_edge(xor_pest_control, loop_pest_control)
root.order.add_edge(xor_market_strategy, loop_market_strategy)
root.order.add_edge(xor_logistics_plan, loop_logistics_plan)
root.order.add_edge(xor_yield_analysis, loop_yield_analysis)
root.order.add_edge(xor_data_review, loop_data_review)
root.order.add_edge(xor_community_engage, loop_community_engage)

print(root)