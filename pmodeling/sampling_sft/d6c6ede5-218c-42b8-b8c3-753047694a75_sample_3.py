import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
load_test        = Transition(label='Load Test')
climate_study    = Transition(label='Climate Study')
permit_check     = Transition(label='Permit Check')
system_design    = Transition(label='System Design')
equipment_buy    = Transition(label='Equipment Buy')
sensor_setup     = Transition(label='Sensor Setup')
irrigation_fit   = Transition(label='Irrigation Fit')
solar_install    = Transition(label='Solar Install')
staff_train      = Transition(label='Staff Train')
pilot_plant      = Transition(label='Pilot Plant')
data_monitor     = Transition(label='Data Monitor')
crop_harvest     = Transition(label='Crop Harvest')
maintenance_plan = Transition(label='Maintenance Plan')
community_meet   = Transition(label='Community Meet')

# Define the loop for continuous monitoring and crop management
loop_body = StrictPartialOrder(nodes=[data_monitor, crop_harvest, maintenance_plan])
loop_body.order.add_edge(data_monitor, crop_harvest)
loop_body.order.add_edge(crop_harvest, maintenance_plan)

loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_plant, loop_body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, climate_study, permit_check,
    system_design, equipment_buy, sensor_setup, irrigation_fit,
    solar_install, staff_train, loop, community_meet
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(load_test, permit_check)
root.order.add_edge(climate_study, permit_check)
root.order.add_edge(permit_check, system_design)
root.order.add_edge(system_design, equipment_buy)
root.order.add_edge(system_design, sensor_setup)
root.order.add_edge(system_design, irrigation_fit)
root.order.add_edge(system_design, solar_install)
root.order.add_edge(equipment_buy, staff_train)
root.order.add_edge(sensor_setup, staff_train)
root.order.add_edge(irrigation_fit, staff_train)
root.order.add_edge(solar_install, staff_train)
root.order.add_edge(staff_train, loop)
root.order.add_edge(loop, community_meet)