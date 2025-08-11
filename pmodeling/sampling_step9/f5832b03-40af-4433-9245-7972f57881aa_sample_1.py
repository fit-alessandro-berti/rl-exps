import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_build, climate_setup])
xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_install, sensor_deploy])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, nutrient_prep])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_system, automation_config])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[trial_growth, data_analysis])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, stakeholder_meet])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)