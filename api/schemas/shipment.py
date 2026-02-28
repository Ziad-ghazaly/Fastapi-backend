from dataclasses import field
from datetime import datetime
from pydantic import BaseModel, Field 
from enum import Enum

class ShipmentStatus(str, Enum):  # enum is used to restrict the possible values for the status field
    placed = "placed"
    in_transit = "in_transit"
    delivered = "delivered"  
    pending = "pending"
    
    
    
class baseShipment(BaseModel):
    weight : float = Field(lt=25.0, ge=0.1)  
    content : str 
    destination : int
    

class ShipmentRead(baseShipment):
   shipment_id : int 
   destination : int 
   estimated_delivery : datetime

class shipmentCreate(baseShipment):
     pass

class shipmentUpdate(BaseModel):
    status : ShipmentStatus | None = field(default=None)
    estimated_delivery : datetime| None = field(default=None)
    destination : int | None = field(default=None)
    