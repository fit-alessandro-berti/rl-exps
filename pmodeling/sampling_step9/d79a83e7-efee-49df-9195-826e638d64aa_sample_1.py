import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
EnvAssessment = Transition(label='Env Assessment')
RegCompliance = Transition(label='Reg Compliance')
ModularSetup = Transition(label='Modular Setup')
CropSelection = Transition(label='Crop Selection')
IoTIntegration = Transition(label='IoT Integration')
NutrientFlow = Transition(label='Nutrient Flow')
LightCalibration = Transition(label='Light Calibration')
StaffTraining = Transition(label='Staff Training')
PestControl = Transition(label='Pest Control')
MarketStrategy = Transition(label='Market Strategy')
LogisticsPlan = Transition(label='Logistics Plan')
YieldAnalysis = Transition(label='Yield Analysis')
DataReview = Transition(label='Data Review')
CommunityEngage = Transition(label='Community Engage')

skip = SilentTransition()

# Site Survey
site_survey = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey])

# Environmental Assessment
env_assessment = OperatorPOWL(operator=Operator.LOOP, children=[EnvAssessment])

# Regulatory Compliance
reg_compliance = OperatorPOWL(operator=Operator.LOOP, children=[RegCompliance])

# Modular Infrastructure Setup
modular_setup = OperatorPOWL(operator=Operator.LOOP, children=[ModularSetup])

# Crop Selection
crop_selection = OperatorPOWL(operator=Operator.LOOP, children=[CropSelection])

# IoT Integration
iot_integration = OperatorPOWL(operator=Operator.LOOP, children=[IoTIntegration])

# Nutrient Circulation System Design
nutrient_flow = OperatorPOWL(operator=Operator.LOOP, children=[NutrientFlow])

# Automated Lighting Calibration
light_calibration = OperatorPOWL(operator=Operator.LOOP, children=[LightCalibration])

# Staff Training
staff_training = OperatorPOWL(operator=Operator.LOOP, children=[StaffTraining])

# Pest Control Protocols without Pesticides
pest_control = OperatorPOWL(operator=Operator.LOOP, children=[PestControl])

# Marketing Strategy Development
market_strategy = OperatorPOWL(operator=Operator.LOOP, children=[MarketStrategy])

# Logistics Planning for Fresh Produce Distribution
logistics_plan = OperatorPOWL(operator=Operator.LOOP, children=[LogisticsPlan])

# Continuous Yield Optimization through Data Analytics
yield_analysis = OperatorPOWL(operator=Operator.LOOP, children=[YieldAnalysis])

# Establishing Community Engagement Programs
community_engage = OperatorPOWL(operator=Operator.LOOP, children=[CommunityEngage])

