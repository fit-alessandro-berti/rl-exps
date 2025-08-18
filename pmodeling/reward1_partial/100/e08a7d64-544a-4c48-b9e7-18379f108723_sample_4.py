import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
expert_review = Transition(label='Expert Review')
legal_verify = Transition(label='Legal Verify')
risk_assess = Transition(label='Risk Assess')
insurance_quote = Transition(label='Insurance Quote')
catalog_entry = Transition(label='Catalog Entry')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
transport_plan = Transition(label='Transport Plan')
customs_clear = Transition(label='Customs Clear')
certification = Transition(label='Certification')
exhibit_setup = Transition(label='Exhibit Setup')
owner_notify = Transition(label='Owner Notify')
final_audit = Transition(label='Final Audit')

# Define silent transitions for skipping activities
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()

# Define exclusive choice for risk assessment and insurance quote
risk_insurance_choice = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define exclusive choice for material testing and expert review
material_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[material_testing, expert_review])

# Define exclusive choice for legal verify and catalog entry
legal_catalog_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, catalog_entry])

# Define exclusive choice for digital scan and condition report
digital_condition_choice = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, condition_report])

# Define exclusive choice for transport plan and customs clear
transport_customs_choice = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, customs_clear])

# Define exclusive choice for certification and exhibit setup
certification_exhibit_choice = OperatorPOWL(operator=Operator.XOR, children=[certification, exhibit_setup])

# Define exclusive choice for owner notify and final audit
owner_notify_final_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[owner_notify, final_audit])

# Define the root POWL model with sequential execution of activities
root = StrictPartialOrder(
    nodes=[provenance_check, material_expert_choice, legal_catalog_choice, risk_insurance_choice,
           digital_condition_choice, transport_customs_choice, certification_exhibit_choice,
           owner_notify_final_audit_choice]
)

# Add edges to the root model
root.order.add_edge(provenance_check, material_expert_choice)
root.order.add_edge(material_expert_choice, legal_catalog_choice)
root.order.add_edge(legal_catalog_choice, risk_insurance_choice)
root.order.add_edge(risk_insurance_choice, digital_condition_choice)
root.order.add_edge(digital_condition_choice, transport_customs_choice)
root.order.add_edge(transport_customs_choice, certification_exhibit_choice)
root.order.add_edge(certification_exhibit_choice, owner_notify_final_audit_choice)

# Print the root POWL model
print(root)