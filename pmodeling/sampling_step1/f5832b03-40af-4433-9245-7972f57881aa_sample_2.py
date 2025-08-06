import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
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

# Define the dependencies between activities
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, legal_review)
root.order.add_edge(site_survey, tech_sourcing)
root.order.add_edge(site_survey, structural_build)
root.order.add_edge(site_survey, climate_setup)
root.order.add_edge(site_survey, irrigation_install)
root.order.add_edge(site_survey, sensor_deploy)
root.order.add_edge(site_survey, crop_select)
root.order.add_edge(site_survey, nutrient_prep)
root.order.add_edge(site_survey, waste_system)
root.order.add_edge(site_survey, automation_config)
root.order.add_edge(site_survey, trial_growth)
root.order.add_edge(site_survey, data_analysis)
root.order.add_edge(site_survey, quality_audit)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(site_survey, compliance_check)

# Add the dependencies between other activities
root.order.add_edge(design_layout, legal_review)
root.order.add_edge(design_layout, tech_sourcing)
root.order.add_edge(design_layout, structural_build)
root.order.add_edge(design_layout, climate_setup)
root.order.add_edge(design_layout, irrigation_install)
root.order.add_edge(design_layout, sensor_deploy)
root.order.add_edge(design_layout, crop_select)
root.order.add_edge(design_layout, nutrient_prep)
root.order.add_edge(design_layout, waste_system)
root.order.add_edge(design_layout, automation_config)
root.order.add_edge(design_layout, trial_growth)
root.order.add_edge(design_layout, data_analysis)
root.order.add_edge(design_layout, quality_audit)
root.order.add_edge(design_layout, stakeholder_meet)
root.order.add_edge(design_layout, compliance_check)

# Print the root POWL model
print(root)