import os
name = (
    os.environ.get("SEMAPHORE_NAME") or 
    os.environ.get("name") or 
    os.environ.get("SEMAPHORE_SURVEY_NAME") or
    os.environ.get("ANSIBLE_NAME") or
    "No Name Provided"
)
print(f"Hello World....{name}")
