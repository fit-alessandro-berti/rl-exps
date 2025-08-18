from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define the loop nodes and exclusive choices
site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_audit])
modular_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_design, hydroponic_setup])
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_config, nutrient_mix])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_detect, lighting_setup])
energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, automation_install])
staff_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, market_analysis])
regulation_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, yield_monitor])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage, data_analytics])

# Define the exclusive choices
modular_xor = OperatorPOWL(operator=Operator.XOR, children=[modular_design, hydroponic_setup])
climate_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_config, nutrient_mix])
pest_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_detect, lighting_setup])
energy_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, automation_install])
staff_xor = OperatorPOWL(operator=Operator.XOR, children=[staff_training, market_analysis])
regulation_xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, yield_monitor])
waste_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, data_analytics])

# Create the root partial order
root = StrictPartialOrder(nodes=[
    site_audit_loop, modular_loop, climate_loop, pest_loop, energy_loop, staff_loop, regulation_loop, waste_loop,
    modular_xor, climate_xor, pest_xor, energy_xor, staff_xor, regulation_xor, waste_xor
])

# Define the dependencies
root.order.add_edge(site_audit_loop, modular_loop)
root.order.add_edge(modular_loop, climate_loop)
root.order.add_edge(climate_loop, pest_loop)
root.order.add_edge(pest_loop, energy_loop)
root.order.add_edge(energy_loop, staff_loop)
root.order.add_edge(staff_loop, regulation_loop)
root.order.add_edge(regulation_loop, waste_loop)

# Add the exclusive choices to the root
root.order.add_edge(modular_loop, modular_xor)
root.order.add_edge(climate_loop, climate_xor)
root.order.add_edge(pest_loop, pest_xor)
root.order.add_edge(energy_loop, energy_xor)
root.order.add_edge(staff_loop, staff_xor)
root.order.add_edge(regulation_loop, regulation_xor)
root.order.add_edge(waste_loop, waste_xor)

# Print the root to verify
print(root)