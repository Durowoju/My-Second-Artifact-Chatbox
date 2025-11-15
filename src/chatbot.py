import json
import textwrap

DATA_PATH = "data/presentations.json"


def load_speakers(path=DATA_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def list_speakers(speakers):
    print("\nAvailable speakers:\n")
    for sp in speakers:
        print(f"- {sp['name']} — {sp['presentation_title']}")
    print()


def find_by_name(speakers, name_query: str):
    name_query = name_query.lower()
    for sp in speakers:
        if name_query in sp["name"].lower() or name_query in sp["id"].lower():
            return sp
    return None


def find_by_tag(speakers, tag_query: str):
    tag_query = tag_query.lower().replace("#", "")
    results = []
    for sp in speakers:
        for t in sp.get("tags", []):
            if tag_query in t.lower():
                results.append(sp)
                break
    return results


def print_wrapped(text: str, width: int = 80):
    print(textwrap.fill(text, width=width))


def main():
    speakers = load_speakers()
    print("=" * 80)
    print(" TED-Style Presentation Chatbot ")
    print("=" * 80)
    print("Ask about a speaker, e.g.:")
    print('  - "tell me about Emmanuel"')
    print('  - "summary for Sahil"')
    print('  - "who talks about AI?"')
    print('  - "list speakers"')
    print('  - "exit"\n')

    while True:
        user = input("You: ").strip()
        if not user:
            continue

        if user.lower() in ["exit", "quit", "q"]:
            print("Bot: Thank you for chatting. Keep going beyond boundaries!")
            break

        if "list" in user.lower() and "speaker" in user.lower():
            list_speakers(speakers)
            continue

        # search by tag keyword
        if "tag" in user.lower() or "#" in user:
            # extract last word as tag query
            tag_query = user.split()[-1]
            matches = find_by_tag(speakers, tag_query)
            if matches:
                print("\nBot: Here are some speakers related to that theme:\n")
                for sp in matches:
                    print(f"- {sp['name']} — {sp['presentation_title']}")
                print()
            else:
                print("\nBot: I couldn't find any talks with that tag or theme.\n")
            continue

        # try to detect a name in the query
        found = None
        for sp in speakers:
            if sp["name"].split()[0].lower() in user.lower():
                found = sp
                break

        if not found:
            # fallback: ask user for a name
            print("\nBot: Which speaker are you asking about? (first name is enough)")
            name_q = input("Speaker name: ").strip()
            found = find_by_name(speakers, name_q)

        if not found:
            print("\nBot: I couldn't find that speaker. Try 'list speakers' to see options.\n")
            continue

        # decide what kind of answer to give
        if "summary" in user.lower() or "summarize" in user.lower():
            print(f"\nBot: Here’s a short summary of {found['name']}'s talk:\n")
            print_wrapped(found["intro_paragraph"])
            print()
        elif "message" in user.lower() or "lesson" in user.lower():
            print(f"\nBot: Here’s the key message from {found['name']}:\n")
            print_wrapped(found["key_message"])
            print()
        else:
            print(f"\nBot: Here’s some information about {found['name']}:\n")
            print_wrapped(found["speaker_intro"])
            print("\nKey message:")
            print_wrapped(found["key_message"])
            print()

if __name__ == "__main__":
    main()
