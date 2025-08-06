from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Collection_Survey = Transition(label='Collection Survey')
Provenance_Check = Transition(label='Provenance Check')
Legal_Review = Transition(label='Legal Review')
Scientific_Test = Transition(label='Scientific Test')
Material_Analysis = Transition(label='Material Analysis')
Ownership_Audit = Transition(label='Ownership Audit')
Ethical_Screening = Transition(label='Ethical Screening')
Condition_Report = Transition(label='Condition Report')
Expert_Consultation = Transition(label='Expert Consultation')
Transport_Planning = Transition(label='Transport Planning')
Secure_Packing = Transition(label='Secure Packing')
Customs_Clearance = Transition(label='Customs Clearance')
Insurance_Setup = Transition(label='Insurance Setup')
Exhibit_Preparation = Transition(label='Exhibit Preparation')
Final_Approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define POWL model
root = StrictPartialOrder()

# Define partial order nodes and their dependencies
root.nodes = [Collection_Survey, Provenance_Check, Legal_Review, Scientific_Test, Material_Analysis, Ownership_Audit, Ethical_Screening, Condition_Report, Expert_Consultation, Transport_Planning, Secure_Packing, Customs_Clearance, Insurance_Setup, Exhibit_Preparation, Final_Approval]

# Define dependencies between nodes
root.order.add_edge(Collection_Survey, Provenance_Check)
root.order.add_edge(Collection_Survey, Legal_Review)
root.order.add_edge(Provenance_Check, Ownership_Audit)
root.order.add_edge(Provenance_Check, Ethical_Screening)
root.order.add_edge(Provenance_Check, Condition_Report)
root.order.add_edge(Legal_Review, Ownership_Audit)
root.order.add_edge(Legal_Review, Ethical_Screening)
root.order.add_edge(Legal_Review, Condition_Report)
root.order.add_edge(Ownership_Audit, Scientific_Test)
root.order.add_edge(Ownership_Audit, Material_Analysis)
root.order.add_edge(Ethical_Screening, Scientific_Test)
root.order.add_edge(Ethical_Screening, Material_Analysis)
root.order.add_edge(Condition_Report, Scientific_Test)
root.order.add_edge(Condition_Report, Material_Analysis)
root.order.add_edge(Scientific_Test, Expert_Consultation)
root.order.add_edge(Material_Analysis, Expert_Consultation)
root.order.add_edge(Expert_Consultation, Transport_Planning)
root.order.add_edge(Transport_Planning, Secure_Packing)
root.order.add_edge(Secure_Packing, Customs_Clearance)
root.order.add_edge(Customs_Clearance, Insurance_Setup)
root.order.add_edge(Insurance_Setup, Exhibit_Preparation)
root.order.add_edge(Exhibit_Preparation, Final_Approval)

# Print the POWL model
print(root)