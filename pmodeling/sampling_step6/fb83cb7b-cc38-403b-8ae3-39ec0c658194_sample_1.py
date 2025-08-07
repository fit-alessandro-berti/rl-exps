import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_assess = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
permit_obtain = Transition(label='Permit Obtain')
material_source = Transition(label='Material Source')
soil_prepare = Transition(label='Soil Prepare')
waterproof_roof = Transition(label='Waterproof Roof')
irrigation_setup = Transition(label='Irrigation Setup')
bed_assemble = Transition(label='Bed Assemble')
crop_plan = Transition(label='Crop Plan')
pest_monitor = Transition(label='Pest Monitor')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
harvest_schedule = Transition(label='Harvest Schedule')
community_train = Transition(label='Community Train')
yield_record = Transition(label='Yield Record')
impact_review = Transition(label='Impact Review')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    site_assess,
    structure_check,
    permit_obtain,
    material_source,
    soil_prepare,
    waterproof_roof,
    irrigation_setup,
    bed_assemble,
    crop_plan,
    pest_monitor,
    nutrient_calibrate,
    harvest_schedule,
    community_train,
    yield_record,
    impact_review
])

# Optionally, define dependencies if any are specified in the process description
# For example, if there are dependencies, you can add them like this:
# root.order.add_edge(site_assess, structure_check)
# root.order.add_edge(site_assess, permit_obtain)
# ...

# The 'root' variable now contains the POWL model for the urban rooftop farming process