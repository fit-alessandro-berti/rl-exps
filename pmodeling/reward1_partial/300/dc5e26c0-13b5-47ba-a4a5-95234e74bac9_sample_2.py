import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order structure
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

# Define the dependencies between transitions
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

root.order.add_edge(design_layout, climate_setup)
root.order.add_edge(design_layout, sensor_install)
root.order.add_edge(design_layout, nutrient_mix)
root.order.add_edge(design_layout, automation_code)
root.order.add_edge(design_layout, crop_planning)
root.order.add_edge(design_layout, pest_control)
root.order.add_edge(design_layout, energy_audit)
root.order.add_edge(design_layout, waste_sort)
root.order.add_edge(design_layout, planting_tier)
root.order.add_edge(design_layout, harvest_prep)
root.order.add_edge(design_layout, logistics_plan)
root.order.add_edge(design_layout, community_meet)
root.order.add_edge(design_layout, data_review)
root.order.add_edge(design_layout, system_upgrade)

root.order.add_edge(climate_setup, sensor_install)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(climate_setup, automation_code)
root.order.add_edge(climate_setup, crop_planning)
root.order.add_edge(climate_setup, pest_control)
root.order.add_edge(climate_setup, energy_audit)
root.order.add_edge(climate_setup, waste_sort)
root.order.add_edge(climate_setup, planting_tier)
root.order.add_edge(climate_setup, harvest_prep)
root.order.add_edge(climate_setup, logistics_plan)
root.order.add_edge(climate_setup, community_meet)
root.order.add_edge(climate_setup, data_review)
root.order.add_edge(climate_setup, system_upgrade)

root.order.add_edge(sensor_install, nutrient_mix)
root.order.add_edge(sensor_install, automation_code)
root.order.add_edge(sensor_install, crop_planning)
root.order.add_edge(sensor_install, pest_control)
root.order.add_edge(sensor_install, energy_audit)
root.order.add_edge(sensor_install, waste_sort)
root.order.add_edge(sensor_install, planting_tier)
root.order.add_edge(sensor_install, harvest_prep)
root.order.add_edge(sensor_install, logistics_plan)
root.order.add_edge(sensor_install, community_meet)
root.order.add_edge(sensor_install, data_review)
root.order.add_edge(sensor_install, system_upgrade)

root.order.add_edge(nutrient_mix, automation_code)
root.order.add_edge(nutrient_mix, crop_planning)
root.order.add_edge(nutrient_mix, pest_control)
root.order.add_edge(nutrient_mix, energy_audit)
root.order.add_edge(nutrient_mix, waste_sort)
root.order.add_edge(nutrient_mix, planting_tier)
root.order.add_edge(nutrient_mix, harvest_prep)
root.order.add_edge(nutrient_mix, logistics_plan)
root.order.add_edge(nutrient_mix, community_meet)
root.order.add_edge(nutrient_mix, data_review)
root.order.add_edge(nutrient_mix, system_upgrade)

root.order.add_edge(automation_code, crop_planning)
root.order.add_edge(automation_code, pest_control)
root.order.add_edge(automation_code, energy_audit)
root.order.add_edge(automation_code, waste_sort)
root.order.add_edge(automation_code, planting_tier)
root.order.add_edge(automation_code, harvest_prep)
root.order.add_edge(automation_code, logistics_plan)
root.order.add_edge(automation_code, community_meet)
root.order.add_edge(automation_code, data_review)
root.order.add_edge(automation_code, system_upgrade)

root.order.add_edge(crop_planning, pest_control)
root.order.add_edge(crop_planning, energy_audit)
root.order.add_edge(crop_planning, waste_sort)
root.order.add_edge(crop_planning, planting_tier)
root.order.add_edge(crop_planning, harvest_prep)
root.order.add_edge(crop_planning, logistics_plan)
root.order.add_edge(crop_planning, community_meet)
root.order.add_edge(crop_planning, data_review)
root.order.add_edge(crop_planning, system_upgrade)

root.order.add_edge(pest_control, energy_audit)
root.order.add_edge(pest_control, waste_sort)
root.order.add_edge(pest_control, planting_tier)
root.order.add_edge(pest_control, harvest_prep)
root.order.add_edge(pest_control, logistics_plan)
root.order.add_edge(pest_control, community_meet)
root.order.add_edge(pest_control, data_review)
root.order.add_edge(pest_control, system_upgrade)

root.order.add_edge(energy_audit, waste_sort)
root.order.add_edge(energy_audit, planting_tier)
root.order.add_edge(energy_audit, harvest_prep)
root.order.add_edge(energy_audit, logistics_plan)
root.order.add_edge(energy_audit, community_meet)
root.order.add_edge(energy_audit, data_review)
root.order.add_edge(energy_audit, system_upgrade)

root.order.add_edge(waste_sort, planting_tier)
root.order.add_edge(waste_sort, harvest_prep)
root.order.add_edge(waste_sort, logistics_plan)
root.order.add_edge(waste_sort, community_meet)
root.order.add_edge(waste_sort, data_review)
root.order.add_edge(waste_sort, system_upgrade)

root.order.add_edge(planting_tier, harvest_prep)
root.order.add_edge(planting_tier, logistics_plan)
root.order.add_edge(planting_tier, community_meet)
root.order.add_edge(planting_tier, data_review)
root.order.add_edge(planting_tier, system_upgrade)

root.order.add_edge(harvest_prep, logistics_plan)
root.order.add_edge(harvest_prep, community_meet)
root.order.add_edge(harvest_prep, data_review)
root.order.add_edge(harvest_prep, system_upgrade)

root.order.add_edge(logistics_plan, community_meet)
root.order.add_edge(logistics_plan, data_review)
root.order.add_edge(logistics_plan, system_upgrade)

root.order.add_edge(community_meet, data_review)
root.order.add_edge(community_meet, system_upgrade)

root.order.add_edge(data_review, system_upgrade)

print(root)