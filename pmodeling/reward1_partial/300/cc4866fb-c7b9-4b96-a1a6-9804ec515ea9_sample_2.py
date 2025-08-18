from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define exclusive choice for 'Sensor Install' and 'Energy Audit'
sensor_energy_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, energy_audit])

# Define loop for 'Staff Training'
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training])

# Define strict partial order with dependencies
root = StrictPartialOrder(nodes=[
    site_survey,
    design_planning,
    permit_filing,
    structural_reinforce,
    hydroponic_setup,
    sensor_energy_choice,
    nutrient_mix,
    waste_process,
    climate_control,
    staff_training_loop,
    market_study,
    community_meet,
    launch_trial,
    data_monitor
])

# Define dependencies
root.order.add_edge(site_survey, design_planning)
root.order.add_edge(design_planning, permit_filing)
root.order.add_edge(permit_filing, structural_reinforce)
root.order.add_edge(structural_reinforce, hydroponic_setup)
root.order.add_edge(hydroponic_setup, sensor_energy_choice)
root.order.add_edge(sensor_energy_choice, nutrient_mix)
root.order.add_edge(nutrient_mix, waste_process)
root.order.add_edge(waste_process, climate_control)
root.order.add_edge(climate_control, staff_training_loop)
root.order.add_edge(staff_training_loop, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, launch_trial)
root.order.add_edge(launch_trial, data_monitor)

# Print the root
print(root)