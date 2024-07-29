import pandas as pd
import numpy as np
import faiss
from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel
from sklearn.preprocessing import normalize

# Load the GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
text_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def embed_text(texts):
    inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True, max_length=512)
    outputs = model(**inputs, output_hidden_states=True)
    embeddings = outputs.hidden_states[-1].mean(dim=1).detach().numpy()
    return normalize(embeddings)  # Normalizing embeddings

# Load your DataFrame
df = pd.read_csv('output_new.csv').dropna()  # Adjust path as needed
texts = df['Reviews'].tolist()  # Replace with your actual column name

def print_non_strings(lst):
    for item in lst:
        if not isinstance(item, str):
            print(f"Non-string item: {item}")

print_non_strings(texts)

# Batch processing to reduce memory usage
batch_size = 100  # Adjust batch size based on available memory
all_embeddings = []

for i in range(0, len(texts), batch_size):
    batch_texts = texts[i:i + batch_size]
    batch_embeddings = embed_text(batch_texts)
    all_embeddings.append(batch_embeddings)

embeddings = np.vstack(all_embeddings)

# Initialize FAISS index with a more memory-efficient index type
dimension = embeddings.shape[1]
index = faiss.IndexIVFFlat(faiss.IndexFlatL2(dimension), dimension, 100)  # Using IVF index
index.train(embeddings)  # Train the index
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, 'faiss_index.index')

# Function to query FAISS and generate response
def get_response(query, k=5):
    query_embedding = embed_text([query])[0]
    _, indices = index.search(np.array([query_embedding]), k)
    
    relevant_texts = [texts[i] for i in indices[0]]
    context = ' '.join(relevant_texts)
    
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = text_generator(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']
    
    return response

# Example usage
query = "Your query here"
print(get_response(query))

