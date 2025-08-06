import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[skip1, equipment_buy])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[skip2, solar_install])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[skip3, staff_train])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[skip4, maintenance_plan])

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, skip5])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip5])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, load_test, climate_study, permit_check, system_design, loop1, loop2, loop3, loop4, xor1, xor2, equipment_buy, solar_install, staff_train, maintenance_plan, community_meet])

# Define partial order dependencies
root.order.add_edge(site_survey, load_test)
root.order.add_edge(load_test, climate_study)
root.order.add_edge(climate_study, permit_check)
root.order.add_edge(permit_check, system_design)
root.order.add_edge(system_design, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop3, xor2)
root.order.add_edge(loop4, xor1)
root.order.add_edge(loop4, xor2)
root.order.add_edge(xor1, crop_harvest)
root.order.add_edge(xor1, skip5)
root.order.add_edge(xor2, community_meet)
root.order.add_edge(xor2, skip5)

# Print the root POWL model
print(root)