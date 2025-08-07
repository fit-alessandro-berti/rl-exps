import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
iot_setup        = Transition(label='IoT Setup')
crop_selection   = Transition(label='Crop Selection')
hydroponic_install = Transition(label='Hydroponic Install')
water_recycling  = Transition(label='Water Recycling')
energy_audit     = Transition(label='Energy Audit')
plant_scheduling = Transition(label='Plant Scheduling')
yield_monitoring = Transition(label='Yield Monitoring')
regulation_review= Transition(label='Regulation Review')
staff_training   = Transition(label='Staff Training')
data_integration = Transition(label='Data Integration')
supply_setup     = Transition(label='Supply Setup')
logistics_plan   = Transition(label='Logistics Plan')
quality_audit    = Transition(label='Quality Audit')

# Loop for continuous monitoring and scheduling
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitoring, data_integration])

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
    monitoring_loop,
    regulation_review,
    staff_training,
    supply_setup,
    logistics_plan,
    quality_audit
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, iot_setup)
root.order.add_edge(iot_setup, crop_selection)
root.order.add_edge(crop_selection, hydroponic_install)
root.order.add_edge(hydroponic_install, water_recycling)
root.order.add_edge(water_recycling, energy_audit)
root.order.add_edge(energy_audit, plant_scheduling)
root.order.add_edge(plant_scheduling, monitoring_loop)
root.order.add_edge(monitoring_loop, regulation_review)
root.order.add_edge(regulation_review, staff_training)
root.order.add_edge(staff_training, supply_setup)
root.order.add_edge(supply_setup, logistics_plan)
root.order.add_edge(logistics_plan, quality_audit)