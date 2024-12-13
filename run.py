from services.search import search_company
from services.gpt import generate_message
from services.email import send_email

def process_lead(name, company, role, email):
 # Step 1: Research company
    search_results = search_company(company)
    insights = " ".join([item['snippet'] for item in search_results[:2]])

    # Step 2: Generate personalized message
    prompt = f"Write a personalized email to {name}, a {role} at {company}. Mention their recent work: {insights}."
    message = generate_message(prompt)

    # Step 3: Log the message
    print(f"Generated message for {name}:\n{message}\n")

    # Step 4: Send email (optional)
    # send_email(email, f"Hello {name}, Let's Collaborate!", message)

# Add one piece of sample data
process_lead("Andrew Vardell", "Scout Motors", "Strategy",)

# Lead details
name = "Jane Doe"
company = "Tech Solutions"
role = "CTO"

# Research and message generation
search_results = search_company(company)
insights = " ".join([result['snippet'] for result in search_results[:2]])
prompt = f"Write a personalized email to {name}, a {role} at {company}. Mention their recent work: {insights}."
email_body = generate_message(prompt)
