import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
env_control = Transition(label='Env Control')
nutrient_mix = Transition(label='Nutrient Mix')
crop_select = Transition(label='Crop Select')
ai_setup = Transition(label='AI Setup')
worker_train = Transition(label='Worker Train')
pest_control = Transition(label='Pest Control')
irrigation_plan = Transition(label='Irrigation Plan')
data_monitor = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_audit = Transition(label='Energy Audit')
market_setup = Transition(label='Market Setup')
logistics_plan = Transition(label='Logistics Plan')
waste_manage = Transition(label='Waste Manage')

# Create exclusive choices for some activities
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ai_setup, worker_train])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, irrigation_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_monitor, yield_forecast])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, market_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, waste_manage])

# Define loops for repetitive tasks
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structure_prep, system_install, env_control, nutrient_mix, crop_select])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5])

# Construct the overall partial order
root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)

# Add edges to connect the activities within the loops
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop2, xor5)