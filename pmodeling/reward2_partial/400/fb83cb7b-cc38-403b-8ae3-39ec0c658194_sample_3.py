import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
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

# Create the POWL model
root = StrictPartialOrder(nodes=[site_assess, structure_check, permit_obtain, material_source, soil_prepare, waterproof_roof, irrigation_setup, bed_assemble, crop_plan, pest_monitor, nutrient_calibrate, harvest_schedule, community_train, yield_record, impact_review])

# Add dependencies to the model
root.order.add_edge(site_assess, structure_check)
root.order.add_edge(structure_check, permit_obtain)
root.order.add_edge(permit_obtain, material_source)
root.order.add_edge(material_source, soil_prepare)
root.order.add_edge(soil_prepare, waterproof_roof)
root.order.add_edge(waterproof_roof, irrigation_setup)
root.order.add_edge(irrigation_setup, bed_assemble)
root.order.add_edge(bed_assemble, crop_plan)
root.order.add_edge(crop_plan, pest_monitor)
root.order.add_edge(pest_monitor, nutrient_calibrate)
root.order.add_edge(nutrient_calibrate, harvest_schedule)
root.order.add_edge(harvest_schedule, community_train)
root.order.add_edge(community_train, yield_record)
root.order.add_edge(yield_record, impact_review)

print(root)