import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
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

# Define control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[structural_build, legal_review])
loop = OperatorPOWL(operator=Operator.LOOP, children=[tech_sourcing, climate_setup, irrigation_install, sensor_deploy])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, nutrient_prep, waste_system, automation_config])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[trial_growth, data_analysis, quality_audit, stakeholder_meet])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check])

# Define the root Partial Order
root = StrictPartialOrder(nodes=[site_survey, design_layout, xor, loop, xor_2, xor_3, xor_4])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, compliance_check)

print(root)