#!/usr/bin/python
# -*- coding: utf-8 -*-

from .. import core as c


class VariableBase:
    def __init__(self):
        pass

    def GetVariableMemoryAddr(self):
        raise NotImplementedError('override')

    # -------

    def AtLeast(self, value):
        return c.Memory(self.GetVariableMemoryAddr(), c.AtLeast, value)

    def AtMost(self, value):
        return c.Memory(self.GetVariableMemoryAddr(), c.AtMost, value)

    def Exactly(self, value):
        return c.Memory(self.GetVariableMemoryAddr(), c.Exactly, value)

    # -------

    def SetNumber(self, value):
        return c.SetMemory(self.GetVariableMemoryAddr(), c.SetTo, value)

    def AddNumber(self, value):
        return c.SetMemory(self.GetVariableMemoryAddr(), c.Add, value)

    def SubtractNumber(self, value):
        return c.SetMemory(self.GetVariableMemoryAddr(), c.Subtract, value)

    # -------

    def Assign(self, value):
        c.Trigger(actions=c.SetMemory(self.GetVariableMemoryAddr(), c.SetTo, value))

    def __lshift__(self, value):
        self.Assign(value)

    def __iadd__(self, value):
        c.Trigger(actions=c.SetMemory(self.GetVariableMemoryAddr(), c.Add, value))

    def __isub__(self, value):
        c.Trigger(actions=c.SetMemory(self.GetVariableMemoryAddr(), c.Subtract, value))

    # -------

    def __eq__(self, other):
        return self.Exactly(other)

    def __le__(self, other):
        return self.AtMost(other)

    def __ge__(self, other):
        return self.AtLeast(other)
