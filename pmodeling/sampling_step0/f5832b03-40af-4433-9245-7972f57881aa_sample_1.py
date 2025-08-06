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

# Define silent transitions
skip = SilentTransition()

# Define POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_build, climate_setup, irrigation_install, sensor_deploy, nutrient_prep, waste_system, automation_config])
xor = OperatorPOWL(operator=Operator.XOR, children=[crop_select, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the final result
print(root)