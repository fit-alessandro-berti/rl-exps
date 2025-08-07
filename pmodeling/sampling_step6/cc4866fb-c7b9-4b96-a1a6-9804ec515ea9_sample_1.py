import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_planning,
    permit_filing,
    structural_reinforce,
    hydroponic_setup,
    sensor_install,
    energy_audit,
    crop_selection,
    nutrient_mix,
    waste_process,
    climate_control,
    staff_training,
    market_study,
    community_meet,
    launch_trial,
    data_monitor
])

# Define the dependencies
root.order.add_edge(site_survey, design_planning)
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, structural_reinforce)
root.order.add_edge(site_survey, hydroponic_setup)
root.order.add_edge(site_survey, sensor_install)
root.order.add_edge(site_survey, energy_audit)
root.order.add_edge(site_survey, crop_selection)
root.order.add_edge(site_survey, nutrient_mix)
root.order.add_edge(site_survey, waste_process)
root.order.add_edge(site_survey, climate_control)
root.order.add_edge(site_survey, staff_training)
root.order.add_edge(site_survey, market_study)
root.order.add_edge(site_survey, community_meet)
root.order.add_edge(site_survey, launch_trial)
root.order.add_edge(site_survey, data_monitor)

# Print the root of the POWL model
print(root)