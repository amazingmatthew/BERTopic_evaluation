

# Trainer and DataLoader

from evaluation import Trainer, DataLoader

%%time
dataloader = DataLoader(dataset="trump").prepare_docs(save="trump.txt").preprocess_octis(output_folder="trump")
%%time
dataloader = DataLoader(dataset="trump_dtm").prepare_docs(save="trump_dtm.txt").preprocess_octis(output_folder="trump_dtm")


