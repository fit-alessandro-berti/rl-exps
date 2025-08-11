import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
Stylistic_Review = Transition(label='Stylistic Review')
Expert_Panel = Transition(label='Expert Panel')
Legal_Clearance = Transition(label='Legal Clearance')
Ethics_Audit = Transition(label='Ethics Audit')
Insurance_Quote = Transition(label='Insurance Quote')
Risk_Assess = Transition(label='Risk Assess')
Digital_Archive = Transition(label='Digital Archive')
Replica_Build = Transition(label='Replica Build')
Transport_Prep = Transition(label='Transport Prep')
Final_Review = Transition(label='Final Review')
Catalog_Entry = Transition(label='Catalog Entry')
Public_Notice = Transition(label='Public Notice')
Condition_Report = Transition(label='Condition Report')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes for activities that need to be repeated
Provenance_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Provenance_Check])
Material_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Material_Testing, Stylistic_Review])
Legal_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Legal_Clearance, Ethics_Audit, Insurance_Quote, Risk_Assess])
Transport_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Transport_Prep, Final_Review])

# Define exclusive choice nodes for activities that are mutually exclusive
Digital_Or_Replica = OperatorPOWL(operator=Operator.XOR, children=[Digital_Archive, Replica_Build])
Transport_Or_Catalog = OperatorPOWL(operator=Operator.XOR, children=[Transport_Prep, Catalog_Entry])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[Provenance_Loop, Material_Loop, Legal_Loop, Transport_Loop, Digital_Or_Replica, Transport_Or_Catalog])
root.order.add_edge(Provenance_Loop, Material_Loop)
root.order.add_edge(Material_Loop, Expert_Panel)
root.order.add_edge(Expert_Panel, Legal_Loop)
root.order.add_edge(Legal_Loop, Transport_Loop)
root.order.add_edge(Transport_Loop, Digital_Or_Replica)
root.order.add_edge(Digital_Or_Replica, Transport_Or_Catalog)
root.order.add_edge(Transport_Or_Catalog, Condition_Report)
root.order.add_edge(Condition_Report, Public_Notice)

print(root)