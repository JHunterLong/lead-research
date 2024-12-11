from services.search import search_company
from services.gpt import generate_message
from services.email import send_email

# Lead details
name = "Jane Doe"
company = "Tech Solutions"
role = "CTO"

# Research and message generation
search_results = search_company(company)
insights = " ".join([result['snippet'] for result in search_results[:2]])
prompt = f"Write a personalized email to {name}, a {role} at {company}. Mention their recent work: {insights}."
email_body = generate_message(prompt)

# Send the email
send_email("jane.doe@techsolutions.com", "Collaboration Opportunity", email_body)
