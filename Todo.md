### 待办

* class Lambda(nn.Module):   # ????????
    def __init__(self, func):
        super().__init__()
        self.func = func
        
    def forward(self, x):
        return self.func(x)
