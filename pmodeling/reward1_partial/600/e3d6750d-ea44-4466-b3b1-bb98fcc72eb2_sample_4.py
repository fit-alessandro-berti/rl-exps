import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (site_survey, structural_check),
        (structural_check, iot_setup),
        (iot_setup, crop_selection),
        (crop_selection, hydroponic_install),
        (hydroponic_install, water_recycling),
        (water_recycling, energy_audit),
        (energy_audit, plant_scheduling),
        (plant_scheduling, yield_monitoring),
        (yield_monitoring, regulation_review),
        (regulation_review, staff_training),
        (staff_training, data_integration),
        (data_integration, supply_setup),
        (supply_setup, quality_audit),
        (quality_audit, logistics_plan)
    ]
)

# Print the POWL model (optional)
print(root)