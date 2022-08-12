import random as rnd
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt


class generate_Customers:
    def __init__(self):
        self.ItemNum = 0
        self.ArrTime = 0.0
        self.QinTime = 0.0
        self.QoutTime = 0.0
        self.SinTime = 0.0
        self.SoutTime = 0.0
        self.rework = 0


def random_variate_generation(Myparameter):
    u = np.random.uniform(0, 1)
    print()
    x = -1 * (1 / Myparameter) * np.log(1 - u)
    return x


class Sim_model:
    def __init__(self):
        self.lamda = 10
        self.Mu = 8
        self.QCapacity = 9
        self.Qdiscipline = "FCFS"

        self.num_in_system = 0
        self.clock = 0.0
        self.t_arrival = self.generate_interarrival()
        # print("ArrivalTime: ",self.t_arrival)
        self.t_depart = float('inf')
        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0
        self.Que = []
        self.SQue = []
        self.serverStatus = 0
        self.Outputs = []
        self.Skips = []

    def advance_time(self):
        t_event = min(self.t_arrival, self.t_depart)

        self.total_wait += self.num_in_system * (t_event - self.clock)

        self.clock = t_event

        if self.t_arrival >= self.t_depart:
            print("Simulation Clock :", self.clock, " -- Departure of Customer")
            self.handle_depart_event()
        else:
            print("Simulation Clock :", self.clock, " -- Arrival of Customer")
            self.handle_arrival_event()

    def handle_arrival_event(self):
        self.num_in_system += 1
        self.num_arrivals += 1
        Customers = generate_Customers()
        # print("New Gen ITem Customers",Customers.ItemNum)
        # print("self.num_arrivals",self.num_arrivals)

        Customers.ItemNum = self.num_arrivals
        Customers.ArrTime = self.clock

        if self.num_in_system <= 1:  # if server is free
            self.t_depart = self.clock + self.generate_service()
            self.serverStatus = 1
            Customers.QinTime = self.clock
            Customers.QoutTime = self.clock
            Customers.SinTime = self.clock
            self.SQue.append(Customers)
            # print("item goes to service",self.SQue)
        else:
            # checking (if Que has Space or not)
            if len(self.Que) >= self.QCapacity:
                # print("Queue is full" , self.Que)
                self.Skips.append(Customers)
                self.num_in_system -= 1
            else:
                self.Que.append(Customers)
                Customers.QinTime = self.clock
                # print("Item goest to self.Que",self.Que)

        self.t_arrival = self.clock + self.generate_interarrival()

    def handle_depart_event(self):
        self.num_in_system -= 1
        self.num_departs += 1
        currItem = self.SQue[0]
        currItem.SoutTime = self.clock
        self.Outputs.append(currItem)

        if self.num_in_system > 0:
            # if(len(self.Que[0])>0)
            if self.Qdiscipline == "FCFS":
                Nextitem = self.Que[0]
            elif self.Qdiscipline == "LCFS":
                Nextitem = self.Que[-1]

            Nextitem.QoutTime = self.clock
            Nextitem.SinTime = self.clock
            self.SQue[0] = Nextitem
            # print("item goes to service",self.SQue)
            if self.Qdiscipline == "FCFS":
                self.Que = self.Que[1:]
            elif self.Qdiscipline == "LCFS":
                self.Que = self.Que[0:-1]

            self.t_depart = self.clock + self.generate_service()
        else:
            self.t_depart = float('inf')
            self.SQue = []

    def generate_interarrival(self):
        return random_variate_generation(self.lamda)

    def generate_service(self):
        return random_variate_generation(self.Mu)


np.random.seed(10)
sim = Sim_model()
RunTime = 100
sim.Qdiscipline = "LCFS"
StatusTime = []
CustomersinSys = []
TimeFull = []
initialTime = 0
eventwhenKisfull = 0

while sim.clock <= RunTime:
    # print("Simulation Clock : ",sim.num_in_system)
    sim.advance_time()
    print("num_arrivals ", sim.num_arrivals)
    print("num_in_system ", sim.num_in_system)

    StatusTime.append(sim.clock)
    CustomersinSys.append(sim.num_in_system)

    if sim.num_in_system == 10:
        if eventwhenKisfull == 0:
            eventwhenKisfull = 1
            initialTime = sim.clock
        else:
            TimeFull.append(sim.clock - initialTime)
            initialTime = sim.clock

    if sim.num_in_system != 10:
        if eventwhenKisfull == 1:
            TimeFull.append(sim.clock - initialTime)
            eventwhenKisfull = 0

    print("num_in_queue ", len(sim.Que))
    print("num_in_service ", len(sim.SQue))
    print("num_departs ", sim.num_departs)
    print("num_in_skips ", len(sim.Skips))
    print("----------")
