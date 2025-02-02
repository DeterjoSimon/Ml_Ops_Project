import torch
import random
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW
import numpy as np
from IPython import embed
def myModel():
    # Use a GPU if you have one available (Runtime -> Change runtime type -> GPU)
    #device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Set seeds for reproducibility
    random.seed(26)
    np.random.seed(26)
    torch.manual_seed(26)


    model = AutoModelForSequenceClassification.from_pretrained("roberta-base")
    #model.to(device) # Send the model to the GPU if we have one


    return model
