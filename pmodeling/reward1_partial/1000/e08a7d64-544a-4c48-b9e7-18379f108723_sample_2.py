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

# Define silent transitions for skipping certain steps
skip_material_testing = SilentTransition()
skip_insurance_quote = SilentTransition()
skip_catalog_entry = SilentTransition()
skip_digital_scan = SilentTransition()
skip_condition_report = SilentTransition()
skip_transport_plan = SilentTransition()
skip_customs_clear = SilentTransition()

# Define workflow steps
provenance_check_step = OperatorPOWL(operator=Operator.SILENT, children=[provenance_check])
material_testing_step = OperatorPOWL(operator=Operator.SILENT, children=[material_testing])
expert_review_step = OperatorPOWL(operator=Operator.SILENT, children=[expert_review])
legal_verify_step = OperatorPOWL(operator=Operator.SILENT, children=[legal_verify])
risk_assess_step = OperatorPOWL(operator=Operator.SILENT, children=[risk_assess])
insurance_quote_step = OperatorPOWL(operator=Operator.SILENT, children=[insurance_quote])
catalog_entry_step = OperatorPOWL(operator=Operator.SILENT, children=[catalog_entry])
digital_scan_step = OperatorPOWL(operator=Operator.SILENT, children=[digital_scan])
condition_report_step = OperatorPOWL(operator=Operator.SILENT, children=[condition_report])
transport_plan_step = OperatorPOWL(operator=Operator.SILENT, children=[transport_plan])
customs_clear_step = OperatorPOWL(operator=Operator.SILENT, children=[customs_clear])
certification_step = OperatorPOWL(operator=Operator.SILENT, children=[certification])
exhibit_setup_step = OperatorPOWL(operator=Operator.SILENT, children=[exhibit_setup])
owner_notify_step = OperatorPOWL(operator=Operator.SILENT, children=[owner_notify])
final_audit_step = OperatorPOWL(operator=Operator.SILENT, children=[final_audit])

# Define exclusive choice for material testing and insurance quote
material_or_insurance = OperatorPOWL(operator=Operator.XOR, children=[skip_material_testing, skip_insurance_quote])
material_or_insurance.add_edge(skip_material_testing, material_testing)
material_or_insurance.add_edge(skip_insurance_quote, insurance_quote)

# Define exclusive choice for catalog entry and digital scan
catalog_or_digital = OperatorPOWL(operator=Operator.XOR, children=[skip_catalog_entry, skip_digital_scan])
catalog_or_digital.add_edge(skip_catalog_entry, catalog_entry)
catalog_or_digital.add_edge(skip_digital_scan, digital_scan)

# Define exclusive choice for condition report and transport plan
condition_or_transport = OperatorPOWL(operator=Operator.XOR, children=[skip_condition_report, skip_transport_plan])
condition_or_transport.add_edge(skip_condition_report, condition_report)
condition_or_transport.add_edge(skip_transport_plan, transport_plan)

# Define exclusive choice for customs clear and exhibit setup
customs_or_exhibit = OperatorPOWL(operator=Operator.XOR, children=[skip_customs_clear, skip_exhibit_setup])
customs_or_exhibit.add_edge(skip_customs_clear, customs_clear)
customs_or_exhibit.add_edge(skip_exhibit_setup, exhibit_setup)

# Define loop for certification issuance
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification, owner_notify, final_audit])

# Define the root POWL model
root = StrictPartialOrder(nodes=[provenance_check_step, material_testing_step, expert_review_step, legal_verify_step, risk_assess_step, material_or_insurance, catalog_or_digital, condition_or_transport, customs_or_exhibit, certification_loop])
root.order.add_edge(provenance_check_step, material_testing_step)
root.order.add_edge(material_testing_step, expert_review_step)
root.order.add_edge(expert_review_step, legal_verify_step)
root.order.add_edge(legal_verify_step, risk_assess_step)
root.order.add_edge(risk_assess_step, material_or_insurance)
root.order.add_edge(material_or_insurance, catalog_or_digital)
root.order.add_edge(catalog_or_digital, condition_or_transport)
root.order.add_edge(condition_or_transport, customs_or_exhibit)
root.order.add_edge(customs_or_exhibit, certification_loop)

# Print the root POWL model
print(root)