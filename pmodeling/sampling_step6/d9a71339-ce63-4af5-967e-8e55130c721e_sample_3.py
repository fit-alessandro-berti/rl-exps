import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions based on the given activities
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
modular_install = Transition(label='Modular Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_setup = Transition(label='Sensor Setup')
ai_training = Transition(label='AI Training')
data_capture = Transition(label='Data Capture')
maintenance_plan = Transition(label='Maintenance Plan')
pest_scan = Transition(label='Pest Scan')
growth_monitor = Transition(label='Growth Monitor')
harvest_sync = Transition(label='Harvest Sync')
quality_test = Transition(label='Quality Test')
package_prep = Transition(label='Package Prep')
logistics_plan = Transition(label='Logistics Plan')

# Define the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    modular_install,
    hydroponic_setup,
    nutrient_mix,
    sensor_setup,
    ai_training,
    data_capture,
    maintenance_plan,
    pest_scan,
    growth_monitor,
    harvest_sync,
    quality_test,
    package_prep,
    logistics_plan
])

# Since there are no dependencies mentioned in the description, the workflow is fully concurrent
# Therefore, there is no need to define any edges in the partial order

# Save the final result in the variable 'root'
print(root)