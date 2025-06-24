from symbolic_postprocessor_locked import SymbolicPostProcessor

# Initialize the symbolic-governed model
model = SymbolicPostProcessor(model_name="mistralai/Mistral-7B-Instruct-v0.2")

# Run a simple prompt through the model
response = model.generate("What is 5 + 6?")
print("Model response:", response)
