import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
legal_review = Transition(label='Legal Review')
tech_sourcing = Transition(label='Tech Sourcing')
structural_build = Transition(label='Structural Build')
climate_setup = Transition(label='Climate Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
crop_select = Transition(label='Crop Select')
nutrient_prep = Transition(label='Nutrient Prep')
waste_system = Transition(label='Waste System')
automation_config = Transition(label='Automation Config')
trial_growth = Transition(label='Trial Growth')
data_analysis = Transition(label='Data Analysis')
quality_audit = Transition(label='Quality Audit')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    legal_review,
    tech_sourcing,
    structural_build,
    climate_setup,
    irrigation_install,
    sensor_deploy,
    crop_select,
    nutrient_prep,
    waste_system,
    automation_config,
    trial_growth,
    data_analysis,
    quality_audit,
    stakeholder_meet,
    compliance_check
])

# Define the order of activities
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, legal_review)
root.order.add_edge(legal_review, tech_sourcing)
root.order.add_edge(tech_sourcing, structural_build)
root.order.add_edge(structural_build, climate_setup)
root.order.add_edge(climate_setup, irrigation_install)
root.order.add_edge(irrigation_install, sensor_deploy)
root.order.add_edge(sensor_deploy, crop_select)
root.order.add_edge(crop_select, nutrient_prep)
root.order.add_edge(nutrient_prep, waste_system)
root.order.add_edge(waste_system, automation_config)
root.order.add_edge(automation_config, trial_growth)
root.order.add_edge(trial_growth, data_analysis)
root.order.add_edge(data_analysis, quality_audit)
root.order.add_edge(quality_audit, stakeholder_meet)
root.order.add_edge(stakeholder_meet, compliance_check)

# Print the final POWL model
print(root)