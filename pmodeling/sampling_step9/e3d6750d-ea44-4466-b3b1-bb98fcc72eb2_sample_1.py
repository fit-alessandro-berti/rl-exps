import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
iot_setup = Transition(label='IoT Setup')
crop_selection = Transition(label='Crop Selection')
hydroponic_install = Transition(label='Hydroponic Install')
water_recycling = Transition(label='Water Recycling')
energy_audit = Transition(label='Energy Audit')
plant_scheduling = Transition(label='Plant Scheduling')
yield_monitoring = Transition(label='Yield Monitoring')
regulation_review = Transition(label='Regulation Review')
staff_training = Transition(label='Staff Training')
data_integration = Transition(label='Data Integration')
supply_setup = Transition(label='Supply Setup')
quality_audit = Transition(label='Quality Audit')
logistics_plan = Transition(label='Logistics Plan')

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_check])
loop_iot_setup = OperatorPOWL(operator=Operator.LOOP, children=[iot_setup, crop_selection])
loop_hydroponic_install = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_install, water_recycling])
loop_energy_audit = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, plant_scheduling])
loop_yield_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitoring, regulation_review])
loop_staff_training = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, data_integration])
loop_supply_setup = OperatorPOWL(operator=Operator.LOOP, children=[supply_setup, quality_audit])
loop_logistics_plan = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan, skip])

root = StrictPartialOrder(nodes=[loop_site_survey, loop_iot_setup, loop_hydroponic_install, loop_energy_audit, loop_yield_monitoring, loop_staff_training, loop_supply_setup, loop_logistics_plan])
root.order.add_edge(loop_site_survey, loop_iot_setup)
root.order.add_edge(loop_iot_setup, loop_hydroponic_install)
root.order.add_edge(loop_hydroponic_install, loop_energy_audit)
root.order.add_edge(loop_energy_audit, loop_yield_monitoring)
root.order.add_edge(loop_yield_monitoring, loop_staff_training)
root.order.add_edge(loop_staff_training, loop_supply_setup)
root.order.add_edge(loop_supply_setup, loop_logistics_plan)