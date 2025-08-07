from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their names
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

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, env_assessment, reg_compliance, modular_setup, crop_selection, iot_integration, nutrient_flow, light_calibration, staff_training, pest_control, market_strategy, logistics_plan, yield_analysis, data_review, community_engage])

# Define the dependencies (edges) between the activities
root.order.add_edge(site_survey, env_assessment)
root.order.add_edge(site_survey, reg_compliance)
root.order.add_edge(site_survey, modular_setup)
root.order.add_edge(env_assessment, crop_selection)
root.order.add_edge(env_assessment, iot_integration)
root.order.add_edge(env_assessment, nutrient_flow)
root.order.add_edge(env_assessment, light_calibration)
root.order.add_edge(env_assessment, staff_training)
root.order.add_edge(env_assessment, pest_control)
root.order.add_edge(env_assessment, market_strategy)
root.order.add_edge(env_assessment, logistics_plan)
root.order.add_edge(env_assessment, yield_analysis)
root.order.add_edge(env_assessment, data_review)
root.order.add_edge(env_assessment, community_engage)

# Print the root to see the complete POWL model
print(root)