from __future__ import annotations

from datetime import date, datetime
from typing import Annotated, Any, Literal
from uuid import UUID
from pydantic import Field

from pyhuntress.models.base.huntress_model import HuntressModel


#class AccountingBatch(HuntressModel):
#    info: Annotated[dict[str, str] | None, Field(alias="_info")] = None
#    batch_identifier: Annotated[str | None, Field(alias="batchIdentifier")] = None
#    closed_flag: Annotated[bool | None, Field(alias="closedFlag")] = None
#    export_expenses_flag: Annotated[bool | None, Field(alias="exportExpensesFlag")] = None
#    export_invoices_flag: Annotated[bool | None, Field(alias="exportInvoicesFlag")] = None
#    export_products_flag: Annotated[bool | None, Field(alias="exportProductsFlag")] = None
#    id: int | None = None
