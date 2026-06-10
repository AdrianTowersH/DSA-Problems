# Markov chain
# Import tools from the collections module to handle missing keys and count frequencies
from collections import defaultdict, Counter

# Define a class that implements a basic Markov Chain for text prediction
class WordPredictor:
    # The constructor method initializes the object (fixed to use double underscores __init__)
    def __init__(self, data):
        # Create a nested dictionary where missing keys automatically create a new Counter object
        # Structure: { "current_word": Counter({"next_word": count}) }
        self.chain = defaultdict(Counter)
        # Automatically train the model using the dataset passed during initialization
        self._train(data)

    # Internal helper method to build the word transition frequency dictionary
    def _train(self, data):
        # Loop through each sentence/sequence of words in the provided dataset
        for sequence in data:
            # Loop through the list indices, stopping at the second-to-last item to prevent an IndexError
            for i in range(len(sequence) - 1):
                # Identify the word at the current position
                current_word = sequence[i]
                # Identify the word immediately following the current word
                next_word = sequence[i + 1]
                # Look up the current word, access its Counter, and increment the count for the next word by 1
                self.chain[current_word][next_word] += 1

    # Method to predict the most likely next word based on a given input word
    def predict(self, word):
        # Check if the input word was never seen during training; if so, we can't predict anything
        if word not in self.chain:
            # Return None to indicate no prediction is available
            return None
        
        # self.chain[word].most_common(1) returns a list like: [("next_word", count)]
        # [0] grabs the first tuple from that list, and [0][0] extracts just the word string
        most_common_next = self.chain[word].most_common(1)[0][0]
        # Return the final predicted word
        return most_common_next

# --- Example Usage ---

# Sample dataset consisting of tokenized sentences (lists of words)
input_data = [["I", "am", "pete"], ["pete", "I", "am"], ["I", "am", "zebra"]]

# Create an instance of WordPredictor, passing the sample data to train it
predictor = WordPredictor(input_data)

# Define the target word we want to test our predictor with
word_to_test = "I"

# Call the predict method to find out what word most frequently follows "I"
result = predictor.predict(word_to_test)

# Print the result to the console
print(f"La palabra más común después de '{word_to_test}' es: '{result}'")