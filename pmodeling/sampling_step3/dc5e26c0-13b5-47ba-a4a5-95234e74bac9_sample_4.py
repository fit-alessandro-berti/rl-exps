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

# Create a StrictPartialOrder model
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    climate_setup,
    sensor_install,
    nutrient_mix,
    automation_code,
    crop_planning,
    pest_control,
    energy_audit,
    waste_sort,
    planting_tier,
    harvest_prep,
    logistics_plan,
    community_meet,
    data_review,
    system_upgrade
])

# Define dependencies between activities
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, climate_setup)
root.order.add_edge(climate_setup, sensor_install)
root.order.add_edge(sensor_install, nutrient_mix)
root.order.add_edge(nutrient_mix, automation_code)
root.order.add_edge(automation_code, crop_planning)
root.order.add_edge(crop_planning, pest_control)
root.order.add_edge(pest_control, energy_audit)
root.order.add_edge(energy_audit, waste_sort)
root.order.add_edge(waste_sort, planting_tier)
root.order.add_edge(planting_tier, harvest_prep)
root.order.add_edge(harvest_prep, logistics_plan)
root.order.add_edge(logistics_plan, community_meet)
root.order.add_edge(community_meet, data_review)
root.order.add_edge(data_review, system_upgrade)

# The final result is saved in the variable 'root'