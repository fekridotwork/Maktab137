class Payment():
    
    def __init__(self,
                 id : int,
                 user_id : int,
                 travel_id : int,
                 amount : float,
                 paid_at : str,
                 status : str
                 ):
        self,id = id
        self.user_id = user_id
        self.travel_id = travel_id
        self.amount = amount
        self.paid_at = paid_at
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "ticket_id": self.ticket_id,
            "amount": self.amount,
            "status": self.status,
            "paid_at": self.paid_at
        }