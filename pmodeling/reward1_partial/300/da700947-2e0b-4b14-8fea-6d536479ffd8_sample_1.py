import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
climate_design = Transition(label='Climate Design')
lighting_setup = Transition(label='Lighting Setup')
irrigation_plan = Transition(label='Irrigation Plan')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
ai_calibration = Transition(label='AI Calibration')
pest_scan = Transition(label='Pest Scan')
energy_audit = Transition(label='Energy Audit')
renewable_sync = Transition(label='Renewable Sync')
data_modeling = Transition(label='Data Modeling')
staff_briefing = Transition(label='Staff Briefing')
compliance_check = Transition(label='Compliance Check')
community_meet = Transition(label='Community Meet')
yield_review = Transition(label='Yield Review')
feedback_loop = Transition(label='Feedback Loop')

# Define operators
site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_audit])
climate_lighting_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_design, lighting_setup])
irrigation_lighting_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_plan, nutrient_mix])
sensor_ai_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, ai_calibration])
pest_energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_scan, energy_audit])
renewable_data_loop = OperatorPOWL(operator=Operator.LOOP, children=[renewable_sync, data_modeling])
staff_compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_briefing, compliance_check])
community_yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, yield_review])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop])

# Define root
root = StrictPartialOrder(nodes=[site_audit_loop, climate_lighting_loop, irrigation_lighting_loop, sensor_ai_loop, pest_energy_loop, renewable_data_loop, staff_compliance_loop, community_yield_loop, feedback_loop])
root.order.add_edge(site_audit_loop, climate_lighting_loop)
root.order.add_edge(climate_lighting_loop, irrigation_lighting_loop)
root.order.add_edge(irrigation_lighting_loop, sensor_ai_loop)
root.order.add_edge(sensor_ai_loop, pest_energy_loop)
root.order.add_edge(pest_energy_loop, renewable_data_loop)
root.order.add_edge(renewable_data_loop, staff_compliance_loop)
root.order.add_edge(staff_compliance_loop, community_yield_loop)
root.order.add_edge(community_yield_loop, feedback_loop)

print(root)