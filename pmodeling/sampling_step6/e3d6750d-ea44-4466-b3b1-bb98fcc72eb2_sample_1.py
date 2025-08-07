import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) using the exact names provided
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

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, structural_check, iot_setup, crop_selection, hydroponic_install, water_recycling, energy_audit, plant_scheduling, yield_monitoring, regulation_review, staff_training, data_integration, supply_setup, quality_audit, logistics_plan])

# Define the order (dependencies) between nodes
# For simplicity, we'll assume the order is defined by the sequence of activities provided
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, iot_setup)
root.order.add_edge(site_survey, crop_selection)
root.order.add_edge(site_survey, hydroponic_install)
root.order.add_edge(site_survey, water_recycling)
root.order.add_edge(site_survey, energy_audit)
root.order.add_edge(site_survey, plant_scheduling)
root.order.add_edge(site_survey, yield_monitoring)
root.order.add_edge(site_survey, regulation_review)
root.order.add_edge(site_survey, staff_training)
root.order.add_edge(site_survey, data_integration)
root.order.add_edge(site_survey, supply_setup)
root.order.add_edge(site_survey, quality_audit)
root.order.add_edge(site_survey, logistics_plan)

# The root variable now contains the POWL model for the process