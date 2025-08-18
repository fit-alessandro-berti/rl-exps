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

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, staff_training])
loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, hydroponic_install, water_recycling, energy_audit, plant_scheduling, yield_monitoring, data_integration, supply_setup, quality_audit, logistics_plan])

# Define the POWL model
root = StrictPartialOrder(nodes=[site_survey, structural_check, iot_setup, exclusive_choice, loop])
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, iot_setup)
root.order.add_edge(iot_setup, exclusive_choice)
root.order.add_edge(exclusive_choice, loop)
root.order.add_edge(loop, exclusive_choice)