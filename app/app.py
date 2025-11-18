from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "my test post"},
    2: {"title": "Python Dictionary Deep Dive", "content": "Dictionaries are awesome for key-value pairs. They're implemented as hash tables and offer O(1) average time complexity for lookups, insertions, and deletions. Very fast!"},
    3: {"title": "Quick List Comprehension Example", "content": "Did you know you can simplify loops? Try: squares = [x**2 for x in range(10)]. It's concise and often faster than a traditional for loop."},
    4: {"title": "Web Scraping with Requests and BeautifulSoup", "content": "Need data? The 'requests' library fetches the HTML, and 'BeautifulSoup' parses it beautifully. Essential tools for any data-focused Python project."},
    5: {"title": "The Zen of Python (PEP 20)", "content": "Remember the key principles: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Always guide your code!"},
    6: {"title": "Understanding Python Decorators", "content": "A **decorator** is a function that takes another function and extends or modifies its behavior without explicitly modifying it. It's often written using the `@` symbol above the function definition."},
    7: {"title": "Introduction to Object-Oriented Programming (OOP)", "content": "OOP focuses on using **objects** (instances of **classes**) to design applications and computer programs. Key concepts are encapsulation, inheritance, and polymorphism."},
    8: {"title": "Handling Exceptions with Try/Except", "content": "Always anticipate errors! Use **try** to wrap the code that might fail and **except** to gracefully handle the resulting error (like `ZeroDivisionError` or `FileNotFoundError`)."},
    9: {"title": "Working with F-Strings", "content": "F-strings (formatted string literals) provide a concise, readable way to embed Python expressions inside string literals. Example: `f'My name is {name}'`."},
    10: {"title": "Git: Essential Version Control", "content": "Every developer needs Git! It's a distributed version control system that lets you track changes, collaborate effectively, and revert to previous states using commands like `commit`, `pull`, and `push`."}
}

@app.get("/post")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts
@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)