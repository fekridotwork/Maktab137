class Travel:
    def __init__(self, 
                id : int,
                origin : str,
                destination : str,
                departure_time : str,
                duration : int,
                capacity : int,
                available_seats : int,
                price : float,
                status : str
                ):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration
        self.capacity = capacity
        self.available_seats = available_seats
        self.price = price
        self.status = status
        
    def to_dict(self):
        return {
            "id" : self.id,
            "origin" : self.origin,
            "destination" : self.destination,
            "departure_time" : self.departure_time,
            "duration" : self.duration,
            "capacity" : self.capacity,
            "available_seats" : self.available_seats,
            "price" : self.price,
            "status" : self.status
        }
