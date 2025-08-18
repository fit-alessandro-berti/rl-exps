import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    climate_design,
    lighting_setup,
    irrigation_plan,
    nutrient_mix,
    sensor_install,
    ai_calibration,
    pest_scan,
    energy_audit,
    renewable_sync,
    data_modeling,
    staff_briefing,
    compliance_check,
    community_meet,
    yield_review,
    feedback_loop
])

# Define the dependencies
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, climate_design)
root.order.add_edge(climate_design, lighting_setup)
root.order.add_edge(lighting_setup, irrigation_plan)
root.order.add_edge(irrigation_plan, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(sensor_install, ai_calibration)
root.order.add_edge(ai_calibration, pest_scan)
root.order.add_edge(pest_scan, energy_audit)
root.order.add_edge(energy_audit, renewable_sync)
root.order.add_edge(renewable_sync, data_modeling)
root.order.add_edge(data_modeling, staff_briefing)
root.order.add_edge(staff_briefing, compliance_check)
root.order.add_edge(compliance_check, community_meet)
root.order.add_edge(community_meet, yield_review)
root.order.add_edge(yield_review, feedback_loop)

# Print the POWL model
print(root)