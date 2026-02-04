#gets name, corects capitalization, 
# extracts first name, and formats greeting
def format_greeting(name, title="Customer"):
    clean_name = name.strip()
    if not clean_name:
        return "Hello, VIP Customer!"
    clean_name = clean_name.title()
    first_name = clean_name.split()[0]
    return f"Hello, {first_name} ({title})!"

# input name and it outputs customer greeting
full_name = input("Enter your full name: ")
greeting = format_greeting(full_name)
print(greeting)