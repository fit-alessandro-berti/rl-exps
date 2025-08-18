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

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_planning, permit_filing])
structural_reinforce_loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_reinforce])
hydroponic_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, sensor_install, energy_audit])
crop_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, nutrient_mix, waste_process, climate_control])
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training])
market_study_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_study, community_meet, launch_trial, data_monitor])

root = StrictPartialOrder(nodes=[site_survey_loop, structural_reinforce_loop, hydroponic_setup_loop, crop_selection_loop, staff_training_loop, market_study_loop])
root.order.add_edge(site_survey_loop, structural_reinforce_loop)
root.order.add_edge(structural_reinforce_loop, hydroponic_setup_loop)
root.order.add_edge(hydroponic_setup_loop, crop_selection_loop)
root.order.add_edge(crop_selection_loop, staff_training_loop)
root.order.add_edge(staff_training_loop, market_study_loop)