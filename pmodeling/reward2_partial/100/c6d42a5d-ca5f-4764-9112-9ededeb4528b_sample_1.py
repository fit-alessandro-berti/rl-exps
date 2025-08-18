import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Soil_Sample = Transition(label='Soil Sample')
Crop_Select = Transition(label='Crop Select')
Irrigation_Plan = Transition(label='Irrigation Plan')
Permit_Apply = Transition(label='Permit Apply')
Material_Order = Transition(label='Material Order')
Bed_Install = Transition(label='Bed Install')
Pest_Control = Transition(label='Pest Control')
Solar_Setup = Transition(label='Solar Setup')
Staff_Train = Transition(label='Staff Train')
Market_Outreach = Transition(label='Market Outreach')
System_Setup = Transition(label='System Setup')
Supplier_Contact = Transition(label='Supplier Contact')
Health_Monitor = Transition(label='Health Monitor')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Load_Test, Soil_Sample, Crop_Select, Irrigation_Plan,
    Permit_Apply, Material_Order, Bed_Install, Pest_Control, Solar_Setup,
    Staff_Train, Market_Outreach, System_Setup, Supplier_Contact, Health_Monitor
])

# Define the order dependencies
root.order.add_edge(Site_Survey, Load_Test)
root.order.add_edge(Site_Survey, Soil_Sample)
root.order.add_edge(Soil_Sample, Crop_Select)
root.order.add_edge(Crop_Select, Irrigation_Plan)
root.order.add_edge(Permit_Apply, Material_Order)
root.order.add_edge(Material_Order, Bed_Install)
root.order.add_edge(Bed_Install, Pest_Control)
root.order.add_edge(Pest_Control, Solar_Setup)
root.order.add_edge(Solar_Setup, Staff_Train)
root.order.add_edge(Staff_Train, Market_Outreach)
root.order.add_edge(Market_Outreach, System_Setup)
root.order.add_edge(System_Setup, Supplier_Contact)
root.order.add_edge(Supplier_Contact, Health_Monitor)

print(root)