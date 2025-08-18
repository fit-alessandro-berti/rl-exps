from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes and their dependencies
loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_reinforce, hydroponic_setup])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, energy_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, nutrient_mix])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_process, climate_control])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, market_study])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[community_meet, launch_trial])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[data_monitor, skip])

root = StrictPartialOrder(nodes=[site_survey, design_planning, permit_filing, loop, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(site_survey, design_planning)
root.order.add_edge(design_planning, permit_filing)
root.order.add_edge(permit_filing, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, data_monitor)

print(root)