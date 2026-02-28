from datetime import datetime
from sqlmodel import SQLModel, Field # type: ignore
from enum import Enum


class shipmentStatus(str, Enum):  
    placed = "placed"
    in_transit = "in_transit"
    delivered = "delivered"   
    pending = "pending" 
    
    
class baseShipment(SQLModel, table=True):
    __tablename__ = "shipments"
    
    shipment_id : int = Field(default=None, primary_key=True)
    weight : float = Field(lt=25.0, ge=0.1)  
    content : str 
    status : shipmentStatus
    destination : int
    estimated_delivery : datetime
    
    