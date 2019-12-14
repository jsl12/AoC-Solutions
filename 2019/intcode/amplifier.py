from itertools import permutations

from .computer import Computer as IC


class AmpSystem:
    def __init__(self, input, len=5):
        self.amps = [IC(input) for i in range(len)]

    def reset(self):
        for a in self.amps:
            a.reset()

    def assign_inputs(self, inputs):
        for i, a in enumerate(self.amps):
            a.inputs.append(inputs[i])

    def max_thruster_signal(self, possible_settings):
        return max([self.run(list(settings)) for settings in permutations(possible_settings)])

    def run(self, settings, signal = 0):
        self.reset()
        self.assign_inputs(settings)
        self.amps[0].inputs.append(signal)
        while self.amps[-1].op != 99:
            # for each amplifier, try to operate
            for i, a in enumerate(self.amps):
                # check for any outputs ready to go
                if self.amps[i-1].outputs:
                    for j in range(len(self.amps[i-1].outputs)):
                        a.inputs.append(self.amps[i-1].outputs.pop(0))
                if a.op == 3 and not a.inputs:
                    # if it needs an input and there are none available, then skip
                    continue
                try:
                    a.run()
                except IndexError:
                    # hits an index error when it tries to pull an input and there are none available
                    continue
        return self.amps[-1].outputs[0]
