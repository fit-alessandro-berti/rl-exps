import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_lighting = Transition(label='Install Lighting')
setup_hydroponics = Transition(label='Setup Hydroponics')
calibrate_sensors = Transition(label='Calibrate Sensors')
select_crops = Transition(label='Select Crops')
mix_nutrients = Transition(label='Mix Nutrients')
deploy_iot = Transition(label='Deploy IoT')
energy_audit = Transition(label='Energy Audit')
train_staff = Transition(label='Train Staff')
pest_control = Transition(label='Pest Control')
legal_review = Transition(label='Legal Review')
market_analysis = Transition(label='Market Analysis')
plan_logistics = Transition(label='Plan Logistics')
yield_review = Transition(label='Yield Review')

# Define the nodes and their order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, install_lighting, setup_hydroponics, calibrate_sensors, select_crops, mix_nutrients, deploy_iot, energy_audit, legal_review, market_analysis, plan_logistics])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, train_staff, yield_review])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Create the root node
root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)