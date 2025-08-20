import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
identify_need = Transition(label='Identify need for new hire')
create_job_desc = Transition(label='Create job description')
post_job_desc = Transition(label='Post job description')
collect_resumes = Transition(label='Collect resumes')
screen_resumes = Transition(label='Screen resumes')
initial_phone_interviews = Transition(label='Conduct initial phone interviews')
invite_candidates = Transition(label='Invite candidates for interviews')
virtual_interview = Transition(label='Conduct a virtual interview')
in_person_interview = Transition(label='Conduct an in-person interview')
choose_candidate = Transition(label='Choose candidate')
extend_offer = Transition(label='Extend offer')
negotiate_salary = Transition(label='Negotiate salary')
begin_onboarding = Transition(label='Begin onboarding process')
complete_paperwork = Transition(label='Complete paperwork')
complete_orientation = Transition(label='Complete orientation')
complete_training = Transition(label='Complete training')
integration = Transition(label='Fully integrated into the team')

# Define silent transitions
skip = SilentTransition()

# Define loops
interview_loop = OperatorPOWL(operator=Operator.LOOP, children=[invite_candidates, virtual_interview, in_person_interview])
salary_loop = OperatorPOWL(operator=Operator.LOOP, children=[extend_offer, negotiate_salary])

# Define choices
interview_choice = OperatorPOWL(operator=Operator.XOR, children=[virtual_interview, in_person_interview])
salary_choice = OperatorPOWL(operator=Operator.XOR, children=[negotiate_salary, skip])

# Define partial orders
interview_po = StrictPartialOrder(nodes=[invite_candidates, interview_choice])
salary_po = StrictPartialOrder(nodes=[extend_offer, salary_choice])

# Add dependencies to partial orders
interview_po.order.add_edge(invite_candidates, interview_choice)
salary_po.order.add_edge(extend_offer, salary_choice)

# Define main POWL model
root = StrictPartialOrder(nodes=[identify_need, create_job_desc, post_job_desc, collect_resumes, screen_resumes, initial_phone_interviews, interview_loop, choose_candidate, salary_loop, begin_onboarding, complete_paperwork, complete_orientation, complete_training, integration])

# Add dependencies to main POWL model
root.order.add_edge(identify_need, create_job_desc)
root.order.add_edge(create_job_desc, post_job_desc)
root.order.add_edge(post_job_desc, collect_resumes)
root.order.add_edge(collect_resumes, screen_resumes)
root.order.add_edge(screen_resumes, initial_phone_interviews)
root.order.add_edge(initial_phone_interviews, interview_loop)
root.order.add_edge(interview_loop, choose_candidate)
root.order.add_edge(choose_candidate, salary_loop)
root.order.add_edge(salary_loop, begin_onboarding)
root.order.add_edge(begin_onboarding, complete_paperwork)
root.order.add_edge(complete_paperwork, complete_orientation)
root.order.add_edge(complete_orientation, complete_training)
root.order.add_edge(complete_training, integration)