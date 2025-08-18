import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the process tree structure
# Initial provenance check
provenance_check = OperatorPOWL(operator=Operator.XOR, children=[skip, Provenance_Check])

# Specimen sampling and testing
specimen_sampling = OperatorPOWL(operator=Operator.XOR, children=[skip, Specimen_Sampling])
spectroscopy_test = OperatorPOWL(operator=Operator.XOR, children=[skip, Spectroscopy_Test])
radiocarbon_date = OperatorPOWL(operator=Operator.XOR, children=[skip, Radiocarbon_Date])
material_analysis = OperatorPOWL(operator=Operator.XOR, children=[skip, Material_Analysis])

# Forensic review and expert consultations
forensic_review = OperatorPOWL(operator=Operator.XOR, children=[skip, Forensic_Review])
expert_consult = OperatorPOWL(operator=Operator.XOR, children=[skip, Expert_Consult])

# Legal verification and ownership audit
legal_verify = OperatorPOWL(operator=Operator.XOR, children=[skip, Legal_Verify])
ownership_audit = OperatorPOWL(operator=Operator.XOR, children=[skip, Ownership_Audit])

# Risk assessment and insurance quote
risk_assess = OperatorPOWL(operator=Operator.XOR, children=[skip, Risk_Assess])
insurance_quote = OperatorPOWL(operator=Operator.XOR, children=[skip, Insurance_Quote])

# Condition report and documentation
condition_report = OperatorPOWL(operator=Operator.XOR, children=[skip, Condition_Report])
documentation = OperatorPOWL(operator=Operator.XOR, children=[skip, Documentation])

# Committee review and final approval
committee_review = OperatorPOWL(operator=Operator.XOR, children=[skip, Committee_Review])
final_approval = OperatorPOWL(operator=Operator.XOR, children=[skip, Final_Approval])

# Connect the nodes in the process tree
root = StrictPartialOrder(nodes=[
    provenance_check,
    specimen_sampling,
    spectroscopy_test,
    radiocarbon_date,
    material_analysis,
    forensic_review,
    expert_consult,
    legal_verify,
    ownership_audit,
    risk_assess,
    insurance_quote,
    condition_report,
    documentation,
    committee_review,
    final_approval
])

root.order.add_edge(provenance_check, specimen_sampling)
root.order.add_edge(specimen_sampling, spectroscopy_test)
root.order.add_edge(specimen_sampling, radiocarbon_date)
root.order.add_edge(specimen_sampling, material_analysis)
root.order.add_edge(spectroscopy_test, forensic_review)
root.order.add_edge(spectroscopy_test, expert_consult)
root.order.add_edge(radiocarbon_date, forensic_review)
root.order.add_edge(radiocarbon_date, expert_consult)
root.order.add_edge(material_analysis, forensic_review)
root.order.add_edge(material_analysis, expert_consult)
root.order.add_edge(forensic_review, legal_verify)
root.order.add_edge(forensic_review, ownership_audit)
root.order.add_edge(expert_consult, legal_verify)
root.order.add_edge(expert_consult, ownership_audit)
root.order.add_edge(legal_verify, risk_assess)
root.order.add_edge(legal_verify, insurance_quote)
root.order.add_edge(ownership_audit, risk_assess)
root.order.add_edge(ownership_audit, insurance_quote)
root.order.add_edge(risk_assess, condition_report)
root.order.add_edge(risk_assess, documentation)
root.order.add_edge(insurance_quote, condition_report)
root.order.add_edge(insurance_quote, documentation)
root.order.add_edge(condition_report, committee_review)
root.order.add_edge(condition_report, final_approval)
root.order.add_edge(documentation, committee_review)
root.order.add_edge(documentation, final_approval)
root.order.add_edge(committee_review, final_approval)

print(root)