root = StrictPartialOrder(nodes=[site_survey, env_assessment, reg_compliance, modular_setup, crop_selection, iot_integration, nutrient_flow, light_calibration, staff_training, pest_control, market_strategy, logistics_plan, yield_analysis, community_engage])
root.order.add_edge(site_survey, env_assessment)
root.order.add_edge(site_survey, reg_compliance)
root.order.add_edge(site_survey, modular_setup)
root.order.add_edge(site_survey, crop_selection)
root.order.add_edge(site_survey, iot_integration)
root.order.add_edge(site_survey, nutrient_flow)
root.order.add_edge(site_survey, light_calibration)
root.order.add_edge(site_survey, staff_training)
root.order.add_edge(site_survey, pest_control)
root.order.add_edge(site_survey, market_strategy)
root.order.add_edge(site_survey, logistics_plan)
root.order.add_edge(site_survey, yield_analysis)
root.order.add_edge(site_survey, community_engage)
root.order.add_edge(env_assessment, reg_compliance)
root.order.add_edge(env_assessment, modular_setup)
root.order.add_edge(env_assessment, crop_selection)
root.order.add_edge(env_assessment, iot_integration)
root.order.add_edge(env_assessment, nutrient_flow)
root.order.add_edge(env_assessment, light_calibration)
root.order.add_edge(env_assessment, staff_training)
root.order.add_edge(env_assessment, pest_control)
root.order.add_edge(env_assessment, market_strategy)
root.order.add_edge(env_assessment, logistics_plan)
root.order.add_edge(env_assessment, yield_analysis)
root.order.add_edge(env_assessment, community_engage)
root.order.add_edge(reg_compliance, modular_setup)
root.order.add_edge(reg_compliance, crop_selection)
root.order.add_edge(reg_compliance, iot_integration)
root.order.add_edge(reg_compliance, nutrient_flow)
root.order.add_edge(reg_compliance, light_calibration)
root.order.add_edge(reg_compliance, staff_training)
root.order.add_edge(reg_compliance, pest_control)
root.order.add_edge(reg_compliance, market_strategy)
root.order.add_edge(reg_compliance, logistics_plan)
root.order.add_edge(reg_compliance, yield_analysis)
root.order.add_edge(reg_compliance, community_engage)
root.order.add_edge(modular_setup, crop_selection)
root.order.add_edge(modular_setup, iot_integration)
root.order.add_edge(modular_setup, nutrient_flow)
root.order.add_edge(modular_setup, light_calibration)
root.order.add_edge(modular_setup, staff_training)
root.order.add_edge(modular_setup, pest_control)
root.order.add_edge(modular_setup, market_strategy)
root.order.add_edge(modular_setup, logistics_plan)
root.order.add_edge(modular_setup, yield_analysis)
root.order.add_edge(modular_setup, community_engage)
root.order.add_edge(crop_selection, iot_integration)
root.order.add_edge(crop_selection, nutrient_flow)
root.order.add_edge(crop_selection, light_calibration)
root.order.add_edge(crop_selection, staff_training)
root.order.add_edge(crop_selection, pest_control)
root.order.add_edge(crop_selection, market_strategy)
root.order.add_edge(crop_selection, logistics_plan)
root.order.add_edge(crop_selection, yield_analysis)
root.order.add_edge(crop_selection, community_engage)
root.order.add_edge(iot_integration, nutrient_flow)
root.order.add_edge(iot_integration, light_calibration)
root.order.add_edge(iot_integration, staff_training)
root.order.add_edge(iot_integration, pest_control)
root.order.add_edge(iot_integration, market_strategy)
root.order.add_edge(iot_integration, logistics_plan)
root.order.add_edge(iot_integration, yield_analysis)
root.order.add_edge(iot_integration, community_engage)
root.order.add_edge(nutrient_flow, light_calibration)
root.order.add_edge(nutrient_flow, staff_training)
root.order.add_edge(nutrient_flow, pest_control)
root.order.add_edge(nutrient_flow, market_strategy)
root.order.add_edge(nutrient_flow, logistics_plan)
root.order.add_edge(nutrient_flow, yield_analysis)
root.order.add_edge(nutrient_flow, community_engage)
root.order.add_edge(light_calibration, staff_training)
root.order.add_edge(light_calibration, pest_control)
root.order.add_edge(light_calibration, market_strategy)
root.order.add_edge(light_calibration, logistics_plan)
root.order.add_edge(light_calibration, yield_analysis)
root.order.add_edge(light_calibration, community_engage)
root.order.add_edge(staff_training, pest_control)
root.order.add_edge(staff_training, market_strategy)
root.order.add_edge(staff_training, logistics_plan)
root.order.add_edge(staff_training, yield_analysis)
root.order.add_edge(staff_training, community_engage)
root.order.add_edge(pest_control, market_strategy)
root.order.add_edge(pest_control, logistics_plan)
root.order.add_edge(pest_control, yield_analysis)
root.order.add_edge(pest_control, community_engage)
root.order.add_edge(market_strategy, logistics_plan)
root.order.add_edge(market_strategy, yield_analysis)
root.order.add_edge(market_strategy, community_engage)
root.order.add_edge(logistics_plan, yield_analysis)
root.order.add_edge(logistics_plan, community_engage)
root.order.add_edge(yield_analysis, community_engage)

print(root)