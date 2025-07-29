from __future__ import annotations

from datetime import date, datetime
from typing import Annotated, Any, Literal
from uuid import UUID
from pydantic import Field

from pyhuntress.models.base.huntress_model import HuntressModel
    
class SATData(HuntressModel):
    type: Literal[
        "accounts",
        "users",
        "assignments",
        "learners",
        "learner-activities",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")
    
class SATAccounts(HuntressModel):
    type: Literal[
        "accounts",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")
    
class SATUsers(HuntressModel):
    type: Literal[
        "users",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")
    
class SATAssignments(HuntressModel):
    type: Literal[
        "assignments",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")
    
class SATLearners(HuntressModel):
    type: Literal[
        "learners",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")
    
class SATLearnerActivities(HuntressModel):
    type: Literal[
        "learner-activities",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")
    
class SATAccountsAttributes(HuntressModel):
    name: str | None = Field(default=None, alias="Name")
    status: str | None = Field(default=None, alias="Status")
    type: str | None = Field(default=None, alias="Type")
    plan: str | None = Field(default=None, alias="Plan")
    licenses: int | None = Field(default=None, alias="Licenses")
    createdAt: datetime | None = Field(default=None, alias="CreatedAt")
    updatedAt: datetime | None = Field(default=None, alias="UpdatedAt")

class SATAssignmentsCompletionCertificates(HuntressModel):
    type: Any | None = Field(default=None, alias="Type")
    attributes: dict[str, str] | None = Field(default=None, alias="Attributes")

class SATEpisodes(HuntressModel):
    type: Literal[
        "episodes",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")

class SATDepartments(HuntressModel):
    type: Literal[
        "departments",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")

class SATGroups(HuntressModel):
    type: Literal[
        "groups",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")

class SATPhishingCampaigns(HuntressModel):
    type: Literal[
        "phishing-campaigns",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")

class SATPhishingScenarios(HuntressModel):
    type: Literal[
        "phishing-scenarios",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")

class SATPhishingCampaignAttempts(HuntressModel):
    type: Literal[
        "phishing-attempts",
        ] | None = Field(default=None, alias="Type")
    id: str | None = Field(default=None, alias="Id")
    attributes: dict[str, Any] | None = Field(default=None, alias="Attributes")
    relationships: dict[str, dict[str, dict[str, str]]] | None = Field(default=None, alias="Relationships")
    links: dict[str, str] | None = Field(default=None, alias="Links")
    meta: dict[str, dict[str, int]] | None = Field(default=None, alias="Meta")

class SATPhishingAttemptsReport(HuntressModel):
    data: Any
    #This class needs to be researched more