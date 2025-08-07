import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
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

# Create the root node as a StrictPartialOrder with all activities as children
root = StrictPartialOrder(nodes=[site_survey, permit_review, design_layout, material_sourcing, irrigation_setup, sensor_install, structural_test, recruit_farmers, trial_planting, pest_control, soilless_prep, system_calibrate, data_monitor, harvest_plan, community_outreach])

# The order of activities can be defined based on the dependencies, but for simplicity, we assume all activities are concurrent
# root.order.add_edge(site_survey, permit_review)
# root.order.add_edge(site_survey, design_layout)
# root.order.add_edge(site_survey, material_sourcing)
# root.order.add_edge(site_survey, irrigation_setup)
# root.order.add_edge(site_survey, sensor_install)
# root.order.add_edge(site_survey, structural_test)
# root.order.add_edge(site_survey, recruit_farmers)
# root.order.add_edge(site_survey, trial_planting)
# root.order.add_edge(site_survey, pest_control)
# root.order.add_edge(site_survey, soilless_prep)
# root.order.add_edge(site_survey, system_calibrate)
# root.order.add_edge(site_survey, data_monitor)
# root.order.add_edge(site_survey, harvest_plan)
# root.order.add_edge(site_survey, community_outreach)

# Print the root node
print(root)