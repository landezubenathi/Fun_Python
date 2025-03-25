from duckduckgo_search import DDGS

def get_search_answer(query):
    # Check if the query is a math equation
    try:
        result = eval(query)  # Evaluate the math expression safely
        return f"The result of {query} is: {result}"
    except:
        # If it's not a math equation, perform a normal search
        results = DDGS().text(query, max_results=1)
        for result in results:
            return result["body"]  # Extract the actual answer text
        
        return "No relevant answer found."

#query = "How many Provinces in South Africa"
#result = get_search_answer(query)
#print(result)
