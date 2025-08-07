import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
env_assess = Transition(label='Env Assessment')
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
community_engage = Transition(label='Community Engage')

# Define the yield analysis and data review loop: do Yield Analysis, then optionally Data Review and repeat
yield_analysis = Transition(label='Yield Analysis')
data_review = Transition(label='Data Review')
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis, data_review])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, env_assess, reg_compliance, modular_setup,
    crop_selection, iot_integration, nutrient_flow, light_calibration,
    staff_training, pest_control, market_strategy, logistics_plan,
    community_engage, data_loop
])

# Define the control-flow edges
root.order.add_edge(site_survey, env_assess)
root.order.add_edge(env_assess, reg_compliance)
root.order.add_edge(reg_compliance, modular_setup)
root.order.add_edge(modular_setup, crop_selection)
root.order.add_edge(crop_selection, iot_integration)
root.order.add_edge(iot_integration, nutrient_flow)
root.order.add_edge(nutrient_flow, light_calibration)
root.order.add_edge(light_calibration, staff_training)
root.order.add_edge(staff_training, pest_control)
root.order.add_edge(pest_control, market_strategy)
root.order.add_edge(market_strategy, logistics_plan)
root.order.add_edge(logistics_plan, community_engage)
root.order.add_edge(community_engage, data_loop)

# Print the root model (optional, for verification)
print(root)