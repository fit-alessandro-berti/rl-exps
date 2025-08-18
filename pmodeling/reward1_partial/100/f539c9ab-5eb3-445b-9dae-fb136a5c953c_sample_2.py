from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
modular_design = Transition(label='Modular Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_config = Transition(label='Climate Config')
nutrient_mix = Transition(label='Nutrient Mix')
pest_detect = Transition(label='Pest Detect')
lighting_setup = Transition(label='Lighting Setup')
energy_audit = Transition(label='Energy Audit')
automation_install = Transition(label='Automation Install')
staff_training = Transition(label='Staff Training')
market_analysis = Transition(label='Market Analysis')
regulation_check = Transition(label='Regulation Check')
yield_monitor = Transition(label='Yield Monitor')
waste_manage = Transition(label='Waste Manage')
data_analytics = Transition(label='Data Analytics')

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, data_analytics])
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_audit, modular_design, hydroponic_setup, climate_config, nutrient_mix, pest_detect, lighting_setup, energy_audit, automation_install, staff_training, market_analysis, regulation_check, yield_monitor])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[xor, loop])

# Create the root POWL model
root = StrictPartialOrder(nodes=[xor2])
root.order.add_edge(xor2, loop)
root.order.add_edge(xor2, xor)