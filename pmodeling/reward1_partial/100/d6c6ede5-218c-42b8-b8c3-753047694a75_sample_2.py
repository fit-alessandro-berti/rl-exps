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

# Define exclusive choice for permit check and system design
permit_system = OperatorPOWL(operator=Operator.XOR, children=[permit_check, system_design])

# Define loop for equipment buy and sensor setup
equipment_sensor = OperatorPOWL(operator=Operator.LOOP, children=[equipment_buy, sensor_setup])

# Define loop for irrigation fit and solar install
irrigation_solar = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_fit, solar_install])

# Define loop for staff train and pilot plant
staff_pilot = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, pilot_plant])

# Define loop for data monitor and crop harvest
data_crop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, crop_harvest])

# Define loop for maintenance plan and community meet
maintenance_community = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, community_meet])

# Define the root process
root = StrictPartialOrder(nodes=[site_survey, load_test, climate_study, permit_system, equipment_sensor, irrigation_solar, staff_pilot, data_crop, maintenance_community])
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(load_test, permit_system)
root.order.add_edge(climate_study, permit_system)
root.order.add_edge(permit_system, system_design)
root.order.add_edge(system_design, equipment_sensor)
root.order.add_edge(equipment_sensor, irrigation_solar)
root.order.add_edge(irrigation_solar, staff_pilot)
root.order.add_edge(staff_pilot, data_crop)
root.order.add_edge(data_crop, maintenance_community)
root.order.add_edge(maintenance_community, community_meet)