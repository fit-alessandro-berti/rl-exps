import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
permit_review    = Transition(label='Permit Review')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install   = Transition(label='Sensor Install')
structural_test  = Transition(label='Structural Test')
recruit_farmers  = Transition(label='Recruit Farmers')
trial_planting   = Transition(label='Trial Planting')
pest_control     = Transition(label='Pest Control')
soilless_prep    = Transition(label='Soilless Prep')
system_calibrate = Transition(label='System Calibrate')
data_monitor     = Transition(label='Data Monitor')
harvest_plan     = Transition(label='Harvest Plan')
community_outreach= Transition(label='Community Outreach')

# Build the loop body: Pest Control -> Soilless Prep -> System Calibrate -> Data Monitor
loop_body = StrictPartialOrder(nodes=[pest_control, soilless_prep, system_calibrate, data_monitor])
loop_body.order.add_edge(pest_control, soilless_prep)
loop_body.order.add_edge(soilless_prep, system_calibrate)
loop_body.order.add_edge(system_calibrate, data_monitor)

# Define the LOOP operator: execute trial_planting, then repeat loop_body until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[trial_planting, loop_body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_review, design_layout, material_sourcing,
    irrigation_setup, sensor_install, structural_test, recruit_farmers,
    loop, harvest_plan, community_outreach
])

# Sequential control-flow edges
root.order.add_edge(site_survey, permit_review)
root.order.add_edge(permit_review, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_install)
root.order.add_edge(sensor_install, structural_test)
root.order.add_edge(structural_test, recruit_farmers)
root.order.add_edge(recruit_farmers, loop)
root.order.add_edge(loop, harvest_plan)
root.order.add_edge(harvest_plan, community_outreach)