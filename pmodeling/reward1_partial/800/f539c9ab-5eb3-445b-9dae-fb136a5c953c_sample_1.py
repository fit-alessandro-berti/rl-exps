import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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
# Exclusive choice: Site Survey, Structural Audit, Modular Design
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_audit, modular_design])

# Loop: Hydroponic Setup, Climate Config, Nutrient Mix, Pest Detect, Lighting Setup, Energy Audit
loop = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, climate_config, nutrient_mix, pest_detect, lighting_setup, energy_audit])

# Exclusive choice: Automation Install, Staff Training, Market Analysis
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[automation_install, staff_training, market_analysis])

# Exclusive choice: Regulation Check, Yield Monitor, Waste Manage
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, yield_monitor, waste_manage])

# Exclusive choice: Data Analytics
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[data_analytics])

# Define the root POWL model
root = StrictPartialOrder(nodes=[exclusive_choice, loop, exclusive_choice2, exclusive_choice3, exclusive_choice4])

# Define the dependencies (partial order)
root.order.add_edge(exclusive_choice, loop)
root.order.add_edge(loop, exclusive_choice2)
root.order.add_edge(exclusive_choice2, exclusive_choice3)
root.order.add_edge(exclusive_choice3, exclusive_choice4)

print(root)