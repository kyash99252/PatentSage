import ollama

prompt_text = "The sky is blue because of Rayleigh scattering."

try:
    response = ollama.embeddings(
        model='nomic-embed-text', # Make sure this model name matches what you pulled
        prompt=prompt_text
    )
    print(f"Embedding for '{prompt_text}':")
    print(response['embedding'])

except ollama.ResponseError as e:
    print(f"Error generating embedding: {e}")
    if e.status_code == 404:
        print(f"Model '{response['model']}' not found. Make sure it's pulled using `ollama pull {response['model']}` inside your Ollama container.")
    else:
        print("Check if your Ollama server is running and accessible.")