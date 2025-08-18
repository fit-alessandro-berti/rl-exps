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

# Define the relationships between the activities using POWL operators
site_survey_to_design_planning = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_planning])
design_planning_to_permit_filing = OperatorPOWL(operator=Operator.XOR, children=[design_planning, permit_filing])
permit_filing_to_structural_reinforce = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, structural_reinforce])
structural_reinforce_to_hydroponic_setup = OperatorPOWL(operator=Operator.XOR, children=[structural_reinforce, hydroponic_setup])
hydroponic_setup_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, sensor_install])
sensor_install_to_energy_audit = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, energy_audit])
energy_audit_to_crop_selection = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, crop_selection])
crop_selection_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, nutrient_mix])
nutrient_mix_to_waste_process = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, waste_process])
waste_process_to_climate_control = OperatorPOWL(operator=Operator.XOR, children=[waste_process, climate_control])
climate_control_to_staff_training = OperatorPOWL(operator=Operator.XOR, children=[climate_control, staff_training])
staff_training_to_market_study = OperatorPOWL(operator=Operator.XOR, children=[staff_training, market_study])
market_study_to_community_meet = OperatorPOWL(operator=Operator.XOR, children=[market_study, community_meet])
community_meet_to_launch_trial = OperatorPOWL(operator=Operator.XOR, children=[community_meet, launch_trial])
launch_trial_to_data_monitor = OperatorPOWL(operator=Operator.XOR, children=[launch_trial, data_monitor])

# Create the root of the POWL model
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

# Add dependencies between activities
root.order.add_edge(site_survey, design_planning)
root.order.add_edge(design_planning, permit_filing)
root.order.add_edge(permit_filing, structural_reinforce)
root.order.add_edge(structural_reinforce, hydroponic_setup)
root.order.add_edge(hydroponic_setup, sensor_install)
root.order.add_edge(sensor_install, energy_audit)
root.order.add_edge(energy_audit, crop_selection)
root.order.add_edge(crop_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, waste_process)
root.order.add_edge(waste_process, climate_control)
root.order.add_edge(climate_control, staff_training)
root.order.add_edge(staff_training, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, launch_trial)
root.order.add_edge(launch_trial, data_monitor)

print(root)