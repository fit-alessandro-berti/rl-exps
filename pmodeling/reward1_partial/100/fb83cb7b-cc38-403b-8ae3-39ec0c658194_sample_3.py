import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choices for crop planning and pest monitoring
Crop_Plan_Xor = OperatorPOWL(operator=Operator.XOR, children=[Crop_Plan, Yield_Record])
Pest_Monitor_Xor = OperatorPOWL(operator=Operator.XOR, children=[Pest_Monitor, Impact_Review])

# Define loops for nutrient calibration and community training
Nutrient_Calibrate_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Nutrient_Calibrate])
Community_Train_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Community_Train])

# Define partial order for the entire process
root = StrictPartialOrder(
    nodes=[
        Site_Assess,
        Structure_Check,
        Permit_Obtain,
        Material_Source,
        Soil_Prepare,
        Waterproof_Roof,
        Irrigation_Setup,
        Bed_Assemble,
        Crop_Plan_Xor,
        Pest_Monitor_Xor,
        Nutrient_Calibrate_Loop,
        Community_Train_Loop,
        Harvest_Schedule,
        Community_Train_Loop,
        Yield_Record,
        Impact_Review
    ]
)

# Define dependencies in the partial order
root.order.add_edge(Site_Assess, Structure_Check)
root.order.add_edge(Structure_Check, Permit_Obtain)
root.order.add_edge(Permit_Obtain, Material_Source)
root.order.add_edge(Material_Source, Soil_Prepare)
root.order.add_edge(Soil_Prepare, Waterproof_Roof)
root.order.add_edge(Waterproof_Roof, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Bed_Assemble)
root.order.add_edge(Bed_Assemble, Crop_Plan_Xor)
root.order.add_edge(Crop_Plan_Xor, Pest_Monitor_Xor)
root.order.add_edge(Pest_Monitor_Xor, Nutrient_Calibrate_Loop)
root.order.add_edge(Nutrient_Calibrate_Loop, Community_Train_Loop)
root.order.add_edge(Community_Train_Loop, Harvest_Schedule)
root.order.add_edge(Community_Train_Loop, Community_Train_Loop)
root.order.add_edge(Community_Train_Loop, Yield_Record)
root.order.add_edge(Yield_Record, Impact_Review)