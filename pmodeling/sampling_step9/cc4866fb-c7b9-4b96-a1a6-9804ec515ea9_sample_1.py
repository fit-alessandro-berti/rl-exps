import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_planning])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[structural_reinforce, skip])

loop2 = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, sensor_install])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])

loop3 = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, nutrient_mix])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_process, skip])

loop4 = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, staff_training])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[market_study, skip])

loop5 = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, launch_trial])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_monitor, skip])

root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4, xor4, loop5, xor5])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)