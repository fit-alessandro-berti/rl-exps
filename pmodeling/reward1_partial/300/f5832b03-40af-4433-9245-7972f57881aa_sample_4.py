import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, legal_review, tech_sourcing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[structural_build, climate_setup, irrigation_install, sensor_deploy])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, nutrient_prep, waste_system])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[automation_config, trial_growth, data_analysis])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, stakeholder_meet, compliance_check])

# Define partial order
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor, xor4)
root.order.add_edge(xor, xor5)