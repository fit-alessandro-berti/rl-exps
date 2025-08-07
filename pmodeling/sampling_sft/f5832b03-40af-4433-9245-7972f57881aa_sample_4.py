import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
legal_review    = Transition(label='Legal Review')
tech_sourcing   = Transition(label='Tech Sourcing')
stakeholder_meet= Transition(label='Stakeholder Meet')
compliance_check= Transition(label='Compliance Check')

structural_build= Transition(label='Structural Build')
climate_setup   = Transition(label='Climate Setup')
irrigation_install= Transition(label='Irrigation Install')
sensor_deploy   = Transition(label='Sensor Deploy')
automation_config= Transition(label='Automation Config')

crop_select     = Transition(label='Crop Select')
nutrient_prep   = Transition(label='Nutrient Prep')
waste_system    = Transition(label='Waste System')

trial_growth    = Transition(label='Trial Growth')
data_analysis   = Transition(label='Data Analysis')
quality_audit   = Transition(label='Quality Audit')

# Loop for continuous growth monitoring & analysis
loop_growth = OperatorPOWL(
    operator=Operator.LOOP,
    children=[trial_growth, data_analysis]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    legal_review,
    tech_sourcing,
    stakeholder_meet,
    compliance_check,
    structural_build,
    climate_setup,
    irrigation_install,
    sensor_deploy,
    automation_config,
    crop_select,
    nutrient_prep,
    waste_system,
    loop_growth,
    quality_audit
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, legal_review)
root.order.add_edge(legal_review, tech_sourcing)
root.order.add_edge(tech_sourcing, stakeholder_meet)
root.order.add_edge(stakeholder_meet, compliance_check)

root.order.add_edge(compliance_check, structural_build)
root.order.add_edge(structural_build, climate_setup)
root.order.add_edge(climate_setup, irrigation_install)
root.order.add_edge(irrigation_install, sensor_deploy)
root.order.add_edge(sensor_deploy, automation_config)

root.order.add_edge(automation_config, crop_select)
root.order.add_edge(crop_select, nutrient_prep)
root.order.add_edge(nutrient_prep, waste_system)

# Concurrency for trial & analysis
root.order.add_edge(crop_select, loop_growth)
root.order.add_edge(nutrient_prep, loop_growth)
root.order.add_edge(waste_system, loop_growth)

# Final audit after growth loop
root.order.add_edge(loop_growth, quality_audit)