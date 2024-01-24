from datetime import date, timedelta

class Session:

    def __init__(self, distance, duration, input_date="2024-01-24"):
        self.distance = distance
        self.duration = timedelta(seconds=duration)
        self.date = date.fromisoformat(input_date)

    def get_distance(self):
        return self.distance
    
    def get_duration(self):
        return self.duration
    
    def get_date(self):
        return self.date
    
    def compute_pace(self):
        return self.duration / self.distance
    
    def compute_speed(self):
        return self.distance / self.duration.seconds * 3600

class User:
    
    def __init__(self):
        self.sessions = list()
    
    def get_sessions(self):
        return self.sessions
    
    def add_session(self, session):
        self.sessions.append(session)

    def compute_avg_distance(self):
        sum_distance = sum(session.get_distance() for session in self.sessions)
        return sum_distance / len(self.sessions)
