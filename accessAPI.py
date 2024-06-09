import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'
def get_chapter_summary(book, chapter):
    url = f"{base_url}{book.lower()}/{chapter}/summary"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('summary', "Invalid summary reques.")
    else:
        return "Sorry, please enter a valid chapter reference"

def main():
    print("Welcome to the Book of Mormon Summary Tool!")
    while True:
        book = input("Which book of mormon would you like to get the summary on? ")
        chapter = input(f"Which chapter of {book} are you interested in? ")
        
        summary = get_chapter_summary(book, chapter)
        print(f"\nSummary of {book} chapter {chapter}:\n--{summary}\n")

        choice = input("Would you like to view another (Y/N)? ").strip().lower()
        if choice != 'y':
            break
    
    print("Thank you for using Book of Mormon Summary Tool!")

if __name__ == "__main__":
    main()
