from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Site_Review = Transition(label='Site Review')
Impact_Study = Transition(label='Impact Study')
Design_Plan = Transition(label='Design Plan')
Structure_Mod = Transition(label='Structure Mod')
Hydroponics_Setup = Transition(label='Hydroponics Setup')
Crop_Select = Transition(label='Crop Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')
Sensor_Install = Transition(label='Sensor Install')
Staff_Train = Transition(label='Staff Train')
Compliance_Audit = Transition(label='Compliance Audit')
Packaging_Dev = Transition(label='Packaging Dev')
Logistics_Plan = Transition(label='Logistics Plan')
Community_Engage = Transition(label='Community Engage')
Sustainability_Check = Transition(label='Sustainability Check')

# Create the partial order model
root = StrictPartialOrder(nodes=[
    Site_Review,
    Impact_Study,
    Design_Plan,
    Structure_Mod,
    Hydroponics_Setup,
    Crop_Select,
    Nutrient_Mix,
    Pest_Control,
    Sensor_Install,
    Staff_Train,
    Compliance_Audit,
    Packaging_Dev,
    Logistics_Plan,
    Community_Engage,
    Sustainability_Check
])

# Define the order of execution
root.order.add_edge(Site_Review, Impact_Study)
root.order.add_edge(Impact_Study, Design_Plan)
root.order.add_edge(Design_Plan, Structure_Mod)
root.order.add_edge(Structure_Mod, Hydroponics_Setup)
root.order.add_edge(Hydroponics_Setup, Crop_Select)
root.order.add_edge(Crop_Select, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Pest_Control)
root.order.add_edge(Pest_Control, Sensor_Install)
root.order.add_edge(Sensor_Install, Staff_Train)
root.order.add_edge(Staff_Train, Compliance_Audit)
root.order.add_edge(Compliance_Audit, Packaging_Dev)
root.order.add_edge(Packaging_Dev, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Community_Engage)
root.order.add_edge(Community_Engage, Sustainability_Check)

print(root)