import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
design_planning = Transition(label='Design Planning')
permit_filing = Transition(label='Permit Filing')
structural_reinforce = Transition(label='Structural Reinforce')
hydroponic_setup = Transition(label='Hydroponic Setup')
sensor_install = Transition(label='Sensor Install')
energy_audit = Transition(label='Energy Audit')
crop_selection = Transition(label='Crop Selection')
nutrient_mix = Transition(label='Nutrient Mix')
waste_process = Transition(label='Waste Process')
climate_control = Transition(label='Climate Control')
staff_training = Transition(label='Staff Training')
market_study = Transition(label='Market Study')
community_meet = Transition(label='Community Meet')
launch_trial = Transition(label='Launch Trial')
data_monitor = Transition(label='Data Monitor')

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[structural_reinforce, site_survey])
loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_filing, design_planning])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, sensor_install])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, crop_selection])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, waste_process])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[climate_control, staff_training])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[market_study, community_meet])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[launch_trial, data_monitor])

# Create root POWL model
root = StrictPartialOrder(nodes=[xor, loop, xor_2, xor_3, xor_4, xor_5, xor_6, loop_2])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, loop_2)
root.order.add_edge(loop_2, launch_trial)