import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
permit_review    = Transition(label='Permit Review')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install   = Transition(label='Sensor Install')
structural_test  = Transition(label='Structural Test')
recruit_farmers  = Transition(label='Recruit Farmers')
trial_planting   = Transition(label='Trial Planting')
soilless_prep    = Transition(label='Soilless Prep')
pest_control     = Transition(label='Pest Control')
system_calibrate = Transition(label='System Calibrate')
data_monitor     = Transition(label='Data Monitor')
harvest_plan     = Transition(label='Harvest Plan')
community_outreach= Transition(label='Community Outreach')

# Loop for continuous monitoring and pest control
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, pest_control])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_review, design_layout, material_sourcing,
    irrigation_setup, sensor_install, structural_test,
    recruit_farmers, trial_planting, soilless_prep,
    system_calibrate, monitor_loop, harvest_plan,
    community_outreach
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, permit_review)
root.order.add_edge(permit_review, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_install)
root.order.add_edge(sensor_install, structural_test)
root.order.add_edge(structural_test, recruit_farmers)
root.order.add_edge(recruit_farmers, trial_planting)
root.order.add_edge(trial_planting, soilless_prep)
root.order.add_edge(soilless_prep, system_calibrate)
root.order.add_edge(system_calibrate, monitor_loop)
root.order.add_edge(monitor_loop, harvest_plan)
root.order.add_edge(harvest_plan, community_outreach)