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

# Define the partial order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    iot_setup,
    crop_selection,
    hydroponic_install,
    water_recycling,
    energy_audit,
    plant_scheduling,
    yield_monitoring,
    regulation_review,
    staff_training,
    data_integration,
    supply_setup,
    quality_audit,
    logistics_plan
])

# Add dependencies (if any)
# Example: Add a dependency from 'Site Survey' to 'Structural Check'
root.order.add_edge(site_survey, structural_check)

# Example: Add a dependency from 'IoT Setup' to 'Crop Selection'
root.order.add_edge(iot_setup, crop_selection)

# Example: Add a dependency from 'Hydroponic Install' to 'Water Recycling'
root.order.add_edge(hydroponic_install, water_recycling)

# Example: Add a dependency from 'Energy Audit' to 'Plant Scheduling'
root.order.add_edge(energy_audit, plant_scheduling)

# Example: Add a dependency from 'Yield Monitoring' to 'Regulation Review'
root.order.add_edge(yield_monitoring, regulation_review)

# Example: Add a dependency from 'Staff Training' to 'Data Integration'
root.order.add_edge(staff_training, data_integration)

# Example: Add a dependency from 'Supply Setup' to 'Quality Audit'
root.order.add_edge(supply_setup, quality_audit)

# Example: Add a dependency from 'Logistics Plan' to 'Quality Audit'
root.order.add_edge(logistics_plan, quality_audit)

# You can add more dependencies based on the actual process flow.