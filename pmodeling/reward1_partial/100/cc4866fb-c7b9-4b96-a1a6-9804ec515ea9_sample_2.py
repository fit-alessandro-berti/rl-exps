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

# Define exclusive choice for Site Survey and Design Planning
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_planning])

# Define loop for Permit Filing
permit_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_filing])

# Define loop for Structural Reinforce
structural_loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_reinforce])

# Define exclusive choice for Hydroponic Setup and Sensor Install
hydroponic_choice = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, sensor_install])

# Define loop for Energy Audit
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])

# Define exclusive choice for Crop Selection and Nutrient Mix
crop_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, nutrient_mix])

# Define loop for Waste Process
waste_process_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_process])

# Define loop for Climate Control
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control])

# Define loop for Staff Training
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training])

# Define exclusive choice for Market Study and Community Meet
market_choice = OperatorPOWL(operator=Operator.XOR, children=[market_study, community_meet])

# Define loop for Launch Trial
launch_trial_loop = OperatorPOWL(operator=Operator.LOOP, children=[launch_trial])

# Define loop for Data Monitor
data_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor])

# Define partial order
root = StrictPartialOrder(nodes=[
    exclusive_choice,
    permit_loop,
    structural_loop,
    hydroponic_choice,
    energy_audit_loop,
    crop_choice,
    waste_process_loop,
    climate_control_loop,
    staff_training_loop,
    market_choice,
    launch_trial_loop,
    data_monitor_loop
])

# Add dependencies between nodes
root.order.add_edge(exclusive_choice, permit_loop)
root.order.add_edge(exclusive_choice, structural_loop)
root.order.add_edge(permit_loop, hydroponic_choice)
root.order.add_edge(permit_loop, energy_audit_loop)
root.order.add_edge(structural_loop, hydroponic_choice)
root.order.add_edge(structural_loop, energy_audit_loop)
root.order.add_edge(hydroponic_choice, crop_choice)
root.order.add_edge(hydroponic_choice, waste_process_loop)
root.order.add_edge(energy_audit_loop, climate_control_loop)
root.order.add_edge(energy_audit_loop, staff_training_loop)
root.order.add_edge(crop_choice, market_choice)
root.order.add_edge(crop_choice, launch_trial_loop)
root.order.add_edge(waste_process_loop, climate_control_loop)
root.order.add_edge(waste_process_loop, staff_training_loop)
root.order.add_edge(climate_control_loop, launch_trial_loop)
root.order.add_edge(climate_control_loop, data_monitor_loop)
root.order.add_edge(staff_training_loop, launch_trial_loop)
root.order.add_edge(staff_training_loop, data_monitor_loop)
root.order.add_edge(market_choice, launch_trial_loop)
root.order.add_edge(market_choice, data_monitor_loop)
root.order.add_edge(launch_trial_loop, data_monitor_loop)

print(root)