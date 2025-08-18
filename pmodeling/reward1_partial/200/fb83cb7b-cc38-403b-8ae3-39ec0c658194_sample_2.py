import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
Site_Assess = Transition(label='Site Assess')
Structure_Check = Transition(label='Structure Check')
Permit_Obtain = Transition(label='Permit Obtain')
Material_Source = Transition(label='Material Source')
Soil_Prepare = Transition(label='Soil Prepare')
Waterproof_Roof = Transition(label='Waterproof Roof')
Irrigation_Setup = Transition(label='Irrigation Setup')
Bed_Assemble = Transition(label='Bed Assemble')
Crop_Plan = Transition(label='Crop Plan')
Pest_Monitor = Transition(label='Pest Monitor')
Nutrient_Calibrate = Transition(label='Nutrient Calibrate')
Harvest_Schedule = Transition(label='Harvest Schedule')
Community_Train = Transition(label='Community Train')
Yield_Record = Transition(label='Yield Record')
Impact_Review = Transition(label='Impact Review')

# Define silent transitions for concurrency
skip = SilentTransition()

# Define loop and choice nodes
loop_structure_check = OperatorPOWL(operator=Operator.LOOP, children=[Structure_Check])
choice_permit_obtain_material_source = OperatorPOWL(operator=Operator.XOR, children=[Permit_Obtain, Material_Source])
choice_soil_prepare_waterproof_roof = OperatorPOWL(operator=Operator.XOR, children=[Soil_Prepare, Waterproof_Roof])
choice_irrigation_setup_bed_assemble = OperatorPOWL(operator=Operator.XOR, children=[Irrigation_Setup, Bed_Assemble])

# Define the root node with the entire process structure
root = StrictPartialOrder(nodes=[
    loop_structure_check,
    choice_permit_obtain_material_source,
    choice_soil_prepare_waterproof_roof,
    choice_irrigation_setup_bed_assemble,
    Crop_Plan,
    Pest_Monitor,
    Nutrient_Calibrate,
    Harvest_Schedule,
    Community_Train,
    Yield_Record,
    Impact_Review
])
root.order.add_edge(loop_structure_check, choice_permit_obtain_material_source)
root.order.add_edge(loop_structure_check, choice_soil_prepare_waterproof_roof)
root.order.add_edge(choice_permit_obtain_material_source, choice_irrigation_setup_bed_assemble)
root.order.add_edge(choice_soil_prepare_waterproof_roof, choice_irrigation_setup_bed_assemble)
root.order.add_edge(choice_irrigation_setup_bed_assemble, Crop_Plan)
root.order.add_edge(choice_irrigation_setup_bed_assemble, Pest_Monitor)
root.order.add_edge(choice_irrigation_setup_bed_assemble, Nutrient_Calibrate)
root.order.add_edge(choice_irrigation_setup_bed_assemble, Harvest_Schedule)
root.order.add_edge(Crop_Plan, Community_Train)
root.order.add_edge(Crop_Plan, Yield_Record)
root.order.add_edge(Crop_Plan, Impact_Review)

print(root)