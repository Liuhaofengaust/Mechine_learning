### 待办

* class Lambda(nn.Module):   # ????????
    def __init__(self, func):
        super().__init__()
        self.func = func
        
    def forward(self, x):
        return self.func(x)
* image_datasets = {x:datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x])
                      for x in ["train", "val"]}
