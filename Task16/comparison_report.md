# RAG Retrieval Performance Comparison Report

## Objective

The objective of this experiment was to evaluate how different document chunk sizes affect the retrieval performance of a basic Retrieval-Augmented Generation (RAG) system.

The company documentation was divided into different chunk sizes, converted into embeddings, and retrieved using semantic similarity.

## Chunk Sizes Tested

Three chunk sizes were tested:

- 50 words
- 100 words
- 150 words

The same set of questions was used for every chunk size to maintain a consistent comparison.

## Questions Used

1. What is HearMe?
2. How does HearMe process a customer call?
3. How is ASR performance evaluated?
4. How can RAG improve HearMe?

## Evaluation Method

The `all-MiniLM-L6-v2` Sentence Transformer model was used to convert the document chunks and user questions into embeddings.

Cosine similarity was then calculated between each question embedding and the document chunk embeddings.

For each question, the chunk with the highest similarity score was selected as the retrieved context.

Higher similarity scores indicate stronger semantic similarity between the question and the retrieved document chunk.

## Response Evaluation Table

The complete evaluation results are available in:

`response_evaluation.csv`

The table contains:

- Chunk Size
- Question
- Similarity Score
- Retrieved Context

## Chunk Size Comparison

### 50-Word Chunks

The 50-word chunk size divides the documentation into smaller and more focused sections.

Advantages:

- More focused retrieval
- Less unrelated information in each chunk
- Useful for specific questions

Limitation:

- Important surrounding context may sometimes be separated into another chunk.

### 100-Word Chunks

The 100-word chunk size provides more contextual information while maintaining reasonably focused retrieval.

Advantages:

- Good balance between context and retrieval precision
- More complete information can be retrieved in a single chunk

Limitation:

- May contain some information that is not directly related to the question.

### 150-Word Chunks

The 150-word chunk size provides larger sections of the source document.

Advantages:

- Provides more surrounding context
- Useful when an answer depends on information across multiple sentences

Limitation:

- Larger chunks may include unrelated information and reduce retrieval precision.

## Performance Analysis

The average cosine similarity score for each chunk size was calculated using the results from all test questions.

The chunk size with the highest average similarity score was considered the strongest performer for this specific retrieval experiment.

The experiment demonstrates that chunk size has a direct effect on semantic retrieval quality.

Smaller chunks tend to provide more focused information, while larger chunks provide additional context. Therefore, selecting an appropriate chunk size requires balancing retrieval precision with contextual completeness.

## Best Chunk Size

The best-performing chunk size should be selected according to the actual average similarity scores generated in `rag_pipeline.ipynb`.

The result is specific to this dataset, embedding model, and set of evaluation questions and should not be interpreted as a universally optimal RAG chunk size.

## Conclusion

The experiment successfully compared retrieval performance across 50-word, 100-word, and 150-word document chunks.

The results demonstrate the importance of chunk-size selection when building RAG systems. An appropriate chunk size can improve the relevance of retrieved information and provide better context for downstream answer generation.