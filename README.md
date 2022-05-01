# Neutral Networks

### What is Deep Learning?
Deep learning is a branch of machine learning which is completely based on artificial neural networks, as neural network is going to mimic the human brain so deep learning is also a kind of mimic of human brain.

> "Deep learning is a particular kind of machine learning that achieves great power and flexibility by learning to represent the world as a nested hierarchy of concepts, with each concept defined in relation to simpler concepts, and more abstract representations computed in terms of less abstract ones."

The question here is how do we recreate these neurons in a computer. So, we create an artificial structure called an artificial neural net where we have nodes or neurons. We have some neurons for input value and some for output value and in between, there may be lots of neurons interconnected in the hidden layer.

### Architectures :
1. **Deep Neural Network** – It is a neural network with a certain level of complexity (having multiple hidden layers in between input and output layers). They are capable of modeling and processing non-linear relationships.
2. **Deep Belief Network(DBN)** – It is a class of Deep Neural Network. It is multi-layer belief networks.
Steps for performing DBN :
- a. Learn a layer of features from visible units using Contrastive Divergence algorithm.
- b. Treat activations of previously trained features as visible units and then learn features of features.
- c. Finally, the whole DBN is trained when the learning for the final hidden layer is achieved.
3. **Recurrent Neural Network** – Allows for parallel and sequential computation. Similar to the human brain (large feedback network of connected neurons). They are able to remember important things about the input they received and hence enables them to be more precise.

### Applications :
- **Automatic Text Generation** – Corpus of text is learned and from this model new text is generated, word-by-word or character-by-character.
Then this model is capable of learning how to spell, punctuate, form sentences, or it may even capture the style.
- **Healthcare** – Helps in diagnosing various diseases and treating it.
- **Automatic Machine Translation** – Certain words, sentences or phrases in one language is transformed into another language (Deep Learning is achieving top results in the areas of text, images).
- **Image Recognition** – Recognizes and identifies peoples and objects in images as well as to understand content and context. This area is already being used in Gaming, Retail, Tourism, etc.
