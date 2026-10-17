# Day 20 — AI Fundamentals + Open-Source LLMs

## 1. AI, ML, Deep Learning, GenAI and LLMs

- **AI (Artificial Intelligence):** The broad field of making computers perform tasks that normally require human intelligence.
- **ML (Machine Learning):** A subset of AI that learns patterns from training data to make predictions or decisions.
- **Deep Learning (DL):** A subset of ML that uses neural networks with multiple layers.
- **Generative AI:** AI that generates new content, such as text, images, videos and code.
- **LLM (Large Language Model):** A model trained on large amounts of data to process and generate language.

**Simplified relationship:**

AI → ML → Deep Learning → Generative AI → LLMs

*Note: This is a simplified learning flow, not a strict hierarchy covering every AI technique.*

## 2. Transformers, Tokens and Embeddings

- **Transformer:** A neural network architecture used by many modern LLMs.
- **Attention:** Helps a model understand which parts of the input are relevant to one another.
- **Token:** A piece of text. It can be a complete word, part of a word or punctuation.
- **Embedding:** A numerical representation of information that helps models and search systems work with patterns and meaning.

**Basic LLM flow:**

Text → Tokens → Numerical representations → Transformer layers → Next-token prediction → Generated response.

Many modern LLMs generate text by repeatedly predicting the next token.

## 3. RAG (Retrieval-Augmented Generation)

**Meaning:** RAG retrieves relevant external information and gives it to an LLM as context before generating an answer.

**Example:** An employee asks about the company's refund policy. The application searches company documents and gives the relevant policy to the LLM.

**Basic workflow:**

User question → Retrieve relevant information → Give information to the LLM → Generate answer.

- Embeddings can help retrieve information with similar meaning.
- A vector database or another search system can store and retrieve document chunks.
- RAG does not require retraining the model whenever a document changes; the document store or index may need updating.
- RAG can reduce unsupported answers but does not guarantee correctness.
- RAG can also use keyword search instead of embeddings.

## 4. Open-Weight LLMs and Hugging Face

- **Open-weight LLM:** A model whose trained weights are available under its licence. This does not necessarily mean its training data and entire development process are open.
- **Hugging Face:** A platform and ecosystem for discovering and working with AI models, datasets and tools.
- **Ollama:** Software for running compatible AI models locally.
- **Qwen3:4b:** The LLM used in my local Ollama setup.

**Remember:** Hugging Face helps me discover models; Ollama helps me run a compatible model locally.

Companies may use open-weight models for greater deployment control, privacy options and cost flexibility, depending on the model, licence and infrastructure.

## 5. Local Inference vs Cloud API

**Inference** means using a trained model to generate an answer or prediction.

### Local inference
The model runs on my own computer.

Example: Python → Ollama → Qwen3:4b → Response.

- Can run without internet after setup and model download.
- Can avoid per-request model API charges.
- Depends on my computer's processing power and memory.
- Prompts can remain local if the application does not send them elsewhere.

### Cloud API
The model runs on a provider's remote servers.

Example: Python → Claude API → Response.

- Normally requires internet and API access.
- May be free or paid, depending on the provider and usage.
- Can provide access to models that are impractical to run locally.
- Requires attention to provider data-handling policies.

## 6. Prompting vs RAG vs Fine-tuning vs LoRA

### Prompting
Giving the model clear instructions.

Example: “Classify this customer message as billing, refund, technical or other. Return valid JSON.”

**Use when:** You need to guide the model's task, format or behaviour.

### RAG
Retrieving relevant external information and providing it to the model.

Example: Answering employee questions using company PDFs.

**Use when:** The model needs access to company-specific or frequently changing information.

### Fine-tuning
Training an existing model further using additional examples to adapt its behaviour or task performance.

Example: Adapting a model for a specialised classification task using labelled examples.

**Use when:** Prompting and other approaches are insufficient, and suitable training data and resources are available.

### LoRA (Low-Rank Adaptation)
A parameter-efficient fine-tuning technique that trains a small set of additional parameters rather than updating all the original model parameters.

**Use when:** Adapting a compatible model with less training compute and memory than full fine-tuning may require.

**Quick comparison:**

| Approach | What changes? |
|---|---|
| Prompting | Instructions |
| RAG | Information supplied at answer time |
| Fine-tuning | Learned model parameters |
| LoRA | A smaller set of trainable additional parameters |

These approaches can be combined in the same application.

## 7. What Does Building an LLM Mean?

There are different levels of work:

1. **Using an LLM:** Sending prompts to an existing model.
2. **Building an LLM-powered application:** Connecting an existing model with Python, tools, validation, retrieval and storage.
3. **Customizing an LLM:** Using approaches such as RAG or fine-tuning.
4. **Training an LLM from scratch:** Designing and training a new model from initialized parameters using training data and computing resources.

Training a small language model from scratch can be a useful learning exercise. Training a highly capable, large-scale LLM requires substantially more data, compute and expertise.

For AI automation and GenAI application development, building useful applications with existing models is an important starting skill.

## 8. What Is an AI Agent?

An **AI agent** is a system that can use a model, tools and control logic to choose actions toward a goal. It may observe results and decide what to do next.

Example: A customer-support agent looks up an order, checks refund eligibility and follows an authorised refund workflow.

- **LLM:** The model.
- **AI-powered application:** Software that uses AI to perform a task.
- **Tool calling:** A model requests that a tool be used.
- **AI agent:** A system that can choose and perform actions toward a goal.

Not every tool-calling application is a full agent.

## 9. Key Takeaways

- ML learns patterns; Generative AI generates content.
- Transformers power many modern LLMs.
- Embeddings represent information numerically.
- RAG gives an LLM relevant external information.
- Hugging Face helps discover models; Ollama runs compatible models locally.
- Local inference and cloud APIs are different ways to access models.
- Prompting changes instructions; RAG supplies information; fine-tuning adapts model parameters; LoRA makes certain fine-tuning approaches more efficient.
- Building an LLM-powered application is different from training an LLM from scratch.
- An AI agent can use tools and make decisions to work toward a goal.

## Day 20 Status

**Theory:** Covered  
**Conceptual practice:** Completed  
**Future practical work:** Build a RAG application and explore fine-tuning/LoRA when appropriate.