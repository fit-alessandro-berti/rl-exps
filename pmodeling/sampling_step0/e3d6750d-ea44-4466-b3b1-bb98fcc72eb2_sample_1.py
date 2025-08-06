import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_check])
iot_loop = OperatorPOWL(operator=Operator.LOOP, children=[iot_setup, crop_selection])
hydroponic_loop = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_install, water_recycling])
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, plant_scheduling])
yield_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitoring, regulation_review])
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, data_integration])
supply_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_setup, quality_audit])
logistics_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan, site_survey])

root = StrictPartialOrder(nodes=[site_survey_loop, iot_loop, hydroponic_loop, energy_audit_loop, yield_monitoring_loop, staff_training_loop, supply_setup_loop, logistics_plan_loop])
root.order.add_edge(site_survey_loop, iot_loop)
root.order.add_edge(iot_loop, hydroponic_loop)
root.order.add_edge(hydroponic_loop, energy_audit_loop)
root.order.add_edge(energy_audit_loop, yield_monitoring_loop)
root.order.add_edge(yield_monitoring_loop, staff_training_loop)
root.order.add_edge(staff_training_loop, supply_setup_loop)
root.order.add_edge(supply_setup_loop, logistics_plan_loop)

print(root)