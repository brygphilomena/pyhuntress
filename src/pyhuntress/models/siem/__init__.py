from __future__ import annotations

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import Field

from pyhuntress.models.base.huntress_model import HuntressModel

class SIEMPagination(HuntressModel):
    current_page: int | None = Field(default=None, alias="CurrentPage")
    current_page_count: int | None = Field(default=None, alias="CurrentPageCount")
    limit: int | None = Field(default=None, alias="Limit")
    total_count: int | None = Field(default=None, alias="TotalCount")
    next_page: int | None = Field(default=None, alias="NextPage")
    next_page_url: str | None = Field(default=None, alias="NextPageURL")
    next_page_token: str | None = Field(default=None, alias="NextPageToken")
    
class SIEMAgents(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    version: str | None = Field(default=None, alias="Version")
    arch: str | None = Field(default=None, alias="Arch")
    win_build_number: str | None = Field(default=None, alias="WinBuildNumber")
    domain_name: str | None = Field(default=None, alias="DomainName")
    created_at: datetime | None = Field(default=None, alias="CreateAt")
    hostname: str | None = Field(default=None, alias="Hostname")
    ipv4_address: str | None = Field(default=None, alias="IPv4Address")
    external_ip: str | None = Field(default=None, alias="ExternalIP")
    mac_addresses: list | None = Field(default=None, alias="MacAddresses")
    updated_at: datetime | None = Field(default=None, alias="IPv4Address")
    last_survey_at: datetime | None = Field(default=None, alias="LastSurveyAt")
    last_callback_at: datetime | None = Field(default=None, alias="LastCallbackAt")
    account_id: int | None = Field(default=None, alias="AccountID")
    organization_id: int | None = Field(default=None, alias="OrganizationID")
    platform: Literal[
        "windows",
        "darwin",
        "linux",
    ] | None = Field(default=None, alias="Platform")
    os: str | None = Field(default=None, alias="OS")
    service_pack_major: int | None = Field(default=None, alias="ServicePackMajor")
    service_pack_minor: int | None = Field(default=None, alias="ServicePackMinor")
    tags: list | None = Field(default=None, alias="Tags")
    os_major: int | None = Field(default=None, alias="OSMajor")
    os_minor: int | None = Field(default=None, alias="OSMinor")
    os_patch: int | None = Field(default=None, alias="OSPatch")
    version_number: int | None = Field(default=None, alias="VersionNumber")
    edr_version: str | None = Field(default=None, alias="EDRVersion")
    os_build_version: str | None = Field(default=None, alias="OSBuildVersion")
    serial_number: str | None = Field(default=None, alias="SerialNumber")
    defender_status: str | None = Field(default=None, alias="DefenderStatus")
    defender_substatus: str | None = Field(default=None, alias="DefenderSubstatus")
    defender_policy_status: str | None = Field(default=None, alias="DefenderPolicyStatus")
    firewall_status: str | None = Field(default=None, alias="FirewallStatus")

class SIEMAgentsResponse(HuntressModel):
    agents: dict[str, Any] | None = Field(default=None, alias="Agents")
    pagination: dict[str, Any] | None = Field(default=None, alias="Pagination")
    
class SIEMAccount(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    subdomain: str | None = Field(default=None, alias="Subdomain")
    status: str | None = Field(default=None, alias="Status")

class SIEMActorResponse(HuntressModel):
    account: dict[str, Any] | None = Field(default=None, alias="Account")
    user: str | None = Field(default=None, alias="User")

class SIEMBillingReports(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    plan: str | None = Field(default=None, alias="Plan")
    quantity: int | None = Field(default=None, alias="Quantity")
    amount: int | None = Field(default=None, alias="Amount")
    currency_type: str | None = Field(default=None, alias="CurrencyType")
    receipt: str | None = Field(default=None, alias="Receipt")
    status: Literal[
        "open",
        "paid",
        "failed",
        "partial_refund",
        "full_refund",
        "draft",
        "voided",
    ] | None = Field(default=None, alias="Status")
    created_at: datetime | None = Field(default=None, alias="CreatedAt")
    updated_at: datetime | None = Field(default=None, alias="UpdatedAt")

class SIEMBillingReportsResponse(HuntressModel):
    billing_reports: dict[str, Any] | None = Field(default=None, alias="BillingReports")

class SIEMIncidentReportsResponse(HuntressModel):
    incident_reports: dict[str, Any] | None = Field(default=None, alias="IncidentReports")
    pagination: dict[str, Any] | None = Field(default=None, alias="Pagination")
    
class SIEMIncidentReports(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    status: Literal[
        "sent",
        "closed",
        "dismissed",
        "auto_remediating",
        "deleting",
    ] | None = Field(default=None, alias="Status")
    summary: str | None = Field(default=None, alias="Summary")
    body: str | None = Field(default=None, alias="Body")
    updated_at: datetime | None = Field(default=None, alias="UpdatedAt")
    agent_id: int | None = Field(default=None, alias="AgentId")
    platform: Literal[
        "windows",
        "darwin",
        "microsoft_365",
        "google",
        "linux",
        "other",
    ] | None = Field(default=None, alias="Platform")
    status_updated_at: datetime | None = Field(default=None, alias="StatusUpdatedAt")
    organization_id: int | None = Field(default=None, alias="OrganizationId")
    sent_at: datetime | None = Field(default=None, alias="SentAt")
    account_id: int | None = Field(default=None, alias="AccountId")
    subject: str | None = Field(default=None, alias="Subject")
    remediations: list[dict[str, Any]] | None = Field(default=None, alias="Remediations")
    severity: Literal[
        "low",
        "high",
        "critical",
    ] | None = Field(default=None, alias="Severity")
    closed_at: datetime | None = Field(default=None, alias="ClosedAt")
    indicator_types: list | None = Field(default=None, alias="IndicatorTypes")
    indicator_counts: dict[str, Any] | None = Field(default=None, alias="IndicatorCounts")
    

class SIEMRemediations(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    type: str | None = Field(default=None, alias="Type")
    status: str | None = Field(default=None, alias="Status")
    details: dict[str, Any] | None = Field(default=None, alias="Details")
    completable_by_task_response: bool | None = Field(default=None, alias="CompletedByTaskResponse")
    completable_manually: bool | None = Field(default=None, alias="CompletedManually")
    display_action: str | None = Field(default=None, alias="DisplayAction")
    approved_at: datetime | None = Field(default=None, alias="ApprovedAt")
    approved_by: dict[str, Any] | None = Field(default=None, alias="ApprovedBy")
    completed_at: datetime | None = Field(default=None, alias="CompletedAt")
    
class SIEMRemediationsDetails(HuntressModel):
    rule_id: int | None = Field(default=None, alias="RuleId")
    rule_name: str | None = Field(default=None, alias="RuleName")
    completed_at: datetime | None = Field(default=None, alias="CompletedAt")
    forward_from: str | None = Field(default=None, alias="ForwardFrom")
    remediation: str | None = Field(default=None, alias="remediation")
    
class SIEMRemediationsApprovedBy(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    email: str | None = Field(default=None, alias="Email")
    first_name: str | None = Field(default=None, alias="FirstName")
    last_name: str | None = Field(default=None, alias="LastName")
    
class SIEMIndicatorCounts(HuntressModel):
    footholds: int | None = Field(default=None, alias="Footholds")
    mde_detections: int | None = Field(default=None, alias="MDEDetections")
    monitored_files: int | None = Field(default=None, alias="MonitoredFiles")
    siem_detections: int | None = Field(default=None, alias="SIEMDetections")
    managed_identity: int | None = Field(default=None, alias="ManagedIdentity")
    process_detections: int | None = Field(default=None, alias="ProcessDetections")
    ransomware_canaries: int | None = Field(default=None, alias="RansomwareCanaries")
    antivirus_detections: int | None = Field(default=None, alias="AntivirusDetections")
    
class SIEMOrganizationsResponse(HuntressModel):
    organizations: dict[str, Any] | None = Field(default=None, alias="Organizations")
    pagination: dict[str, Any] | None = Field(default=None, alias="Pagination")
    
class SIEMOrganizations(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    created_at: datetime | None = Field(default=None, alias="CreatedAt")
    updated_at: datetime | None = Field(default=None, alias="UpdatedAt")
    account_id: int | None = Field(default=None, alias="AccountId")
    key: str | None = Field(default=None, alias="Key")
    notify_emails: list | None = Field(default=None, alias="NotifyEmails")
    microsoft_365_tenant_id: str | None = Field(default=None, alias="Microsoft365TenantId")
    incident_reports_count: int | None = Field(default=None, alias="IncidentsReportsCount")
    agents_count: int | None = Field(default=None, alias="AgentsCount")
    microsoft_365_users_count: int | None = Field(default=None, alias="Microsoft365UsersCount")
    sat_learner_count: int | None = Field(default=None, alias="SATLearnerCount")
    logs_sources_count: int | None = Field(default=None, alias="LogsSourcesCount")

class SIEMReportsResponse(HuntressModel):
    reports: dict[str, Any] | None = Field(default=None, alias="Organizations")
    pagination: dict[str, Any] | None = Field(default=None, alias="Pagination")

class SIEMReports(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    type: Literal[
        "monthly_summary",
        "quarterly_summary",
        "yearly_summary",
    ] | None = Field(default=None, alias="Type")
    period: str | None = Field(default=None, alias="Period")
    organization_id: int | None = Field(default=None, alias="OrganizationId")
    created_at: datetime | None = Field(default=None, alias="CreatedAt")
    updated_at: datetime | None = Field(default=None, alias="UpdatedAt")
    url: str | None = Field(default=None, alias="Type")
    events_analyzed: int | None = Field(default=None, alias="EventsAnalyzed")
    total_entities: int | None = Field(default=None, alias="TotalEntities")
    signals_detected: int | None = Field(default=None, alias="SignalsDetected")
    signals_investigated: int | None = Field(default=None, alias="SignalsInvestigated")
    itdr_entities: int | None = Field(default=None, alias="ITDREntities")
    itdr_events: int | None = Field(default=None, alias="ITDREvents")
    siem_total_logs: int | None = Field(default=None, alias="SIEMTotalLogs")
    siem_ingested_logs: int | None = Field(default=None, alias="SIEMIngestedLogs")
    autorun_events: int | None = Field(default=None, alias="AutorunEvents")
    autorun_signals_detected: int | None = Field(default=None, alias="AutorunSignalsDetected")
    investigations_completed: int | None = Field(default=None, alias="InvestigationsCompleted")
    autorun_signals_reviewed: int | None = Field(default=None, alias="AutorunSignalsReviewed")
    incidents_reported: int | None = Field(default=None, alias="IncidentsReported")
    itdr_incidents_reported: int | None = Field(default=None, alias="ITDRIncidentsReported")
    siem_incidents_reported: int | None = Field(default=None, alias="SIEMIncidentsReported")
    incidents_resolved: int | None = Field(default=None, alias="IncidentsResolved")
    incident_severity_counts: int | None = Field(default=None, alias="IncidentSeverityCounts")
    incident_product_counts: int | None = Field(default=None, alias="IncidentProductCounts")
    incident_indicator_counts: int | None = Field(default=None, alias="IncidentIndicatorCounts")
    top_incident_av_threats: list | None = Field(default=None, alias="TopIncidentAVThreats")
    top_incident_hosts: list | None = Field(default=None, alias="TopIncidentHosts")
    potential_threat_indicators: list | None = Field(default=None, alias="PotentialThreatIndicators")
    agents_count: int | None = Field(default=None, alias="AgentsCount")
    deployed_canaries_count: int | None = Field(default=None, alias="DeployedCanariesCount")
    protected_profiles_count: int | None = Field(default=None, alias="ProtectedProfilesCount")
    windows_agent_count: int | None = Field(default=None, alias="WindowsAgentCount")
    macos_agent_count: int | None = Field(default=None, alias="MacOSAgentCount")
    servers_agent_count: int | None = Field(default=None, alias="ServersAgentCount")
    analyst_note: str | None = Field(default=None, alias="AnalystNote")
    global_threats_note: str | None = Field(default=None, alias="GlobalThreatsNote")
    ransomware_note: str | None = Field(default=None, alias="RansomwareNote")
    incident_log: str | None = Field(default=None, alias="IncidentLog")
    total_mav_detection_count: int | None = Field(default=None, alias="TotalMAVDetectionCount")
    blocked_malware_count: int | None = Field(default=None, alias="BlockedMalwareCount")
    investigated_mav_detection_count: int | None = Field(default=None, alias="InvestigatedMAVDetectionCount")
    mav_incident_report_count: int | None = Field(default=None, alias="MAVIncidentReportCount")
    autoruns_reviewed: int | None = Field(default=None, alias="AutorunsReviewed")
    host_processes_analyzed: int | None = Field(default=None, alias="HostProcessesAnalyzed")
    process_detections: int | None = Field(default=None, alias="ProcessDetections")
    process_detections_reviewed: int | None = Field(default=None, alias="ProcessDetectionsReviewed")
    process_detections_reported: int | None = Field(default=None, alias="ProcessDetectionsReported")
    itdr_signals: int | None = Field(default=None, alias="ITDRSignals")
    siem_signals: int | None = Field(default=None, alias="SIEMSignals")
    itdr_investigations_completed: int | None = Field(default=None, alias="ITDRInvestigationsCompleted")
    macos_agents: str | None = Field(default=None, alias="MacOSAgents")
    windows_agents: str | None = Field(default=None, alias="WindowsAgents")
    only_macos_agents: str | None = Field(default=None, alias="OnlyMacOSAgents")
    antivirus_exclusions_count: int | None = Field(default=None, alias="AntivirusExclusionsCount")
    new_exclusions_count: int | None = Field(default=None, alias="NewExclusionsCount")
    allowed_exclusions_count: int | None = Field(default=None, alias="AllowedExclusionsCount")
    risky_exclusions_removed_count: int | None = Field(default=None, alias="RiskyExclusionsRemovedCount")

class SIEMSignalsResponse(HuntressModel):
    signals: dict[str, Any] | None = Field(default=None, alias="Organizations")
    pagination: dict[str, Any] | None = Field(default=None, alias="Pagination")

class SIEMSignals(HuntressModel):
    created_at: datetime | None = Field(default=None, alias="CreatedAt")
    id: int | None = Field(default=None, alias="Id")
    status: str | None = Field(default=None, alias="Status")
    updated_at: datetime | None = Field(default=None, alias="UpdatedAt")
    details: dict[str, Any] | None = Field(default=None, alias="Details")
    entity: dict[str, Any] | None = Field(default=None, alias="Entity")
    investigated_at: datetime | None = Field(default=None, alias="InvestigatedAt")
    investigation_context: str | None = Field(default=None, alias="InvestigationContext")
    name: str | None = Field(default=None, alias="Name")
    organization: dict[str, Any] | None = Field(default=None, alias="Organization")
    type: str | None = Field(default=None, alias="Type")
    
class SIEMSignalsDetails(HuntressModel):
    identity: str | None = Field(default=None, alias="Identity")
    application: str | None = Field(default=None, alias="Application")
    detected_at: datetime | None = Field(default=None, alias="DetectedAt")
    
class SIEMSignalsEntity(HuntressModel):
    id: int | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    type: Literal[
        "user_entity",
        "source",
        "mailbox",
        "service_principal",
        "agent",
        "identity",
    ] | None = Field(default=None, alias="Type")
