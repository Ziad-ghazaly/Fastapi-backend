

from datetime import datetime, timedelta

from app.api.schemas.shipment import ShipmentRead, shipmentCreate, shipmentUpdate
from app.database.models import baseShipment, shipmentStatus
from app.database.session import SessionDep
from fastapi import APIRouter, HTTPException, status # type: ignore



router = APIRouter()

@router.get("/shipment/", response_model=baseShipment)
async def get_shipment(shipment_id: int, session: SessionDep): # using the schema to validate the response
    shipment = await session.get(baseShipment, shipment_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="error wrong shipment id is not found",
        )
    return shipment

@router.post("/shipment/")
async def add_shipment(shipment: shipmentCreate, session: SessionDep) -> dict[str, int]:
    new_shipment = baseShipment(
     **shipment.model_dump(),
    status=shipmentStatus.pending,
    estimated_delivery=datetime.now() + timedelta(days=3)
    )
    session.add(new_shipment)
    await session.commit()
    await session.refresh(new_shipment)
    return {"id": new_shipment.shipment_id}

@router.patch("/shipment/", response_model=ShipmentRead)
async def update_shipment(shipment_id: int, shipment_update: shipmentUpdate, session: SessionDep):
    update = shipment_update.model_dump(exclude_unset=True)
    shipment = session.get(baseShipment, shipment_id)
    if not shipment:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"
        )
    shipment.sqlmodel_update(update)
    session.add(shipment)
    await session.commit()
    await session.refresh(shipment)
    return shipment
        

@router.delete("/shipment/") 
async def delete_shipment(shipment_id: int, session: SessionDep) -> dict[str, str]:
    await session.delete(session.get(baseShipment, shipment_id))
    await session.commit()
    return {"message": "shipment deleted successfully"}
