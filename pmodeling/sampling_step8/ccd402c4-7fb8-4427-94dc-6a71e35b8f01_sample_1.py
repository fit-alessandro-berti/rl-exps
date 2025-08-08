import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Permit Filing', 'Stakeholder Meet', 'Design Layout', 'IoT Install', 'Sensor Calibrate', 'Hydroponic Setup', 'Nutrient Mix', 'Seed Sowing', 'Climate Control', 'Data Monitor', 'Yield Forecast', 'Energy Plan', 'Maintenance Plan', 'Harvest Prep', 'Supply Dispatch', 'Market Launch']

# Create the transitions
transitions = [Transition(label=activity) for activity in activities]

# Define the POWL model
site_survey = transitions[0]
permit_filing = transitions[1]
stakeholder_meet = transitions[2]
design_layout = transitions[3]
iot_install = transitions[4]
sensor_calibrate = transitions[5]
hydroponic_setup = transitions[6]
nutrient_mix = transitions[7]
seed_sowing = transitions[8]
climate_control = transitions[9]
data_monitor = transitions[10]
yield_forecast = transitions[11]
energy_plan = transitions[12]
maintenance_plan = transitions[13]
harvest_prep = transitions[14]
supply_dispatch = transitions[15]
market_launch = transitions[16]

root = StrictPartialOrder(nodes=[site_survey, permit_filing, stakeholder_meet, design_layout, iot_install, sensor_calibrate, hydroponic_setup, nutrient_mix, seed_sowing, climate_control, data_monitor, yield_forecast, energy_plan, maintenance_plan, harvest_prep, supply_dispatch, market_launch])

# Define the dependencies between the activities
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(permit_filing, design_layout)
root.order.add_edge(design_layout, iot_install)
root.order.add_edge(iot_install, sensor_calibrate)
root.order.add_edge(sensor_calibrate, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_sowing)
root.order.add_edge(seed_sowing, climate_control)
root.order.add_edge(climate_control, data_monitor)
root.order.add_edge(data_monitor, yield_forecast)
root.order.add_edge(yield_forecast, energy_plan)
root.order.add_edge(energy_plan, maintenance_plan)
root.order.add_edge(maintenance_plan, harvest_prep)
root.order.add_edge(harvest_prep, supply_dispatch)
root.order.add_edge(supply_dispatch, market_launch)

print(root)