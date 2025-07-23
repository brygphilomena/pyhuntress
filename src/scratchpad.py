import os
from pyhuntress import HuntressSIEMAPIClient
from dotenv import load_dotenv

load_dotenv()

siem_url = os.getenv('siem_url')
publickey = os.getenv('publickey')
privatekey = os.getenv('privatekey')

# init client
siem_api_client = HuntressSIEMAPIClient(
    siem_url,
    publickey,
    privatekey,
)

#account = siem_api_client.account.get()
#print(account)

#actor = siem_api_client.actor.get()
#print(actor)

#agents = siem_api_client.agents.get()
#print(agents)

#billingreports = siem_api_client.billing_reports.get()
#print(billingreports)

#incidentreports = siem_api_client.incident_reports.get()
#print(incidentreports)

#organizations = siem_api_client.organizations.get()
#print(organizations)

#reports = siem_api_client.reports.get()
#print(reports)

#signals = siem_api_client.signals.get()
#print(signals)

paginated_billingreports = siem_api_client.billing_reports.paginated(1, 10)
print(paginated_billingreports.data)

paginated_incidentreports = siem_api_client.incident_reports.paginated(1, 10)
print(paginated_incidentreports.data)

paginated_organizations = siem_api_client.organizations.paginated(1, 10)
print(paginated_organizations.data)

paginated_reports = siem_api_client.reports.paginated(1, 10)
print(paginated_reports.data)

paginated_signals = siem_api_client.signals.paginated(1, 10)
print(paginated_signals.data)
