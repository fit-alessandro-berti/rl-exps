import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Site Survey --> Permit Review
site_survey_permits = OperatorPOWL(operator=Operator.XOR, children=[permit_review, skip])
root = StrictPartialOrder(nodes=[site_survey, permit_review, design_layout, material_sourcing, irrigation_setup, sensor_install, structural_test, recruit_farmers, trial_planting, pest_control, soilless_prep, system_calibrate, data_monitor, harvest_plan, community_outreach])
root.order.add_edge(site_survey, site_survey_permits)
root.order.add_edge(permit_review, site_survey_permits)

# Permit Review --> Design Layout
root.order.add_edge(permit_review, design_layout)

# Design Layout --> Material Sourcing
root.order.add_edge(design_layout, material_sourcing)

# Material Sourcing --> Irrigation Setup
root.order.add_edge(material_sourcing, irrigation_setup)

# Irrigation Setup --> Sensor Install
root.order.add_edge(irrigation_setup, sensor_install)

# Sensor Install --> Structural Test
root.order.add_edge(sensor_install, structural_test)

# Structural Test --> Recruit Farmers
root.order.add_edge(structural_test, recruit_farmers)

# Recruit Farmers --> Trial Planting
root.order.add_edge(recruit_farmers, trial_planting)

# Trial Planting --> Pest Control
root.order.add_edge(trial_planting, pest_control)

# Pest Control --> Soilless Prep
root.order.add_edge(pest_control, soilless_prep)

# Soilless Prep --> System Calibrate
root.order.add_edge(soilless_prep, system_calibrate)

# System Calibrate --> Data Monitor
root.order.add_edge(system_calibrate, data_monitor)

# Data Monitor --> Harvest Plan
root.order.add_edge(data_monitor, harvest_plan)

# Harvest Plan --> Community Outreach
root.order.add_edge(harvest_plan, community_outreach)

print(root)