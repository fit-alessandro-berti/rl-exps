import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey      = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
iot_setup        = Transition(label='IoT Setup')
crop_selection   = Transition(label='Crop Selection')
hydroponic_install = Transition(label='Hydroponic Install')
water_recycling  = Transition(label='Water Recycling')
energy_audit     = Transition(label='Energy Audit')
plant_scheduling = Transition(label='Plant Scheduling')
yield_monitoring = Transition(label='Yield Monitoring')
regulation_review = Transition(label='Regulation Review')
staff_training   = Transition(label='Staff Training')
data_integration = Transition(label='Data Integration')
supply_setup     = Transition(label='Supply Setup')
quality_audit    = Transition(label='Quality Audit')
logistics_plan   = Transition(label='Logistics Plan')

# Loop for continuous yield monitoring and data integration
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_monitoring, data_integration]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, iot_setup,
    crop_selection, hydroponic_install, water_recycling, energy_audit,
    plant_scheduling, monitor_loop,
    regulation_review, staff_training,
    supply_setup, quality_audit, logistics_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, iot_setup)
root.order.add_edge(iot_setup, crop_selection)
root.order.add_edge(crop_selection, hydroponic_install)
root.order.add_edge(hydroponic_install, water_recycling)
root.order.add_edge(water_recycling, energy_audit)
root.order.add_edge(energy_audit, plant_scheduling)
root.order.add_edge(plant_scheduling, monitor_loop)
root.order.add_edge(monitor_loop, regulation_review)
root.order.add_edge(regulation_review, staff_training)
root.order.add_edge(staff_training, supply_setup)
root.order.add_edge(supply_setup, quality_audit)
root.order.add_edge(quality_audit, logistics_plan)