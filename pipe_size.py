import argparse


class WaterPipeManager:
    
    def __init__(self, pipe_list, flow_list, tol):

        self.pipe_list = pipe_list 
        self.flow_list = flow_list
        self.tol = tol

    def compute_velocity(self, q, d):

        return 1274*q/ (d*d)

    def size_water_pipe(self):
        result = []
        for idx, l in enumerate(self.flow_list):
            tmp = -1
            for id, d in enumerate(self.pipe_list):
                v = self.compute_velocity(l, d)
                if d <=50:
                    if v <=1.15 * (1+self.tol): 
                        tmp = d 
                        break
                else:
                    if v > 1.15 * (1-self.tol) and v <=2.0:
                        tmp = d
                        break
            result.append(tmp)    

        return result

if __name__ == "__main__":
## ===== ===== ===== ===== ===== ===== ===== =====
## Parse arguments
## ===== ===== ===== ===== ===== ===== ===== =====

    parser = argparse.ArgumentParser(description = "Water Pipe Sizer");

    parser.add_argument('--pipe_dia', action='store',
                    type=int, nargs='*', default=[25,32,40,50,65,80,100,150,200,250,300],
                    help="Pipe Diameters for consideration")
    parser.add_argument('--flow_list', action='store',
                    type=float, nargs='*', default=[],
                    help="Flow Rate for consideration")
    parser.add_argument('--tol', type=float, default=0.2, help='Tolerance');

    args = parser.parse_args();

    worker = WaterPipeManager(args.pipe_dia, args.flow_list, args.tol)
    print(worker.size_water_pipe())


