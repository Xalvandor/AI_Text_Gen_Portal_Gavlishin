import pickle, torch

# Check the checkpoint's vocab_size
ckpt = torch.load('out/ckpt.pt', map_location='cpu')
print("Model vocab_size:", ckpt['model_args']['vocab_size'])

# Check the meta.pkl vocab_size
with open('myNanoGPT/data/movies/meta.pkl', 'rb') as f:
    meta = pickle.load(f)
print("Meta vocab_size:", meta['vocab_size'])