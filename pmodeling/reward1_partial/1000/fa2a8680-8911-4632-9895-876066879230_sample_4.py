import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Client_Meet = Transition(label='Client Meet')
Requirement_Gather = Transition(label='Requirement Gather')
Module_Design = Transition(label='Module Design')
Supplier_Vetting = Transition(label='Supplier Vetting')
Component_Order = Transition(label='Component Order')
Prototype_Build = Transition(label='Prototype Build')
Field_Testing = Transition(label='Field Testing')
Test_Analysis = Transition(label='Test Analysis')
Software_Setup = Transition(label='Software Setup')
Data_Integration = Transition(label='Data Integration')
Pilot_Train = Transition(label='Pilot Train')
Compliance_Check = Transition(label='Compliance Check')
Fleet_Deploy = Transition(label='Fleet Deploy')
Remote_Monitor = Transition(label='Remote Monitor')
Maintenance_Plan = Transition(label='Maintenance Plan')
Performance_Tune = Transition(label='Performance Tune')

# Define the control flow
client_meet = OperatorPOWL(operator=Operator.SEQUENCE, children=[Client_Meet, Requirement_Gather])
module_design = OperatorPOWL(operator=Operator.SEQUENCE, children=[Module_Design, Supplier_Vetting, Component_Order, Prototype_Build, Field_Testing, Test_Analysis])
software_setup = OperatorPOWL(operator=Operator.SEQUENCE, children=[Software_Setup, Data_Integration, Pilot_Train, Compliance_Check, Fleet_Deploy])
monitoring = OperatorPOWL(operator=Operator.SEQUENCE, children=[Remote_Monitor, Maintenance_Plan, Performance_Tune])

# Create the root node
root = StrictPartialOrder(nodes=[client_meet, module_design, software_setup, monitoring])
root.order.add_edge(client_meet, module_design)
root.order.add_edge(module_design, software_setup)
root.order.add_edge(software_setup, monitoring)

# Print the root node
print(root)