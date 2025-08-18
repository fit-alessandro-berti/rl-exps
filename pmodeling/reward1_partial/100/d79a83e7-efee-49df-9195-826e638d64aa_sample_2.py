import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[site_survey, env_assessment, reg_compliance, modular_setup, crop_selection,
           iot_integration, nutrient_flow, light_calibration, staff_training,
           pest_control, market_strategy, logistics_plan, yield_analysis, data_review,
           community_engage],
    order={
        (site_survey, env_assessment): OperatorPOWL(operator=Operator.XOR),
        (site_survey, reg_compliance): OperatorPOWL(operator=Operator.XOR),
        (site_survey, modular_setup): OperatorPOWL(operator=Operator.XOR),
        (env_assessment, crop_selection): OperatorPOWL(operator=Operator.XOR),
        (reg_compliance, modular_setup): OperatorPOWL(operator=Operator.XOR),
        (modular_setup, iot_integration): OperatorPOWL(operator=Operator.XOR),
        (iot_integration, nutrient_flow): OperatorPOWL(operator=Operator.XOR),
        (nutrient_flow, light_calibration): OperatorPOWL(operator=Operator.XOR),
        (light_calibration, staff_training): OperatorPOWL(operator=Operator.XOR),
        (staff_training, pest_control): OperatorPOWL(operator=Operator.XOR),
        (pest_control, market_strategy): OperatorPOWL(operator=Operator.XOR),
        (market_strategy, logistics_plan): OperatorPOWL(operator=Operator.XOR),
        (logistics_plan, yield_analysis): OperatorPOWL(operator=Operator.XOR),
        (yield_analysis, data_review): OperatorPOWL(operator=Operator.XOR),
        (data_review, community_engage): OperatorPOWL(operator=Operator.XOR)
    }
)

print(root)