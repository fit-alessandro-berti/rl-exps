import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey      = Transition(label='Site Survey')
env_assessment   = Transition(label='Env Assessment')
reg_compliance   = Transition(label='Reg Compliance')
modular_setup    = Transition(label='Modular Setup')
crop_selection   = Transition(label='Crop Selection')
iot_integration  = Transition(label='IoT Integration')
nutrient_flow    = Transition(label='Nutrient Flow')
light_calibration= Transition(label='Light Calibration')
staff_training   = Transition(label='Staff Training')
pest_control     = Transition(label='Pest Control')
market_strategy  = Transition(label='Market Strategy')
logistics_plan   = Transition(label='Logistics Plan')
yield_analysis   = Transition(label='Yield Analysis')
data_review      = Transition(label='Data Review')
community_engage = Transition(label='Community Engage')

# Define the data review loop: repeat Data Review until exit
skip = SilentTransition()
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review, skip])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey, env_assessment, reg_compliance, modular_setup,
    crop_selection, iot_integration, nutrient_flow, light_calibration,
    staff_training, pest_control, market_strategy, logistics_plan,
    yield_analysis, data_loop, community_engage
])

# Sequence of initial setup activities
root.order.add_edge(site_survey, env_assessment)
root.order.add_edge(env_assessment, reg_compliance)
root.order.add_edge(reg_compliance, modular_setup)

# Then parallelize the core farming activities
root.order.add_edge(modular_setup, crop_selection)
root.order.add_edge(modular_setup, iot_integration)
root.order.add_edge(modular_setup, nutrient_flow)
root.order.add_edge(modular_setup, light_calibration)
root.order.add_edge(modular_setup, staff_training)
root.order.add_edge(modular_setup, pest_control)

# Follow with market and logistics planning
root.order.add_edge(crop_selection, market_strategy)
root.order.add_edge(crop_selection, logistics_plan)

# Concurrency between IoT Integration and Nutrient Flow
root.order.add_edge(iot_integration, nutrient_flow)

# Then yield analysis and data review in parallel
root.order.add_edge(nutrient_flow, yield_analysis)
root.order.add_edge(nutrient_flow, data_loop)

# After yield analysis, community engagement
root.order.add_edge(yield_analysis, community_engage)
root.order.add_edge(data_loop, community_engage)

# Finally, logistics plan is complete
root.order.add_edge(logistics_plan, community_engage)