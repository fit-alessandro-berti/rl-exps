from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
begin_onboarding = Transition(label='Begin onboarding process')
choose_candidate = Transition(label='Choose candidate')
collect_resumes = Transition(label='Collect resumes')
complete_orientation = Transition(label='Complete orientation')
complete_paperwork = Transition(label='Complete paperwork')
complete_training = Transition(label='Complete training')
conduct_virtual_interview = Transition(label='Conduct a virtual interview')
conduct_in_person_interview = Transition(label='Conduct an in-person interview')
conduct_initial_phone_interviews = Transition(label='Conduct initial phone interviews')
create_job_description = Transition(label='Create job description')
extend_offer = Transition(label='Extend offer')
identify_need_for_new_hire = Transition(label='Identify need for new hire')
invite_candidates_for_interviews = Transition(label='Invite candidates for interviews')
negotiate_salary = Transition(label='Negotiate salary')
post_job_description = Transition(label='Post job description')
screen_resumes = Transition(label='Screen resumes')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for phone interviews
xor_phone = OperatorPOWL(operator=Operator.XOR, children=[conduct_initial_phone_interviews, skip])

# Define exclusive choice for interviews
xor_interviews = OperatorPOWL(operator=Operator.XOR, children=[conduct_virtual_interview, conduct_in_person_interview])

# Define loop for interviewing candidates
loop_interviews = OperatorPOWL(operator=Operator.LOOP, children=[xor_interviews, skip])

# Define exclusive choice for onboarding steps
xor_onboarding = OperatorPOWL(operator=Operator.XOR, children=[complete_paperwork, complete_orientation, complete_training])

# Define loop for onboarding steps
loop_onboarding = OperatorPOWL(operator=Operator.LOOP, children=[xor_onboarding, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define exclusive choice for selecting candidate
xor_select_candidate = OperatorPOWL(operator=Operator.XOR, children=[choose_candidate, skip])

# Define exclusive choice for hiring candidate
xor_hire_candidate = OperatorPOWL(operator=Operator.XOR, children=[extend_offer, skip])

# Define exclusive choice for job search
xor_job_search = OperatorPOWL(operator=Operator.XOR, children=[identify_need_for_new_hire, skip])

# Define exclusive choice for posting job description
xor_post_job_description = OperatorPOWL(operator=Operator.XOR, children=[post_job_description, skip])

# Define exclusive choice for screen resumes
xor_screen_resumes = OperatorPOWL(operator=Operator.XOR, children=[screen_resumes, skip])

# Define