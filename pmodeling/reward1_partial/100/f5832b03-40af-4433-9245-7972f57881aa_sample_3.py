import pm4py

# Define the transitions (activities)
site_survey = pm4py.objects.powl.obj.Transition(label='Site Survey')
design_layout = pm4py.objects.powl.obj.Transition(label='Design Layout')
legal_review = pm4py.objects.powl.obj.Transition(label='Legal Review')
tech_sourcing = pm4py.objects.powl.obj.Transition(label='Tech Sourcing')
structural_build = pm4py.objects.powl.obj.Transition(label='Structural Build')
climate_setup = pm4py.objects.powl.obj.Transition(label='Climate Setup')
irrigation_install = pm4py.objects.powl.obj.Transition(label='Irrigation Install')
sensor_deploy = pm4py.objects.powl.obj.Transition(label='Sensor Deploy')
crop_select = pm4py.objects.powl.obj.Transition(label='Crop Select')
nutrient_prep = pm4py.objects.powl.obj.Transition(label='Nutrient Prep')
waste_system = pm4py.objects.powl.obj.Transition(label='Waste System')
automation_config = pm4py.objects.powl.obj.Transition(label='Automation Config')
trial_growth = pm4py.objects.powl.obj.Transition(label='Trial Growth')
data_analysis = pm4py.objects.powl.obj.Transition(label='Data Analysis')
quality_audit = pm4py.objects.powl.obj.Transition(label='Quality Audit')
stakeholder_meet = pm4py.objects.powl.obj.Transition(label='Stakeholder Meet')
compliance_check = pm4py.objects.powl.obj.Transition(label='Compliance Check')

# Define the exclusive choice between two paths
exclusive_choice = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[quality_audit, compliance_check])

# Define the loop for trial growth and data analysis
loop = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.LOOP, children=[trial_growth, data_analysis])

# Define the main POWL model
root = pm4py.objects.powl.obj.StrictPartialOrder(nodes=[site_survey, design_layout, legal_review, tech_sourcing, structural_build, climate_setup, irrigation_install, sensor_deploy, crop_select, nutrient_prep, waste_system, automation_config, loop, exclusive_choice])
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
root.order.add_edge(automation_config, loop)
root.order.add_edge(loop, loop)
root.order.add_edge(loop, exclusive_choice)

print(root)