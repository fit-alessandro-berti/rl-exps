import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey       = Transition(label='Site Survey')
structural_check  = Transition(label='Structural Check')
iot_setup         = Transition(label='IoT Setup')
crop_selection    = Transition(label='Crop Selection')
hydroponic_install= Transition(label='Hydroponic Install')
water_recycling   = Transition(label='Water Recycling')
energy_audit      = Transition(label='Energy Audit')
plant_scheduling  = Transition(label='Plant Scheduling')
yield_monitoring  = Transition(label='Yield Monitoring')
regulation_review = Transition(label='Regulation Review')
staff_training    = Transition(label='Staff Training')
data_integration  = Transition(label='Data Integration')
supply_setup      = Transition(label='Supply Setup')
logistics_plan    = Transition(label='Logistics Plan')
quality_audit     = Transition(label='Quality Audit')

# Silent transition for loop exit
skip = SilentTransition()

# Define the loop for continuous monitoring and yield analysis
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_monitoring, skip]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    iot_setup,
    crop_selection,
    hydroponic_install,
    water_recycling,
    energy_audit,
    plant_scheduling,
    regulation_review,
    staff_training,
    data_integration,
    supply_setup,
    logistics_plan,
    monitor_loop,
    quality_audit
])

# Add the control-flow dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, iot_setup)
root.order.add_edge(iot_setup, crop_selection)
root.order.add_edge(crop_selection, hydroponic_install)
root.order.add_edge(hydroponic_install, water_recycling)
root.order.add_edge(water_recycling, energy_audit)
root.order.add_edge(energy_audit, plant_scheduling)
root.order.add_edge(plant_scheduling, regulation_review)
root.order.add_edge(regulation_review, staff_training)
root.order.add_edge(staff_training, data_integration)
root.order.add_edge(data_integration, supply_setup)
root.order.add_edge(supply_setup, logistics_plan)
root.order.add_edge(logistics_plan, monitor_loop)
root.order.add_edge(monitor_loop, quality_audit)

# Finalize the loop structure
root.order.add_edge(monitor_loop, monitor_loop)  # Loop back to itself
root.order.add_edge(quality_audit, skip)  # Exit the loop on quality audit