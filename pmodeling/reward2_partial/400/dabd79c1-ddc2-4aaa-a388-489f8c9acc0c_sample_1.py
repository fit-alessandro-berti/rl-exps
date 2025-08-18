import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Document_Review = Transition(label='Document Review')
Material_Testing = Transition(label='Material Testing')
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Stylistic_Eval = Transition(label='Stylistic Eval')
Database_Check = Transition(label='Database Check')
Ownership_Audit = Transition(label='Ownership Audit')
Export_Verify = Transition(label='Export Verify')
Expert_Arbitration = Transition(label='Expert Arbitration')
Conservation_Plan = Transition(label='Conservation Plan')
Risk_Assessment = Transition(label='Risk Assessment')
Approval_Review = Transition(label='Approval Review')
Insurance_Setup = Transition(label='Insurance Setup')
Secure_Transport = Transition(label='Secure Transport')
Acquisitions_Meet = Transition(label='Acquisitions Meet')
Final_Documentation = Transition(label='Final Documentation')

# Define partial order
root = StrictPartialOrder(nodes=[
    Document_Review, Material_Testing, Radiocarbon_Date, Stylistic_Eval, Database_Check,
    Ownership_Audit, Export_Verify, Expert_Arbitration, Conservation_Plan, Risk_Assessment,
    Approval_Review, Insurance_Setup, Secure_Transport, Acquisitions_Meet, Final_Documentation
])

# Define dependencies
root.order.add_edge(Document_Review, Material_Testing)
root.order.add_edge(Material_Testing, Radiocarbon_Date)
root.order.add_edge(Material_Testing, Stylistic_Eval)
root.order.add_edge(Radiocarbon_Date, Database_Check)
root.order.add_edge(Stylistic_Eval, Database_Check)
root.order.add_edge(Ownership_Audit, Export_Verify)
root.order.add_edge(Export_Verify, Expert_Arbitration)
root.order.add_edge(Expert_Arbitration, Conservation_Plan)
root.order.add_edge(Conservation_Plan, Risk_Assessment)
root.order.add_edge(Risk_Assessment, Approval_Review)
root.order.add_edge(Approval_Review, Insurance_Setup)
root.order.add_edge(Insurance_Setup, Secure_Transport)
root.order.add_edge(Secure_Transport, Acquisitions_Meet)
root.order.add_edge(Acquisitions_Meet, Final_Documentation)