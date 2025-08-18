import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, iot_setup, crop_selection, hydroponic_install,
    water_recycling, energy_audit, plant_scheduling, yield_monitoring, regulation_review,
    staff_training, data_integration, supply_setup, quality_audit, logistics_plan
])

# Define dependencies between activities
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, iot_setup)
root.order.add_edge(iot_setup, crop_selection)
root.order.add_edge(crop_selection, hydroponic_install)
root.order.add_edge(hydroponic_install, water_recycling)
root.order.add_edge(water_recycling, energy_audit)
root.order.add_edge(energy_audit, plant_scheduling)
root.order.add_edge(plant_scheduling, yield_monitoring)
root.order.add_edge(yield_monitoring, regulation_review)
root.order.add_edge(regulation_review, staff_training)
root.order.add_edge(staff_training, data_integration)
root.order.add_edge(data_integration, supply_setup)
root.order.add_edge(supply_setup, quality_audit)
root.order.add_edge(quality_audit, logistics_plan)

# Print the final POWL model
print(root)