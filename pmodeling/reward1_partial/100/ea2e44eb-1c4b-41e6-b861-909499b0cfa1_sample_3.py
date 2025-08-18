from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
expert_consult = Transition(label='Expert Consult')
material_scan = Transition(label='Material Scan')
three_d_imaging = Transition(label='3D Imaging')
stylistic_match = Transition(label='Stylistic Match')
database_query = Transition(label='Database Query')
panel_review = Transition(label='Panel Review')
certify_report = Transition(label='Certify Report')
condition_assess = Transition(label='Condition Assess')
storage_plan = Transition(label='Storage Plan')
catalog_entry = Transition(label='Catalog Entry')
display_prep = Transition(label='Display Prep')
loan_arrange = Transition(label='Loan Arrange')
monitor_setup = Transition(label='Monitor Setup')

# Define silent transitions for parallel activities
skip_provenance = SilentTransition()
skip_archive = SilentTransition()
skip_expert = SilentTransition()
skip_material = SilentTransition()
skip_3d = SilentTransition()
skip_stylistic = SilentTransition()
skip_database = SilentTransition()
skip_panel = SilentTransition()

# Define exclusive choices for provenance and archive searches
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip_provenance])
archive_choice = OperatorPOWL(operator=Operator.XOR, children=[archive_search, skip_archive])

# Define exclusive choices for material scans and 3D imaging
material_choice = OperatorPOWL(operator=Operator.XOR, children=[material_scan, skip_material])
three_d_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_imaging, skip_3d])

# Define exclusive choices for stylistic matches and database queries
stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_match, skip_stylistic])
database_choice = OperatorPOWL(operator=Operator.XOR, children=[database_query, skip_database])

# Define the loop for the panel review
panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[panel_review])

# Define the exclusive choice for panel reviews and expert consultations
panel_choice = OperatorPOWL(operator=Operator.XOR, children=[panel_loop, expert_consult])

# Define the exclusive choice for expert consultations and material scans
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, material_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_choice, material_3d_choice])

# Define the exclusive choice for material scans and 3D imaging
material_3d_choice = OperatorPOWL(operator=Operator.XOR, children=[material_choice, three_d_choice])

# Define the exclusive choice for 3D imaging and stylistic matches
three_d_stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[three_d_choice, stylistic_choice])

# Define the exclusive choice for stylistic matches and database queries
stylistic_database_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_choice, database_choice])

# Define the exclusive choice for database queries and expert consultations
database_expert_choice = OperatorPOWL(operator=Operator.XOR, children=[database_choice, expert_choice])

# Define the exclusive choice for expert consultations and material scans
expert_material_choice = OperatorPOWL(operator=Operator