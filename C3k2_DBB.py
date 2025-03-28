class C3k2_DBB(C3k2):
    def __init__(self, c1, c2, n=1, c3k=False, e=0.5, g=1, shortcut=True):
        super().__init__(c1, c2, n, c3k, e, g, shortcut)
        self.m = nn.ModuleList(C3k_DBB(self.c, self.c, 2, shortcut, g) if c3k else Bottleneck_DBB(self.c, self.c, shortcut, g) for _ in range(n))