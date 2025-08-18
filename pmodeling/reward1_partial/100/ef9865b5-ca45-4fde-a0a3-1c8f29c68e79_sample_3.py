import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
structural_test = Transition(label='Structural Test')
recruit_farmers = Transition(label='Recruit Farmers')
trial_planting = Transition(label='Trial Planting')
pest_control = Transition(label='Pest Control')
soilless_prep = Transition(label='Soilless Prep')
system_calibrate = Transition(label='System Calibrate')
data_monitor = Transition(label='Data Monitor')
harvest_plan = Transition(label='Harvest Plan')
community_outreach = Transition(label='Community Outreach')

# Define the loop for the trial planting and pest control activities
trial_and_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[trial_planting, pest_control])

# Define the exclusive choice for the soilless preparation and system calibration
soilless_or_calibrate = OperatorPOWL(operator=Operator.XOR, children=[soilless_prep, system_calibrate])

# Define the root POWL model with the defined activities and loop
root = StrictPartialOrder(nodes=[site_survey, permit_review, design_layout, material_sourcing, irrigation_setup, sensor_install, structural_test, recruit_farmers, trial_and_pest_loop, soilless_or_calibrate, data_monitor, harvest_plan, community_outreach])
root.order.add_edge(site_survey, permit_review)
root.order.add_edge(permit_review, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_install)
root.order.add_edge(sensor_install, structural_test)
root.order.add_edge(structural_test, recruit_farmers)
root.order.add_edge(recruit_farmers, trial_and_pest_loop)
root.order.add_edge(trial_and_pest_loop, soilless_or_calibrate)
root.order.add_edge(soilless_or_calibrate, data_monitor)
root.order.add_edge(data_monitor, harvest_plan)
root.order.add_edge(harvest_plan, community_outreach)