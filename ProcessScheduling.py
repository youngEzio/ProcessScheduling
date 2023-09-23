def fcfs(processes):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    schedule_order = []

    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            completion_time[i] = max(processes[i][1], completion_time[i - 1]) + processes[i][2]

        waiting_time[i] = completion_time[i] - processes[i][1]
        turnaround_time[i] = waiting_time[i] + processes[i][2]
        schedule_order.append(processes[i][0])

    return waiting_time, turnaround_time, schedule_order


def sjf(processes):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    schedule_order = []

    processes.sort(key=lambda x: (x[2], x[1]))

    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            completion_time[i] = max(processes[i][1], completion_time[i - 1]) + processes[i][2]

        waiting_time[i] = completion_time[i] - processes[i][1]
        turnaround_time[i] = waiting_time[i] + processes[i][2]
        schedule_order.append(processes[i][0])

    return waiting_time, turnaround_time, schedule_order


def ps(processes):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    schedule_order = []

    processes.sort(key=lambda x: (x[3], x[1]))

    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            completion_time[i] = max(processes[i][1], completion_time[i - 1]) + processes[i][2]

        waiting_time[i] = completion_time[i] - processes[i][1]
        turnaround_time[i] = waiting_time[i] + processes[i][2]
        schedule_order.append(processes[i][0])

    return waiting_time, turnaround_time, schedule_order


def rr(processes, time_quantum=4):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    schedule_order = []
    remaining_burst_time = [process[2] for process in processes]

    time = 0
    while any(remaining_burst_time):
        for i in range(n):
            if remaining_burst_time[i] > 0:
                if remaining_burst_time[i] <= time_quantum:
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - processes[i][1] - processes[i][2]
                    turnaround_time[i] = waiting_time[i] + processes[i][2]
                    remaining_burst_time[i] = 0
                else:
                    time += time_quantum
                    remaining_burst_time[i] -= time_quantum
                schedule_order.append(processes[i][0])

    return waiting_time, turnaround_time, schedule_order

def average_waiting_time(waiting_times):
    return sum(waiting_times) / len(waiting_times)


def average_turnaround_time(turnaround_times):
    return sum(turnaround_times) / len(turnaround_times)


if __name__ == "__main__":
    processes = [
        ("P1", 0, 24, 3),
        ("P2", 4, 3, 1),
        ("P3", 5, 3, 4),
        ("P4", 6, 12, 2)
    ]

    n = len(processes)

    print("\nFCFS Scheduling:")
    fcfs_waiting_time, fcfs_turnaround_time, fcfs_schedule_order = fcfs(processes)
    for i in range(n):
        print(f"{processes[i][0]} - Waiting Time: {fcfs_waiting_time[i]}, Turnaround Time: {fcfs_turnaround_time[i]}")
    print("Order of Execution:", "->".join(fcfs_schedule_order))
    print(f"Average Waiting Time: {average_waiting_time(fcfs_waiting_time)}")
    print(f"Average Turnaround Time: {average_turnaround_time(fcfs_turnaround_time)}")

    print("\nSJF Scheduling:")
    sjf_waiting_time, sjf_turnaround_time, sjf_schedule_order = sjf(processes)
    for i in range(n):
        print(f"{processes[i][0]} - Waiting Time: {sjf_waiting_time[i]}, Turnaround Time: {sjf_turnaround_time[i]}")
    print("Order of Execution:", "->".join(sjf_schedule_order))
    print(f"Average Waiting Time: {average_waiting_time(sjf_waiting_time)}")
    print(f"Average Turnaround Time: {average_turnaround_time(sjf_turnaround_time)}")

    print("\nPriority Scheduling:")
    ps_waiting_time, ps_turnaround_time, ps_schedule_order = ps(processes)
    for i in range(n):
        print(f"{processes[i][0]} - Waiting Time: {ps_waiting_time[i]}, Turnaround Time: {ps_turnaround_time[i]}")
    print("Order of Execution:", "->".join(ps_schedule_order))
    print(f"Average Waiting Time: {average_waiting_time(ps_waiting_time)}")
    print(f"Average Turnaround Time: {average_turnaround_time(ps_turnaround_time)}")

    print("\nRound Robin Scheduling:")
    rr_waiting_time, rr_turnaround_time, rr_schedule_order = rr(processes)
    for i in range(n):
        print(f"{processes[i][0]} - Waiting Time: {rr_waiting_time[i]}, Turnaround Time: {rr_turnaround_time[i]}")
    print("Order of Execution:", "->".join(rr_schedule_order))
    print(f"Average Waiting Time: {average_waiting_time(rr_waiting_time)}")
    print(f"Average Turnaround Time: {average_turnaround_time(rr_turnaround_time)}")

