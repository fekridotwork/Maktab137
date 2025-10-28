class Ticket():
    
    def __init__(self,
                 id : int,
                 user_id : int,
                 travel_id : int,
                 seat_number : int,
                 status : str,
                 created_at : str 
                ):
        self.id = id
        self.user_id = user_id
        self.travel_id = travel_id
        self.seat_number = seat_number
        self.status = status
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "travel_id": self.travel_id,
            "seat_number": self.seat_number,
            "status": self.status,
            "created_at": self.created_at
        }