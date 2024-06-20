# Movie Recommendation System

This repository contains a movie recommendation system that uses content-based filtering to suggest movies similar to a user-provided title. The system leverages various features from the movie dataset, including genres, keywords, tagline, cast, and director, to compute similarity scores and recommend movies.

## Features

- **Data Loading**: Loads movie data from a CSV file into a pandas DataFrame.
- **Data Preprocessing**: Cleans and combines selected features to create a single string for each movie.
- **Vectorization**: Converts combined text data into numerical feature vectors using TF-IDF.
- **Similarity Computation**: Calculates cosine similarity scores between movies based on their feature vectors.
- **User Interaction**: Prompts the user to input a movie name and provides a list of 30 recommended movies based on similarity scores.
- **Error Handling**: Manages cases where the movie title is not found in the dataset, ensuring a smooth user experience.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/movierecommendation.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd movierecommendation
   ```

3. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install numpy pandas scikit-learn
   ```

4. **Run the Script**:
   ```bash
   python recommendation_system.py
   ```

5. **Follow the Prompts**:
   Enter a movie name when prompted to receive a list of recommended movies. Type 'q' to quit the program.

## Example

```plaintext
Enter your movie name: Inception
30 Movies Suggested for you:
1. Interstellar
2. The Dark Knight
3. Memento
...
```

## Note

- Ensure the CSV file containing movie data is located at the specified path in the script.
- Modify the script as needed to fit your data's file path and structure.

---

This description provides a clear and structured overview of the project, instructions for usage, and an example of how the system works.
