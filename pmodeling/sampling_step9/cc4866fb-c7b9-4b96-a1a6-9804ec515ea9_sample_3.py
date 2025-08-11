import pm4py
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

# Define loop nodes
structural_loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_reinforce, design_planning])
hydroponic_loop = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, sensor_install])
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, nutrient_mix])
waste_process_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_process, climate_control])
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, market_study])
community_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, launch_trial])
data_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, skip])

# Define exclusive choice nodes
permit_filing_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])
crop_selection_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, skip])
market_study_xor = OperatorPOWL(operator=Operator.XOR, children=[market_study, skip])

# Define partial order
root = StrictPartialOrder(nodes=[structural_loop, hydroponic_loop, energy_audit_loop, waste_process_loop, staff_training_loop, community_meet_loop, data_monitor_loop, permit_filing_xor, crop_selection_xor, market_study_xor])
root.order.add_edge(structural_loop, hydroponic_loop)
root.order.add_edge(hydroponic_loop, energy_audit_loop)
root.order.add_edge(energy_audit_loop, waste_process_loop)
root.order.add_edge(waste_process_loop, staff_training_loop)
root.order.add_edge(staff_training_loop, community_meet_loop)
root.order.add_edge(community_meet_loop, data_monitor_loop)
root.order.add_edge(data_monitor_loop, permit_filing_xor)
root.order.add_edge(permit_filing_xor, crop_selection_xor)
root.order.add_edge(crop_selection_xor, market_study_xor)

# Print the root of the POWL model
print(root)