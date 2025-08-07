import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
climate_setup = Transition(label='Climate Setup')
sensor_install = Transition(label='Sensor Install')
nutrient_mix = Transition(label='Nutrient Mix')
automation_code = Transition(label='Automation Code')
crop_planning = Transition(label='Crop Planning')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
waste_sort = Transition(label='Waste Sort')
planting_tier = Transition(label='Planting Tier')
harvest_prep = Transition(label='Harvest Prep')
logistics_plan = Transition(label='Logistics Plan')
community_meet = Transition(label='Community Meet')
data_review = Transition(label='Data Review')
system_upgrade = Transition(label='System Upgrade')

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[site_survey, design_layout, climate_setup, sensor_install, nutrient_mix, automation_code, crop_planning, pest_control, energy_audit, waste_sort, planting_tier, harvest_prep, logistics_plan, community_meet, data_review, system_upgrade])

# Define dependencies between activities
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, climate_setup)
root.order.add_edge(site_survey, sensor_install)
root.order.add_edge(site_survey, nutrient_mix)
root.order.add_edge(site_survey, automation_code)
root.order.add_edge(site_survey, crop_planning)
root.order.add_edge(site_survey, pest_control)
root.order.add_edge(site_survey, energy_audit)
root.order.add_edge(site_survey, waste_sort)
root.order.add_edge(site_survey, planting_tier)
root.order.add_edge(site_survey, harvest_prep)
root.order.add_edge(site_survey, logistics_plan)
root.order.add_edge(site_survey, community_meet)
root.order.add_edge(site_survey, data_review)
root.order.add_edge(site_survey, system_upgrade)

# The final POWL model is defined in the 'root' variable