import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
climate_study = Transition(label='Climate Study')
permit_check = Transition(label='Permit Check')
system_design = Transition(label='System Design')
equipment_buy = Transition(label='Equipment Buy')
sensor_setup = Transition(label='Sensor Setup')
irrigation_fit = Transition(label='Irrigation Fit')
solar_install = Transition(label='Solar Install')
staff_train = Transition(label='Staff Train')
pilot_plant = Transition(label='Pilot Plant')
data_monitor = Transition(label='Data Monitor')
crop_harvest = Transition(label='Crop Harvest')
maintenance_plan = Transition(label='Maintenance Plan')
community_meet = Transition(label='Community Meet')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    site_survey, load_test, climate_study, permit_check, system_design,
    equipment_buy, sensor_setup, irrigation_fit, solar_install, staff_train,
    pilot_plant, data_monitor, crop_harvest, maintenance_plan, community_meet
])

# Define the dependencies between activities
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(load_test, system_design)
root.order.add_edge(load_test, equipment_buy)
root.order.add_edge(climate_study, system_design)
root.order.add_edge(climate_study, sensor_setup)
root.order.add_edge(climate_study, irrigation_fit)
root.order.add_edge(climate_study, solar_install)
root.order.add_edge(climate_study, staff_train)
root.order.add_edge(climate_study, pilot_plant)
root.order.add_edge(climate_study, data_monitor)
root.order.add_edge(climate_study, crop_harvest)
root.order.add_edge(climate_study, maintenance_plan)
root.order.add_edge(climate_study, community_meet)

print(root)