import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
Provenance_Check = Transition(label='Provenance Check')
Specimen_Sampling = Transition(label='Specimen Sampling')
Spectroscopy_Test = Transition(label='Spectroscopy Test')
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Material_Analysis = Transition(label='Material Analysis')
Forensic_Review = Transition(label='Forensic Review')
Expert_Consult = Transition(label='Expert Consult')
Legal_Verify = Transition(label='Legal Verify')
Ownership_Audit = Transition(label='Ownership Audit')
Risk_Assess = Transition(label='Risk Assess')
Insurance_Quote = Transition(label='Insurance Quote')
Condition_Report = Transition(label='Condition Report')
Documentation = Transition(label='Documentation')
Committee_Review = Transition(label='Committee Review')
Final_Approval = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Provenance_Check,
    Specimen_Sampling,
    Spectroscopy_Test,
    Radiocarbon_Date,
    Material_Analysis,
    Forensic_Review,
    Expert_Consult,
    Legal_Verify,
    Ownership_Audit,
    Risk_Assess,
    Insurance_Quote,
    Condition_Report,
    Documentation,
    Committee_Review,
    Final_Approval
])

# Define the dependencies
root.order.add_edge(Provenance_Check, Specimen_Sampling)
root.order.add_edge(Specimen_Sampling, Spectroscopy_Test)
root.order.add_edge(Spectroscopy_Test, Radiocarbon_Date)
root.order.add_edge(Radiocarbon_Date, Material_Analysis)
root.order.add_edge(Material_Analysis, Forensic_Review)
root.order.add_edge(Forensic_Review, Expert_Consult)
root.order.add_edge(Expert_Consult, Legal_Verify)
root.order.add_edge(Legal_Verify, Ownership_Audit)
root.order.add_edge(Ownership_Audit, Risk_Assess)
root.order.add_edge(Risk_Assess, Insurance_Quote)
root.order.add_edge(Insurance_Quote, Condition_Report)
root.order.add_edge(Condition_Report, Documentation)
root.order.add_edge(Documentation, Committee_Review)
root.order.add_edge(Committee_Review, Final_Approval)