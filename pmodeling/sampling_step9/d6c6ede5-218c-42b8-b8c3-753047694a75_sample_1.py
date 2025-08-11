import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Site Survey, Load Test, Climate Study, Permit Check
site_check = OperatorPOWL(operator=Operator.XOR, children=[site_survey, load_test, climate_study, permit_check])

# System Design, Equipment Buy, Sensor Setup, Irrigation Fit, Solar Install, Staff Train
system_setup = OperatorPOWL(operator=Operator.XOR, children=[system_design, equipment_buy, sensor_setup, irrigation_fit, solar_install, staff_train])

# Pilot Plant, Data Monitor, Crop Harvest, Maintenance Plan, Community Meet
pilot_plant_data = OperatorPOWL(operator=Operator.XOR, children=[pilot_plant, data_monitor, crop_harvest, maintenance_plan, community_meet])

root = StrictPartialOrder(nodes=[site_check, system_setup, pilot_plant_data])
root.order.add_edge(site_check, system_setup)
root.order.add_edge(system_setup, pilot_plant_data)