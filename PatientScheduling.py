class Patient:
    def __init__(self, name, arrival_time, treatment_time, urgency_level):
        self.name = name
        self.arrival_time = arrival_time
        self.treatment_time = treatment_time
        self.urgency_level = urgency_level

    def __str__(self):
        return f"{self.name}: {self.arrival_time}, {self.treatment_time}, {self.urgency_level}"

def fcfs_scheduling(patients):
    return patients

def sjf_scheduling(patients):
    patients.sort(key=lambda patient: patient.treatment_time)
    return patients

def ps_scheduling(patients):
    patients.sort(key=lambda patient: patient.urgency_level, reverse=True)
    return patients

def rr_scheduling(patients, time_quantum=1):
    queue = []
    for patient in patients:
        queue.append(patient)

    while queue:
        patient = queue.pop(0)
        patient.treatment_time -= time_quantum

        if patient.treatment_time <= 0:
            yield patient
        else:
            queue.append(patient)

if __name__ == "__main__":
    patients = [
        Patient("A", 0, 30, 3),
        Patient("B", 10, 20, 5),
        Patient("C", 15, 40, 2),
        Patient("D", 20, 15, 4),
    ]

    # FCFS scheduling
    fcfs_schedule = fcfs_scheduling(patients.copy())
    print("FCFS schedule:")
    for patient in fcfs_schedule:
        print(patient)

    # SJF scheduling
    sjf_schedule = sjf_scheduling(patients.copy())
    print("SJF schedule:")
    for patient in sjf_schedule:
        print(patient)

    # PS scheduling
    ps_schedule = ps_scheduling(patients.copy())
    print("PS schedule:")
    for patient in ps_schedule:
        print(patient)

    # RR scheduling
    rr_schedule = rr_scheduling(patients.copy())
    print("RR schedule:")
    for patient in rr_schedule:
        print(patient)
