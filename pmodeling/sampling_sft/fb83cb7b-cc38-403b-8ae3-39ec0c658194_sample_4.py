import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_assess      = Transition(label='Site Assess')
structure_check  = Transition(label='Structure Check')
permit_obtain    = Transition(label='Permit Obtain')
material_source  = Transition(label='Material Source')
soil_prepare     = Transition(label='Soil Prepare')
waterproof_roof  = Transition(label='Waterproof Roof')
irrigation_setup = Transition(label='Irrigation Setup')
bed_assemble     = Transition(label='Bed Assemble')
crop_plan        = Transition(label='Crop Plan')
pest_monitor     = Transition(label='Pest Monitor')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
harvest_schedule = Transition(label='Harvest Schedule')
community_train  = Transition(label='Community Train')
yield_record     = Transition(label='Yield Record')
impact_review    = Transition(label='Impact Review')

# Define the loop body: Pest Monitor -> Nutrient Calibrate
body = StrictPartialOrder(nodes=[pest_monitor, nutrient_calibrate])
# Loop operator: do Pest Monitor, then optionally Nutrient Calibrate and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, nutrient_calibrate])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        site_assess,
        structure_check,
        permit_obtain,
        material_source,
        soil_prepare,
        waterproof_roof,
        irrigation_setup,
        bed_assemble,
        crop_plan,
        loop,
        harvest_schedule,
        community_train,
        yield_record,
        impact_review
    ]
)

# Define the control-flow dependencies
root.order.add_edge(site_assess,    structure_check)
root.order.add_edge(structure_check,permit_obtain)
root.order.add_edge(permit_obtain,  material_source)
root.order.add_edge(material_source,soil_prepare)
root.order.add_edge(soil_prepare,   waterproof_roof)
root.order.add_edge(waterproof_roof,irrigation_setup)
root.order.add_edge(irrigation_setup,bed_assemble)
root.order.add_edge(bed_assemble,   crop_plan)
root.order.add_edge(crop_plan,      loop)
root.order.add_edge(loop,           harvest_schedule)
root.order.add_edge(harvest_schedule,community_train)
root.order.add_edge(community_train,yield_record)
root.order.add_edge(yield_record,impact_review)